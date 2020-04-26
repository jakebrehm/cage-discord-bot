import os
import sqlite3
import time
from datetime import datetime

from tabulate import tabulate


class Database:

    def __init__(self, path):

        self.path = path

    def connect(self):

        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS facts (
                id INTEGER PRIMARY KEY,
                server INTEGER,
                date TEXT,
                time TEXT,
                author INTEGER,
                status TEXT,
                fact TEXT
            )
            """
        )

    def terminate(self):
        self.connection.commit()
        self.connection.close()

    def get_approved_fact(self):
        self.cursor.execute(
            """
            SELECT fact FROM facts WHERE status="accepted"
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
            SELECT fact FROM facts WHERE status="pending"
            ORDER BY date, time LIMIT 1
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
            INSERT INTO facts (server, date, time, author, status, fact)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (server, date, time, author, status, fact),
        )
        return self.connection, self.cursor

    def judge_fact(self, fact, status):
        self.connect()
        self.cursor.execute(
            """UPDATE facts SET status=? WHERE fact=? AND status=?""",
            (status, fact, 'pending'),
        )
        self.terminate()

    def get_dialogue(self, description_id):
        self.connect()
        self.cursor.execute(
            """
            SELECT message FROM dialogue WHERE description_id=?
            ORDER BY RANDOM() LIMIT 1
            """,
            (description_id,),
        )
        dialogue = self.cursor.fetchall()
        self.terminate()
        return dialogue[0][0] if dialogue else None

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
