import os
from datetime import datetime

import psycopg2


class Database:

    def __init__(self):

        pass

    def connect(self):

        self.connection = psycopg2.connect(
            os.environ['DATABASE_URL'],
            sslmode='require',
        )

        self.cursor = self.connection.cursor()

    def terminate(self):
        self.connection.commit()
        self.connection.close()

    def get_approved_fact(self):
        self.cursor.execute(
            """
            SELECT "fact" FROM "facts"
            WHERE "status"='accepted'
            ORDER BY RANDOM() LIMIT 1
            """
        )
        fact = self.cursor.fetchall()
        if fact:
            return fact[0][0]
        else:
            return "I don't know much about myself, apparently."

    def get_pending_fact(self):
        self.cursor.execute(
            """
            SELECT "fact" FROM "facts"
            WHERE "status"='pending'
            ORDER BY "date", "time" LIMIT 1
            """
        )
        fact = self.cursor.fetchall()
        return fact[0][0] if fact else None

    def submit_fact(self, server, author, status, fact):
        self.connect()
        date = datetime.utcnow().date().strftime(r'%Y-%m-%d')
        time = datetime.utcnow().time().strftime(r'%H:%M%:%S')
        self.cursor.execute(
            """
            INSERT INTO "facts"
            ("server", "date", "time", "author", "status", "fact")
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (server, date, time, author, status, fact),
        )
        self.terminate()
        return self.connection, self.cursor

    def judge_fact(self, fact, status):
        self.connect()
        self.cursor.execute(
            """
            UPDATE "facts"
            SET "status"=%s
            WHERE "fact"=%s AND "status"=%s
            """,
            (status, fact, 'pending'),
        )
        self.terminate()

    def get_dialogue(self, description_id):
        self.connect()
        self.cursor.execute(
            """
            SELECT "message" FROM "dialogue"
            WHERE "description_id"=%s
            ORDER BY RANDOM() LIMIT 1
            """,
            (description_id,),
        )
        dialogue = self.cursor.fetchall()
        self.terminate()
        return dialogue[0][0] if dialogue else None
    
    def add_user(self, user):
        self.connect()
        self.cursor.execute(
            """
            INSERT INTO "users" ("server", "user", "points")
            SELECT %s, %s, %s
            WHERE NOT EXISTS (
                SELECT *
                FROM "users"
                WHERE "user"=%s
            )
            """,
            (user.guild.id, user.id, 0, user.id),
        )
        self.terminate()

    def get_points(self, user):
        self.add_user(user)
        self.connect()
        self.cursor.execute(
            """
            SELECT "points" FROM "users"
            WHERE "user"=%s
            LIMIT 1
            """,
            (user.id,),
        )
        points = self.cursor.fetchall()
        self.terminate()
        return points[0][0] if points else None

    def add_points(self, user, points):
        self.add_user(user)
        self.connect()
        self.cursor.execute(
            """
            UPDATE "users"
            SET "points" = "points" + %s
            WHERE "user" = %s
            """,
            (points, user.id),
        )
        self.terminate()

    def __getitem__(self, value):
        return self.get_dialogue(value)

    @property
    def random_fact(self):
        self.connect()
        fact = self.get_approved_fact()
        self.terminate()
        return fact

    @property
    def pending_fact(self):
        self.connect()
        fact = self.get_pending_fact()
        self.terminate()
        return fact
