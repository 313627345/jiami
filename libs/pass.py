#!/usr/bin/python3

from Crypto import Random
from Crypto.Cipher import AES
import binascii


def decrypt(textEncrypted, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(textEncrypted[AES.block_size:])
    return plaintext.rstrip(b"\0")


def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".aes256", 'wb') as fo:
        fo.write(enc)


def decrypt_file(file_name, key, iv):
    with open(file_name, 'rb') as fo:
        textEncrypted = fo.read()
    dec = decrypt(textEncrypted, key, iv)
    with open(file_name + ".decrypt", 'wb') as fo:
        fo.write(dec)


print("### This script only work for AES-CBC-256. ###\n## The decrypted will have the .decrypt extension added ##")
key = binascii.unhexlify(input("please enter the key :"))
iv = binascii.unhexlify(input("Please enter the IV : "))
filename = input("please enter the filename to decrypt : ")
decrypt_file(filename, key, iv)