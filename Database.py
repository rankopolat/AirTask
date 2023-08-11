import sqlite3

conn = sqlite3.connect('airtask.db')

table = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USER';").fetchone()

if not table:
    conn.execute('''CREATE TABLE USER
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL);''')
    print("Table created successfully")
else:
    print("Already exists")
