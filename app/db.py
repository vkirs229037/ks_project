import sqlite3
import json
import os

DB_PATH = os.path.dirname(os.path.realpath(__file__)) + "/data/books.db"

def connect():
    return sqlite3.connect(DB_PATH)

def init():
    conn = connect()
    conn.execute("""CREATE TABLE IF NOT EXISTS Books (
                        id integer primary key,
                        title text,
                        author text,
                        year text,
                        desc text
                    );""")
    conn.commit()
    conn.close()

def search(title=None, author=None, year=None, desc=None):
    conn = connect()
    query = "SELECT * FROM Books WHERE " +\
            "title " + ("= %s" if title is not None else "") +\
            "AND author " + ("= %s" if author is not None else "") +\
            "AND year " + ("= %s" if year is not None else "") +\
            "AND desc " + ("= %s" if desc is not None else "") + ";"
    args = filter(lambda p: p is not None, [title, author, year, desc])
    cur = conn.cursor()
    cur.execute(query, args)
    return json.dumps(cur.fetchall())
