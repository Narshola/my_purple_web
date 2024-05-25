from core.db.queries import *
from datetime import datetime
import core.db.scripts as scripts


def get_msg_list(login, chat_user):
    msg_login_list = scripts.do(login_data, [login])
    msg_user_list = scripts.do(id_data, [chat_user])
    scripts.do('''UPDATE chat SET msg_has_seen=TRUE WHERE user_id=? AND to_user_id=?''', [msg_login_list[0][0], msg_user_list[0][0]])
    msg_list = scripts.do(msg_data, [msg_login_list[0][0], msg_user_list[0][0]])
    return msg_list


def update_msg_list(login, chat_user, text):
    login_list = scripts.do(login_data, [login])
    user_list = scripts.do(id_data, [chat_user])
    msg_datetime = datetime.now()
    scripts.do(chat_insert, [login_list[0][0], user_list[0][0], text, msg_datetime])
    scripts.do(to_chat_insert, [user_list[0][0], login_list[0][0], text, msg_datetime])


def get_unread_msg(id):
    msg_notice = scripts.do(get_new_msg, [id])
    if not msg_notice:
        return None
    notice_list = []
    id_list = []
    old_id = msg_notice[0][3]
    id_list.append(old_id)
    for msg in msg_notice:
        if msg[3] != old_id:
            id_list.append(msg[3])
            old_id = msg[3]
    for id in id_list:
        data = scripts.do('''SELECT first_name, last_name, img FROM users WHERE id=?''', [id])
        user_name = data[0][0] + " " + data[0][1]
        img = data[0][2]
        notice_list.append((id, user_name, img))
    return notice_list
