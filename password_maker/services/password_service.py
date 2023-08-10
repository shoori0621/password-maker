from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Padding
from hashlib import pbkdf2_hmac
from django.conf import settings
import logging

'''
暗号化
'''
def encrypt(text):

    salt = get_random_bytes(16)
    iv = get_random_bytes(16)

    # AESキーの生成(128bit、5万回)
    key = pbkdf2_hmac('sha256', bytes(settings.SECRET_KEY, encoding='utf-8'), salt, 50000, int(128 / 8))

    # 暗号
    aes = AES.new(key, AES.MODE_CBC, iv)
    data = Padding.pad(text.encode('utf-8'), AES.block_size, 'pkcs7')
    encrypted = aes.encrypt(data)

    return {
        'salt': salt,
        'iv': iv,
        'encrypted': encrypted
    }


'''
複合化
'''
def decrypt(encryptedData):
    # AESキーの生成(128bit、5万回)
    key = pbkdf2_hmac('sha256', bytes(settings.SECRET_KEY, encoding='utf-8'), encryptedData.salt, 50000, int(128 / 8))

    # 復号
    aes = AES.new(key, AES.MODE_CBC, encryptedData.iv)
    plaintext = aes.decrypt(encryptedData.password)

    return plaintext.decode(encoding='utf-8')
