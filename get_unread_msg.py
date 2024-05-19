import db

def get_unread_msg(msg_notice):
    if not msg_notice:
        return None
    notice_list = []
    id_list = []
    old_id = msg_notice[0][0]
    id_list.append(old_id)
    for msg in msg_notice:
        if msg[0] != old_id:
            id_list.append(msg[0])
            old_id = msg[0]
    for id in id_list:
        data = db.do('''SELECT first_name, last_name FROM users WHERE id=?''', [id])
        user_name = data[0][0] + " " + data[0][1]
        notice_list.append((id, user_name))
    return notice_list

