import hashlib

def encrypt(data):
    enc = hashlib.sha256()
    enc.update(data.encode())
    enc_data = enc.hexdigest()
    return enc_data