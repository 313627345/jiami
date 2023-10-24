from Crypto.Cipher import AES
import os


# 加密算法，key 为 16、24 或 32 个字符的字符串

def encrypt_file(key, in_filename, out_filename=None, chunksize=64 * 1024):
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = os.urandom(AES.block_size)  # 随机生成密钥

    encryptor = AES.new(key, AES.MODE_CBC, iv)

    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(filesize.to_bytes(8, 'big'))  # 写入文件大小
            outfile.write(iv)  # 写入密钥向量

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % AES.block_size != 0:
                    chunk += b' ' * (AES.block_size - len(chunk) % AES.block_size)

                outfile.write(encryptor.encrypt(chunk))


# 使用方式：encrypt_file(‘mypassword’, ‘mytest.py’)

# 解密算法，key 为 16、24 或 32 个字符的字符串
def decrypt_file(key, in_filename, out_filename=None, chunksize=64 * 1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        orig_size = int.from_bytes(infile.read(8), 'big')
        iv = infile.read(AES.block_size)

        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(orig_size)


# 使用方式：decrypt_file('mypassword', 'mytest.pyc.enc')

encrypt_file('********************************', '../main.py')
