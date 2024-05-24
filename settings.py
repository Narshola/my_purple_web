from queries import *
from datetime import datetime
import db

def get_msg_list(login, chat_user):
    msg_login_list = db.do(login_data, [login])
    msg_user_list = db.do(id_data, [chat_user])
    db.do('''UPDATE chat SET msg_has_seen=TRUE WHERE user_id=? AND to_user_id=?''', [msg_login_list[0][0], msg_user_list[0][0]])
    msg_list = db.do(msg_data, [msg_login_list[0][0], msg_user_list[0][0]])
    return msg_list

def update_msg_list(login, chat_user, text):
    login_list = db.do(login_data, [login])
    user_list = db.do(id_data, [chat_user])
    msg_datetime = datetime.now()
    db.do(chat_insert, [login_list[0][0], user_list[0][0], text, msg_datetime])
    db.do(to_chat_insert, [user_list[0][0], login_list[0][0], text, msg_datetime])