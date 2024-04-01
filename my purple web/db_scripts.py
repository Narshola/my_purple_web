import sqlite3
import queries


def do(query):
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    return cursor.fetchall()


def insert_new(fname, lname, age, town, img, login, password):
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO users (first_name, last_name, years, town, img, login, password) VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                   [fname, lname, age, town, img, login, password])
    conn.commit()


if __name__ == "__main__":
    do(queries.drop)
    do(queries.create)
    do(queries.insert)