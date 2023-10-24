from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
import argparse


# ! Getting inputs in command-line


def password(pwd=None):
    ''' Password hashing to 16 bytes '''
    # hashed_pwd = SHA256.new(pwd.encode("utf-8")).digest()
    hashed_pwd = b'********************************'
    return hashed_pwd


def decoding(file_name, hashed_pwd):
    ''' Data decoding '''
    try:
        with open(file_name, 'rb') as ofile:
            # odata_iv = ofile.read(16)
            odata_iv = b"****************"
            print(odata_iv,666)
            odata = ofile.read()
            print(odata)
            decrypt = AES.new(hashed_pwd, AES.MODE_CBC, iv=odata_iv)
        with open(file_name, 'wb') as lfile:
            message = decrypt.decrypt(odata)
            print(message,77777)
            lfile.write(message)
    except FileNotFoundError:
        print("Error : File Not Found")
    except ValueError:
        print("Error : Incorrect Password")


# ! Getting input while running the python file
# file_name = input("Enter the file name to be decrypted with extension : ")
# pwd = input("Enter your password : ")
decoding('111.txt', password())
