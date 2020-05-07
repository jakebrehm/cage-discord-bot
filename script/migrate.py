import configparser
import os
import pathlib
import sqlite3

import psycopg2


def get_tables(cursor):
    cursor.execute(
        """
        SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'
        """
    )
    return [table[0] for table in cursor.fetchall()]


def create_tables(destination_cursor, destination='sqlite3'):

    if destination == 'sqlite3':
        primary_key = 'INTEGER PRIMARY KEY'
        integer = 'INTEGER'
    elif destination == 'postgresql':
        primary_key = 'SERIAL PRIMARY KEY'
        integer = 'BIGINT'
    else:
        raise ValueError(f'{destination} is not a supported database type.')

    # Create tables in the postgresql database
    destination_cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS "facts" (
            "id" {primary_key},
            "server" {integer},
            "date" TEXT,
            "time" TEXT,
            "author" {integer},
            "status" TEXT,
            "fact" TEXT
        )
        """
    )

    destination_cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS "dialogue_descriptions" (
            "id" {primary_key},
            "server" {integer},
            "description" TEXT
        )
        """
    )

    destination_cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS "dialogue" (
            "id" {primary_key},
            "description_id" {integer},
            "server" {integer},
            "message" TEXT
        )
        """
    )

    destination_cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS "users" (
            "id" {primary_key},
            "server" {integer},
            "user" {integer},
            "points" {integer}
        )
        """
    )


def copy_tables(origin_cursor, destination_cursor, destination='sqlite3'):

    if destination == 'sqlite3':
        p = '?'
    elif destination == 'postgresql':
        p = '%s'
    else:
        raise ValueError(f'{destination} is not a supported database type.')

    # Users table
    origin_cursor.execute(
        f"""SELECT * FROM "users" """
    )
    records = [record[1:] for record in origin_cursor.fetchall()]
    destination_cursor.executemany(
        f"""
        INSERT INTO "users"
        ("server", "user", "points")
        VALUES ({p}, {p}, {p})
        """,
        records
    )

    # Dialogue table
    origin_cursor.execute(
        f"""SELECT * FROM "dialogue" """
    )
    records = [record[1:] for record in origin_cursor.fetchall()]
    destination_cursor.executemany(
        f"""
        INSERT INTO "dialogue"
        ("description_id", "server", "message")
        VALUES ({p}, {p}, {p})
        """,
        records
    )

    # Dialogue descriptions table
    origin_cursor.execute(
        f"""SELECT * FROM "dialogue_descriptions" """
    )
    records = [record[1:] for record in origin_cursor.fetchall()]
    destination_cursor.executemany(
        f"""
        INSERT INTO "dialogue_descriptions"
        ("server", "description")
        VALUES ({p}, {p})
        """,
        records
    )

    # Facts table
    origin_cursor.execute(
        f"""SELECT * FROM "facts" """
    )
    records = [record[1:] for record in origin_cursor.fetchall()]
    destination_cursor.executemany(
        f"""
        INSERT INTO "facts"
        ("server", "date", "time", "author", "status", "fact")
        VALUES ({p}, {p}, {p}, {p}, {p}, {p})
        """,
        records
    )


if __name__ == '__main__':

    # Define origin database and destination database
    origin_database = 'postgresql'
    destination_database = 'sqlite3'
    
    # Determine relevant filepaths
    SCRIPT_FOLDER = pathlib.Path(__file__).resolve().parent
    PROJECT_FOLDER = SCRIPT_FOLDER.parent
    DATA_FOLDER = os.path.join(PROJECT_FOLDER, 'data')
    DATABASE_LOCATION = os.path.join(DATA_FOLDER, 'test.db')
    CONFIG_LOCATION = os.path.join(DATA_FOLDER, 'config.ini')

    # Open and read the config file
    config = configparser.ConfigParser()
    config.read(CONFIG_LOCATION)

    # Connect to the sqlite database and create a cursor
    lite_connection = sqlite3.connect(DATABASE_LOCATION)
    lite_cursor = lite_connection.cursor()

    # Connect to the postgres database and create a cursor
    pg_connection = psycopg2.connect(
        host=config['postgresql']['host'],
        port=config['postgresql']['port'],
        user=config['postgresql']['user'],
        password=config['postgresql']['password'],
        database=config['postgresql']['database'],
    )
    pg_cursor = pg_connection.cursor()

    create_tables(lite_cursor, destination=destination_database)
    copy_tables(pg_cursor, lite_cursor, destination=destination_database)

    # Commit to the databases
    if destination_database == 'sqlite3':
        lite_connection.commit()
    elif destination_database == 'postgresql':
        pg_connection.commit()

    # Close out cursors and databases
    lite_connection.close()
    pg_connection.close()
