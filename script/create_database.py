import os
import sqlite3


path = os.path.join('..', 'data', 'data.db')

connection = sqlite3.connect(path)
cursor = connection.cursor()

# cursor.execute(
#     """CREATE TABLE IF NOT EXISTS facts (
#         id INTEGER PRIMARY KEY,
#         server INTEGER,
#         date TEXT,
#         time TEXT,
#         author INTEGER,
#         status TEXT,
#         fact TEXT
#     )"""
# )

# cursor.execute(
#     """CREATE TABLE IF NOT EXISTS dialogue_descriptions (
#         id INTEGER PRIMARY KEY,
#         server INTEGER,
#         description TEXT
#     )"""
# )

# cursor.execute(
#     """CREATE TABLE IF NOT EXISTS dialogue (
#         id INTEGER PRIMARY KEY,
#         description_id INTEGER,
#         server INTEGER,
#         message TEXT
#     )"""
# )



# dialogue = [
#     (1	, 701467145342812240, "Don't worry {name}, I'm here."),
#     (1	, 701467145342812240, "No need to worry {name}, I would never leave you."),
#     (2	, 701467145342812240, "I'm not sure what you're asking me to do, {name}."),
#     (3	, 701467145342812240, "Sorry {name}, I can't let you do that."),
#     (4	, 701467145342812240, "That's ridiculous, {name}. Goodbye."),
#     (4	, 701467145342812240, "That is utter blasphemy. Get out of here, {name}."),
#     (5	, 701467145342812240, "That was ugly. I'm sorry, everyone."),
#     (5	, 701467145342812240, "That was awful. I'm really sorry you had to see that, guys."),
#     (6	, 701467145342812240, "Kicked {name}."),
#     (7	, 701467145342812240, "Banned {name}."),
#     (8	, 701467145342812240, "Unbanned {name}."),
#     (9	, 701467145342812240, "No pending facts. Apparently I'm not very interesting."),
#     (10	, 701467145342812240, "Maybe you can help me. I'm not sure about this fact:"),
#     (11	, 701467145342812240, "Sorry {name}, you were too slow."),
#     (12	, 701467145342812240, "Another time, then…"),
#     (13	, 701467145342812240, "Thanks for accepting the submission, {name}."),
#     (14	, 701467145342812240, "The submission has been rejected."),
#     (15	, 701467145342812240, "Thanks for reminding me, {name}. I can't believe I forgot."),
#     (16	, 701467145342812240, "What are you trying to remind me of, {name}? I don't understand."),
# ]

# description = [
#     (701467145342812240, "When pinged"),
#     (701467145342812240, "On CommandNotFound error"),
#     (701467145342812240, "On MissingPermissions error"),
#     (701467145342812240, "Before a user who says they don't know Nicolas Cage is kicked"),
#     (701467145342812240, "After a user who says they don't know Nicolas Cage is kicked"),
#     (701467145342812240, "When a user if kicked"),
#     (701467145342812240, "When a user is banned"),
#     (701467145342812240, "When a user is unbanned"),
#     (701467145342812240, "When a user wants to judge pending facts but there are none"),
#     (701467145342812240, "Tidbit displayed before the pending submission when a user is judging"),
#     (701467145342812240, "If the user doesn't judge the pending submission in time"),
#     (701467145342812240, "If the user chooses to abstain while judging"),
#     (701467145342812240, "If the user chooses to accept a submission while judging"),
#     (701467145342812240, "If the user chooses to reject a submission while judging"),
#     (701467145342812240, "When the user submits a fun fact"),
#     (701467145342812240, "When the user uses the submit command with an unknown subcommand"),
# ]


# for d in dialogue:
#     cursor.execute(
#         """
#         INSERT INTO dialogue (description_id, server, message) VALUES (?, ?, ?)
#         """,
#         (d[0], d[1], d[2]),
#     )

# for d in description:
#     cursor.execute(
#         """
#         INSERT INTO dialogue_descriptions (server, description) VALUES (?, ?)
#         """,
#         (d[0], d[1]),
#     )


# cursor.execute(
#     """
#     SELECT message FROM dialogue WHERE description_id=?
#     ORDER BY RANDOM() LIMIT 1
#     """,
#     (5,),
# )

from tabulate import tabulate

# cursor.execute("""SELECT * FROM dialogue_descriptions""")

# print(cursor.fetchall())

# cursor.execute("""SELECT * FROM dialogue_descriptions""")
# print(cursor.fetchone())
# print(cursor.description)

cursor.execute("""SELECT id, description FROM dialogue_descriptions""")
# print(cursor.fetchone())
# description = cursor.description
columns = [d[0] for d in cursor.description]
data = cursor.fetchall()
print(columns)

table = tabulate(data, headers=columns, tablefmt='github')
print(table)

connection.commit()
connection.close()