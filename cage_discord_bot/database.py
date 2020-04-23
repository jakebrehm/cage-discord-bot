import os
import sqlite3
import time
from datetime import datetime


class Database:

    def __init__(self, path):

        self.path = path

        self.connect()

    def connect(self):

        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()

        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS facts (
                id INTEGER PRIMARY KEY,
                server INTEGER,
                date TEXT,
                time TEXT,
                author INTEGER,
                status TEXT,
                fact TEXT
            )"""
        )

    def terminate(self):
        self.connection.commit()
        self.connection.close()

    def get_fact(self):
        self.cursor.execute(
            """SELECT fact FROM facts WHERE status="accepted"
               ORDER BY RANDOM() LIMIT 1"""
        )
        fact = self.cursor.fetchall()[0][0]
        if fact:
            return fact
        else:
            return "I don't know much about myself, apparently."

    def submit_fact(self, server, author, status, fact):
        date = datetime.utcnow().date().strftime(r'%Y-%m-%d')
        time = datetime.utcnow().time().strftime(r'%H:%M%:%S')
        self.cursor.execute(
            """INSERT INTO facts (server, date, time, author, status, fact)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (server, date, time, author, status, fact),
        )
        return self.connection, self.cursor

    @property
    def random_fact(self):
        self.connect()
        fact = self.get_fact()
        self.terminate()
        return fact