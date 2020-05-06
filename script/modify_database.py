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
connection = psycopg2.connect(
    host=config['postgresql']['host'],
    port=config['postgresql']['port'],
    user=config['postgresql']['user'],
    password=config['postgresql']['password'],
    database=config['postgresql']['database'],
)
cursor = connection.cursor()


# server = 701467145342812240

# description = "When requesting the amount of points another user has"
# message = "User {name} has {points} points."
# dialogue_id = 19

# description = "When giving points to another user"
# message = "User {name} has been given {points}."
# message = "Congratulations, {name}! You have been given {points} points."
# dialogue_id = 20



# cursor.execute(
#     """
#     INSERT INTO "dialogue_descriptions" ("server", "description")
#     VALUES (%s, %s)
#     """,
#     (server, description)
# )

# cursor.execute(
#     """
#     INSERT INTO "dialogue" ("description_id", "server", "message")
#     VALUES (%s, %s, %s)
#     """,
#     (dialogue_id, server, message)
# )


cursor.execute(
    """
    DELETE FROM dialogue_descriptions
    WHERE id=21
    """
)


# Create tables in the postgresql database
cursor.execute("""SELECT * FROM dialogue""")
for result in cursor.fetchall():
    print(result)

cursor.execute("""SELECT * FROM dialogue_descriptions""")

print('\n')
print('\n')

for result in cursor.fetchall():
    print(result)

# Commit to the databases
connection.commit()

# Close out cursors and databases
connection.close()
