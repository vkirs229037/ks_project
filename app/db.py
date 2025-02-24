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

def search(title, author, year, desc):
    conn = connect()
    query = build_query(title, author, year, desc)
    print("DEBUG:", query)
    args = list(map(lambda s: "%" + s + "%", filter(lambda p: p is not None, [title, author, year, desc])))
    cur = conn.cursor()
    print("DEBUG:", args)
    cur.execute(query, args)
    json_result = json.dumps(cur.fetchall())
    conn.close()
    return json_result

def build_query(title, author, year, desc):
    query_prelude = "SELECT * FROM Books"
    query_args = []
    if title is not None:
        query_args += ["title LIKE ?"]
    if author is not None:
        query_args += ["author LIKE ?"]
    if year is not None:
        query_args += ["year LIKE ?"]
    if desc is not None:
        query_args += ["desc LIKE ?"]
    result = query_prelude + (" WHERE " if len(query_args) > 0 else "") + " AND ".join(query_args) + ";"
    return result

def get(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Books WHERE id = ?", (id,))
    result = cur.fetchall()
    conn.close()
    if len(result) == 0:
        return None
    else:
        return result[0]