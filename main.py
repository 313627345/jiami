import binascii
import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# key一定要32位
key = b"********************************"
# 偏移量一定要16位
iv = b"****************"


def encrypt(data):
    # 参数key: 秘钥，要求是bytes类型，并且长度必须是16、24或32 bytes，因为秘钥的长度可以为：128位、192位、256位
    # 参数mode: 加密的模式，有ECB、CBC等等，最常用的是CBC
    # 参数iv: 初始向量，是CBC加密模式需要的初始向量，类似于加密算法中的盐
    # 创建用于加密的AES对象
    cipher1 = AES.new(key, AES.MODE_CBC, iv)
    # 使用对象进行加密，加密的时候，需要使用pad对数据进行填充，因为加密的数据要求必须是能被128整除
    hex_data= bytes(data, 'UTF-8')
    # pad参数内容，第一个是待填充的数据，第二个是填充成多大的数据，需要填充成128位即16bytes
    ct = cipher1.encrypt(pad(hex_data, 16))
    # 将加密后的结果（二进制）转换成十六进制的或者其它形式
    ct_hex = binascii.b2a_hex(ct)
    return ct_hex


def decrypt(data):
    # 创建用于解密的AES对象
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    # 将十六进制的数据转换成二进制
    hex_data = binascii.a2b_hex(data)
    # 解密完成后，需要对数据进行取消填充，获取原来的数据
    pt = unpad(cipher2.decrypt(hex_data), 16)
    return pt


def encrypt_file(filename):
    with open(filename, 'rb') as entry:
        # 读取文件转成二进制流
        filedata = entry.read()
        # 构建加密算法模式
        encry = AES.new(key, AES.MODE_CBC, iv)
        # 生成加密文件并以后缀 .enc 来命名
        with open(filename + ".enc", 'wb') as f:
            # 加密内容
            message = encry.encrypt(pad(filedata, 16))
            # 写入文件
            f.write(message)
    # 删除源文件
    os.remove(filename)


def decrypt_file(filename):
    with open(filename, 'rb') as ofile:
        # 读取加密文件
        filedata = ofile.read()
        # 构建解密算法模式
        decry = AES.new(key, AES.MODE_CBC, iv)
        # 创建空白文件 去掉.enc
        with open(filename[:-4], 'wb') as lfile:
            # 解密内容
            message = unpad(decry.decrypt(filedata), 16)
            # 写入文件
            lfile.write(message)
    # 删除源文件
    os.remove(filename)


if __name__ == '__main__':
    # 字符串加密解密
    print(encrypt('hello word'))
    print(decrypt('4c479299f12cd14e297115ee1f665538'))

    # 文件加密解密
    # encrypt_file('诗酒趁年华 - 挪威的森林.flac')
    # decrypt_file('诗酒趁年华 - 挪威的森林.flac.enc')
