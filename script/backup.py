import configparser
import csv
import os
import pathlib
import sqlite3
from datetime import datetime

import psycopg2

# Determine relevant filepaths
SCRIPT_FOLDER = pathlib.Path(__file__).resolve().parent
PROJECT_FOLDER = SCRIPT_FOLDER.parent
DATA_FOLDER = os.path.join(PROJECT_FOLDER, 'data')
BACKUP_LOCATION = os.path.join(DATA_FOLDER, 'csv_backups')
CONFIG_LOCATION = os.path.join(DATA_FOLDER, 'config.ini')

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
cursor = connection.cursor()

now = datetime.now().strftime(r'%Y-%m-%d %H:%M:%S')

tables = ['users', 'dialogue_descriptions', 'dialogue']
data = []
for table in tables:
    cursor.execute("""
        SELECT * FROM %s
    """ % (table,))
    data.append(cursor.fetchall())

destination = os.path.join(BACKUP_LOCATION, now)
os.makedirs(destination, exist_ok=False)

for table, datum in zip(tables, data):
    filename = os.path.join(destination, f'{table}.csv')
    print(filename)
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(datum)

# Close out cursors and databases
connection.close()