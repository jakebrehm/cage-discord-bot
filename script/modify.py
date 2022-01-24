



import configparser
import os
import pathlib
import sqlite3

import psycopg2

# Determine relevant filepaths
SCRIPT_FOLDER = pathlib.Path(__file__).resolve().parent
PROJECT_FOLDER = SCRIPT_FOLDER.parent
DATA_FOLDER = os.path.join(PROJECT_FOLDER, 'data')
# DATABASE_LOCATION = os.path.join(DATA_FOLDER, 'data.db')
CONFIG_LOCATION = os.path.join(DATA_FOLDER, 'config.ini')

print(SCRIPT_FOLDER)
print(PROJECT_FOLDER)
print(DATA_FOLDER)
print(CONFIG_LOCATION)

# Open and read the config file
config = configparser.ConfigParser()
config.read(CONFIG_LOCATION)

# Connect to the databases and create cursors
connection = psycopg2.connect(
    host=config['database']['host'],
    port=config['database']['port'],
    user=config['database']['user'],
    password=config['database']['password'],
    database=config['database']['database'],
)
SERVER = config['discord']['server']
cursor = connection.cursor()

# Functions to add records to database
def add_description(dialogue_id, SERVER, description):
    cursor.execute(
        """
        INSERT INTO "dialogue_descriptions" ("id", "server", "description")
        VALUES (%s, %s, %s)
        """,
        (dialogue_id, SERVER, description)
    )

def add_dialogue(dialogue_id, SERVER, message):
    cursor.execute(
        """
        INSERT INTO "dialogue" ("description_id", "server", "message")
        VALUES (%s, %s, %s)
        """,
        (dialogue_id, SERVER, message)
    )

# EDIT HERE - use the above functions here
# add_description(27, SERVER, "When the user prompts the react role selector")
# add_dialogue(27, SERVER, """To see certain channels, and to get certain notifications, you must have the appropriates roles.\nYou are free to choose which roles you do and do not want.```\nPlease choose your roles by reacting to this message.\n```\n🎮 for Gamer""")

# add_description(28, SERVER, "When giving the user a fact count")
# add_dialogue(28, SERVER, "There are {guild_facts} facts for this server, and {total_facts} in total.")

# add_description(29, SERVER, "When giving the user a user count")
# add_dialogue(29, SERVER, "I'm tracking points for {guild_users} users in this server, and {total_users} in total.")

# add_description(30, SERVER, "When giving the user a server count")
# add_dialogue(30, SERVER, "Believe it or not, I am currently in {total_servers} servers.")

# add_description(31, SERVER, "When the user uses the count command with an unknown subcommand")
# add_dialogue(31, SERVER, "What do you want me to count up, {name}?")

# add_description(1, SERVER, "When pinged")

# cursor.execute(
#         """
#         DELETE FROM "dialogue_descriptions"
#         WHERE "id"=28
#         """
#     )

# description = "When the user prompts the game-specific react role selector"
# message = """If you chose the 🎮 Gamer role, you must also choose game-specific roles to see their channels.

# ```
# Please choose roles for specific games by reacting to this message.
# ```
# <:runescape:934989869938274334> for RuneScape
# <:amongus:934989768406749244> for Among Us
# <:callofduty:934989843279261726> for Call of Duty
# <:back4blood:934989791961952256> for Back 4 Blood
# <:residentevil:934990033771978792> for Resident Evil
# """
# dialogue_id = 32
# add_description(dialogue_id, SERVER, description)
# add_dialogue(dialogue_id, SERVER, message)

# # Commit to the databases
# connection.commit()

# Close out cursors and databases
connection.close()