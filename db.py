import sqlite3
import queries
from encrypt import encrypt

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
    # do(queries.drop_users)
    # do(queries.create_users)
    # do(queries.insert_users)

    # do(queries.drop_chat)
    # do(queries.create_chat)
    login_list = do(queries.login_data, ['ahmed'])
    user_list = do(queries.login_data, ['bota'])
    msg_list = do('''SELECT * FROM chat WHERE user_id = ? AND to_user_id = ?''', [login_list[0][0], user_list[0][0]])
    print(msg_list)