import hashlib

def encrypt(data):
    enc = hashlib.sha256()
    enc.update(data.encode())
    enc_data = enc.hexdigest()
    return enc_data


def get_form(form_list):
    elem_dict = {}
    for elem in form_list:
        key = elem[0]
        value = elem[1][0]
        elem_dict[key] = value
    return elem_dict

#[('fname', ['Test']), ('lname', ['Botyara']), ('age', ['87']), ('town', ['Nowt']), ('login', ['bot']), ('password', ['1']), ('password_commit', ['1']), ('img', ['https'])]

if __name__ == "__main__":
    s = "Hello"
    s1 = encrypt(s)
    print(s1)