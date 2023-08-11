import sqlite3



conn = sqlite3.connect('airtask.db')

table = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USER';").fetchone()

if not table:
    conn.execute('''CREATE TABLE USER
         (USERNAME TEXT PRIMARY KEY     NOT NULL,
          EMAIL           TEXT    NOT NULL,
          PASSWORD       TEXT     NOT NULL);''')

    print("Table created successfully")

else:
    print("Already exists")

