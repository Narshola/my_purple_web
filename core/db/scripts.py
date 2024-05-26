from core.functions.encrypt import encrypt
import core.db.queries as queries
import sqlite3

def do(query, *args):
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()
    cursor.execute(query, *args)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data


def insert_new(form_dict):
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()
    cursor.execute(queries.new_insert, [form_dict['fname'], form_dict['lname'], form_dict['age'], form_dict['town'], form_dict['img'], form_dict['login'], encrypt(form_dict['password'])])
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    do(queries.drop_users)
    do(queries.create_users)
    do(queries.insert_users)

    do(queries.drop_chat)
    do(queries.create_chat)
