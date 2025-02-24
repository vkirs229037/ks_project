import sqlite3
import os

content = []
FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../data/books_list.txt"
with open(FILE_PATH) as f:
    content = f.readlines()

DB_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../data/books.db"
conn = sqlite3.connect(DB_PATH)

id = 1

for entry in content:
    title, author, year, desc = entry.split("%")
    conn.execute("INSERT INTO Books VALUES (?, ?, ?, ?, ?)", (id, title, author, year, desc))
    id += 1

conn.commit()
conn.close()