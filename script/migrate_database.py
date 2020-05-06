import configparser
import os
import pathlib
import sqlite3

import psycopg2

# Determine relevant filepaths
SCRIPT_FOLDER = pathlib.Path(__file__).resolve().parent
PROJECT_FOLDER = SCRIPT_FOLDER.parent
DATA_FOLDER = os.path.join(PROJECT_FOLDER, 'data')
DATABASE_LOCATION = os.path.join(DATA_FOLDER, 'data.db')
CONFIG_LOCATION = os.path.join(DATA_FOLDER, 'config.ini')

# Open and read the config file
config = configparser.ConfigParser()
config.read(CONFIG_LOCATION)

# Connect to the databases and create cursors
pg_connection = psycopg2.connect(
    host=config['postgresql']['host'],
    port=config['postgresql']['port'],
    user=config['postgresql']['user'],
    password=config['postgresql']['password'],
    database=config['postgresql']['database'],
)
pg_cursor = pg_connection.cursor()
lite_connection = sqlite3.connect(DATABASE_LOCATION)
lite_cursor = lite_connection.cursor()

# Create tables in the postgresql database
pg_cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS "facts" (
        "id" SERIAL PRIMARY KEY,
        "server" BIGINT,
        "date" TEXT,
        "time" TEXT,
        "author" BIGINT,
        "status" TEXT,
        "fact" TEXT
    )
    """
)

pg_cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS "dialogue_descriptions" (
        "id" SERIAL PRIMARY KEY,
        "server" BIGINT,
        "description" TEXT
    )
    """
)

pg_cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS "dialogue" (
        "id" SERIAL PRIMARY KEY,
        "description_id" INTEGER,
        "server" BIGINT,
        "message" TEXT
    )
    """
)

pg_cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS "users" (
        "id" SERIAL PRIMARY KEY,
        "server" BIGINT,
        "user" BIGINT,
        "points" BIGINT
    )
    """
)

# Facts table
lite_cursor.execute(
    """SELECT * FROM 'facts'"""
)
fact_records = [record[1:] for record in lite_cursor.fetchall()]

pg_cursor.executemany(
    """
    INSERT INTO "facts"
    ("server", "date", "time", "author", "status", "fact")
    VALUES (%s, %s, %s, %s, %s, %s)
    """,
    fact_records
)

# Dialogue description table
lite_cursor.execute(
    """SELECT * FROM 'dialogue_descriptions'"""
)
dialogue_description_records = [record[1:] for record in lite_cursor.fetchall()]

pg_cursor.executemany(
    """
    INSERT INTO "dialogue_descriptions" ("server", "description")
    VALUES (%s, %s)
    """,
    dialogue_description_records
)

# Dialogue table
lite_cursor.execute(
    """SELECT * FROM 'dialogue'"""
)
dialogue_records = [record[1:] for record in lite_cursor.fetchall()]

pg_cursor.executemany(
    """
    INSERT INTO "dialogue" ("description_id", "server", "message")
    VALUES (%s, %s, %s)
    """,
    dialogue_records
)

# Users table
lite_cursor.execute(
    """SELECT * FROM 'users'"""
)
user_records = [record[1:] for record in lite_cursor.fetchall()]

pg_cursor.executemany(
    """
    INSERT INTO "users" ("server", "user", "points")
    VALUES (%s, %s, %s)
    """,
    user_records
)

# for record in dialogue_records:
#     print(record)

# Commit to the databases
pg_connection.commit()

# Close out cursors and databases
lite_cursor.close()
lite_connection.close()
pg_connection.close()
