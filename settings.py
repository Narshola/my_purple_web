from queries import *
import db

def get_msg_list(login, chat_user):
    msg_login_list = db.do(login_data, [login])
    msg_user_list = db.do(id_data, [chat_user])
    db.do('''UPDATE chat SET msg_has_seen=TRUE WHERE user_id=? AND to_user_id=?''', [msg_user_list[0][0], msg_login_list[0][0]])
    db.do('''UPDATE chat SET msg_has_seen=TRUE WHERE user_id=? AND to_user_id=?''', [msg_login_list[0][0], msg_user_list[0][0]])
    msg_list = db.do(msg_data, [msg_login_list[0][0], msg_user_list[0][0]])
    return msg_list