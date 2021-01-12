# encoding=utf-8
import base64
from pyDes import *
import Constant


# 加密
def encrypt(str):
    k = des(Constant.DES_KEY, ECB, None, pad=None, padmode=PAD_PKCS5)
    encrypt_str = k.encrypt(str)
    return base64.b64encode(encrypt_str).decode()  # 转base64编码返回


# 解密
def decrypt(str):
    s = base64.b64decode(str)
    k = des(Constant.DES_KEY, ECB, None, pad=None, padmode=PAD_PKCS5)
    decrypt_str = k.decrypt(s, padmode=PAD_PKCS5)
    return decrypt_str.decode()


