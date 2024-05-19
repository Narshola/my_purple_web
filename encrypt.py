import hashlib

def encrypt(data):
    enc = hashlib.sha256()
    enc.update(data.encode())
    enc_data = enc.hexdigest()
    return enc_data


if __name__ == "__main__":
    s = "Hello"
    s1 = encrypt(s)
    print(s1)
    # msg_notie = [(6, 'z'), (6, 'a'), (5, 'dg'), (5, 'fdg'), (5, 'dfh'), (4, 'sg')]
    # print(get_unread_msg(msg_notie))