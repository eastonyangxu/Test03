import rsa

# rsa生成公钥和私钥
pub, pri = rsa.newkeys(123)
print(pub)
print(pri)

# pubkey = rsa.PublicKey.load_pkcs1('1234'.encode())
# print(pubkey)

message = 'hello'
# 公钥加密
crypto = rsa.encrypt(message.encode(), pub)
# 私钥解密
message = rsa.decrypt(crypto, pri).decode()

print(message)
