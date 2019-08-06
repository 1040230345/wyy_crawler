import os, json
from  binascii import hexlify
from Crypto.Cipher import AES
import base64


class Encrypyed():
    def __init__(self):
        # 加密的固有参数
        self.pub_key = "010001"
        self.modulus = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff6" \
                       "8ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee34" \
                       "1f56135fccf695280104e0312ecbda92557c93870114af6c9d05c" \
                       "4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e820" \
                       "47b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        self.nonce = "0CoJUm6Qyw8W8jud"

    # 随机产生16位参数
    def a(self, size):
        return hexlify(os.urandom(size))[:16].decode('utf-8')

    # 加密
    def b(self,text, key):
        iv = '0102030405060708'
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        result = encryptor.encrypt(text)
        result_str = base64.b64encode(result).decode('utf-8')
        return result_str

    # 产生第二个参数
    def c(self, text, pubKey, modulus):
        text = text[::-1]
        rs = pow(int(hexlify(text.encode('utf-8')), 16), int(pubKey, 16), int(modulus, 16))
        return format(rs, 'x').zfill(256)

    # 赋值加密
    def d(self, text):
        text = json.dumps(text)
        i = self.a(16)
        encText = self.b(text, self.nonce)
        encText = self.b(encText,i)
        encSecKey = self.c(i,self.pub_key,self.modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        return data




