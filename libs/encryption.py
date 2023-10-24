from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
import argparse

# ! Getting inputs in command-line


def password(pwd):
    ''' Password hashing to 16 bytes '''
    # hashed_pwd = SHA256.new(pwd.encode("utf-8")).digest()
    hashed_pwd = b'********************************'
    return hashed_pwd


def encoding(file_name, hashed_pwd):
    ''' Data encoding '''
    try:
        with open(file_name, 'rb') as entry:
            data = entry.read()
            encrypt = AES.new(hashed_pwd, AES.MODE_CBC)
            message = encrypt.encrypt(pad(data, AES.block_size))
            print(message,9999)
        with open(file_name, 'wb') as wfile:
            print(encrypt.iv,77777)
            wfile.write(encrypt.iv)
            wfile.write(message)
    except FileNotFoundError:
        print("Error : File Not Found")

    # ! Getting input while running the python file


# file_name = input("Enter the file name with extension : ")
# pwd = input("Enter your password : ")

encoding('456.txt', password('123'))
