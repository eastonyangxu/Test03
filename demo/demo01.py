import base64

from Cryptodome import Cipher
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5 as PKCS1_v1_5_cipper

pub_key_str = """-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAuw4T755fepEyXTM66pzf6nv8NtnukQTMGnhmBFIFHp/P2vEpxjXU
BBDUpzKkVFR3wuK9O1FNmRDAGNGYC0N/9cZNdhykA1NixJfKQzncN31VJTmNqJNZ
W0x7H9ZGoh2aE0zCCZpRlC1Rf5rL0SVlBoQkn/n9LnYFwyLLIK5/d/y/NZVL6Z6L
cyvga0zRajamLIjY0Dy/8YIwVV6kaSsHeRv2cOB03eam6gbhLGIz/l8wuJhIn1rO
yJLQ36IOJymbbNmcC7+2hEQJP40qLvH7hZ1LaAkgQUHjfi8RvH2T1Jmce7XGPxCo
Ed0yfeFz+pL1KeSWNey6cL3N5hJZE8EntQIDAQAB
-----END RSA PUBLIC KEY-----"""

priv_key_str = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAuw4T755fepEyXTM66pzf6nv8NtnukQTMGnhmBFIFHp/P2vEp
xjXUBBDUpzKkVFR3wuK9O1FNmRDAGNGYC0N/9cZNdhykA1NixJfKQzncN31VJTmN
qJNZW0x7H9ZGoh2aE0zCCZpRlC1Rf5rL0SVlBoQkn/n9LnYFwyLLIK5/d/y/NZVL
6Z6Lcyvga0zRajamLIjY0Dy/8YIwVV6kaSsHeRv2cOB03eam6gbhLGIz/l8wuJhI
n1rOyJLQ36IOJymbbNmcC7+2hEQJP40qLvH7hZ1LaAkgQUHjfi8RvH2T1Jmce7XG
PxCoEd0yfeFz+pL1KeSWNey6cL3N5hJZE8EntQIDAQABAoIBAGim1ayIFK8EMQNH
uDyui/Aqcc9WWky0PGTK23irUsXxb1708gQ89WNY70Cj6qBrqZ1VMb3QHPP4FSFN
kh0rJJoi2g+ssm5R5r5KlhTKeFRrQInVC1Y3KhUUUwZa4aWtnhgSJ7Urq1yVhjU4
K7PVkhH1OHBwcp/d1Bd6jd65AgPkY63P+WpcARJkClmQ1RhgoRwThyJdpKrV4/gO
ha0AUGlJNRNvRwiZxP0zaI5C8RdrG96SnVpeYOcD0z/M1HVlkoYMXsXLKttwLfpK
88Igtm6ZJwRpfuMF5VA+9hHaYGCBdGz0B/rMp2fc+EtrOavYQGrWIWi2RL1Qk6Rt
BUyeTgECgYEA9anj4n/cak1MT+hbNFsL31mJXryl1eVNjEZj/iPMztpdS15CmFgj
Kjr9UuintjSiK7Is43nZUWWyP1XQjRhVi2uP7PRIv92QNl/YteWD6tYCInJHKe2J
QqYyZrElezsdayXb5DK6bi1UIYYji90g79N7x6pOR0UnQNQUXTv+Y8ECgYEAwuzl
6Ez4BSXIIL9NK41jfNMa73Utfl5oO1f6mHM2KbILqaFE76PSgEeXDbOKdcjCbbqC
KCGjwyPd+Clehg4vkYXTq1y2SQGHwfz7DilPSOxhPY9ND7lGbeNzDUK4x8xe52hd
MWKdgqeqCK83e5D0ihzRiMah8dbxmlfLAOZ3sPUCgYEA0dT9Czg/YqUHq7FCReQG
rg3iYgMsexjTNh/hxO97PqwRyBCJPWr7DlU4j5qdteobIsubv+kSEI6Ww7Ze3kWM
u/tyAeleQlPTnD4d8rBKD0ogpJ+L3WpBNaaToldpNmr149GAktgpmXYqSEA1GIAW
ZAL11UPIfOO6dYswobpevYECgYEApSosSODnCx2PbMgL8IpWMU+DNEF6sef2s8oB
aam9zCi0HyCqE9AhLlb61D48ZT8eF/IAFVcjttauX3dWQ4rDna/iwgHF5yhnyuS8
KayxJJ4+avYAmwEnfzdJpoPRpGI0TCovRQhFZI8C0Wb+QTJ7Mofmt9lvIUc64sff
GD0wT/0CgYASMf708dmc5Bpzcis++EgMJVb0q+ORmWzSai1NB4bf3LsNS6suWNNU
zj/JGtMaGvQo5vzGU4exNkhpQo8yUU5YbHlA8RCj7SYkmP78kCewEqxlx7dbcuj2
LAPWpiDca8StTfEphoKEVfCPHaUk0MlBHR4lCrnAkEtz23vhZKWhFw==
-----END RSA PRIVATE KEY-----"""


# 根据key长度计算分块大小
def get_block_size(rsa_key):
    try:
        # RSA仅支持限定长度内的数据的加解密，需要分块
        # 分块大小
        reserve_size = block_reversed_size = 11
        key_size = rsa_key.size_in_bits()
        print(key_size)
        if (key_size % 8) != 0:
            raise RuntimeError('RSA 密钥长度非法')

        # 密钥用来解密，解密不需要预留长度
        if rsa_key.has_private():
            reserve_size = 0

        bs = int(key_size / 8) - reserve_size
    except Exception as err:
        print('计算加解密数据块大小出错', rsa_key, err)
    return bs


# 返回块数据
def block_data(data, rsa_key):
    bs = get_block_size(rsa_key)
    for i in range(0, len(data), bs):
        yield data[i:i + bs]


# 加密
def enc_bytes(data, key=None):
    text = b''
    try:
        rsa_key = key
        if key:
            rsa_key = key

        cipher = PKCS1_v1_5_cipper.new(rsa_key)
        for dat in block_data(data, rsa_key):
            cur_text = cipher.encrypt(dat)
            text += cur_text
    except Exception as err:
        print('RSA加密失败', data, err)
    return text


a = 'adfajodfsdjfoasidjfoadsjgoiasjdoijasdoifjaoidjfoiadfasidjfoiasdjfoiasdjfadf' \
    'dfasdfadsfjaoisdfjaoisjdfoaijsdfoiajsdoifjaoisdfjadjfa' \
    'adfdasdfjadjfasjdfaiosdjfpaidsjfaijdfoiajdsofjaodjfad' \
    'adfaoisdjfopajdsfoajsdofjasodjfoasdjfoiajdiofjaoiwefiqwe09wefjasd' \
    'adsfopajdfojadfja9djfadjfajdsoifjoasidjfpaodjfoajsdofjasdojfoiajd' \
    'nininini'


def rsa_key_str2std(skey):
    ret = None
    try:
        ret = RSA.importKey(skey)
    except Exception as err:
        print('字符串密钥转rsa格式密钥错误', skey, err)
    return ret


print(len(pub_key_str))

pu_key = rsa_key_str2std(pub_key_str)
jiami = (enc_bytes(bytes(a, encoding='utf-8'), pu_key))
print(base64.b64encode(jiami))


# print('abc'.size_in_bits())


# 解密
def dec_bytes(data, key=None):
    text = b''
    try:
        rsa_key = key
        if key:
            rsa_key = key

        cipher = PKCS1_v1_5_cipper.new(rsa_key)
        for dat in block_data(data, rsa_key):
            if type(PKCS1_v1_5_cipper) == True:
                cur_text = cipher.decrypt(dat)
            else:
                cur_text = cipher.decrypt(dat, '解密异常')
            text += cur_text
    except Exception as err:
        print('RSA解密失败', data, err)
    return text


tt = 'Fkr7ef4MXOxXesZ2FAdAKub4iUk0CV9STAeJ3BDtqYTDuo' \
     'cjQnQmaSGoLhRpFMdOXpwjkQg6tKsiBcU6b5ADjMJzZ8SRdM' \
     's2j0XhGtV6ZooKD7AhJcAJPIZTFd2cglwPGwNTbfqWf0ETCnMz05D' \
     'xFovhW0gi9qL6ZXqerOh4ztRbXKOtg1Jppm0mXyGxQRUq5JNrhlQsy50v' \
     'usiYzQNUOL4v1KgOVK8RH37DdhSHhjSsRtbIua7GYsLgpmJHPrSPLsFByZvT4J' \
     'puG5XyEJ/c7QydP5EyeoHFgX5rYCZ2yxakoI7anJL6Zz3rZkWTzt9By+PW9cm1jb' \
     'egz6Vb4A4sf6tqCZy+ksYL9BeYQ7z6HBtrITVnK1IcpsyDXYjPa7LwqP/z1IEgFT' \
     'Du1dzNyHds6ZZkalC1QM7S5NJsL2XTTGUeZkU0P3/YjOFS0+T1hmkCP4TmgMRT0up' \
     '+scpXpZwqKG1flBT8oiWqKgk7MNmHyl7KVG4QLLPRBxUmiBviaBkRkT3ZiFwNP7/0w' \
     'IprvfpoIa5/8y9vof0Z0HHZXB0A+dbGA8nRTG+jJaH4UQKxIv1h2fKxrqAf0wnjq+M/Ra' \
     'kp8/1lMTj1iNkTLJ+/w4fe9JqvDXyzzJxcTfGTVNz5pWNupN2ytcpM6lVOlmedARCCEINsM' \
     '8kd1hCEPgDYPJjYmkE='

tt2 = 'Sct4vW2CD8/RqLuBp3rcKqIbcKYHo5NmOnZh3ySxbXs+X3cCzePiD5L1oU2U3rJQ9e4j5lroz/CvVu4ycv65cdnfiscwdpm71cxYevG+8QWKVC5OaqUDi2MaTMqIMdsisZlsDY7wQfQEVDmByPFOWp5JWjkHZX3qD4771kPSoVdbmUhNj4SGawZMxIvv94cQuiQs3CmvR5HDO9CRzeAeZZvPy0+OqjgTqMI/TYXw9aWtNoT65DJhI4uSPylg/Zze9kAfCSnjg85QzJ9fCP/cCyOuiYfsvdA+yOpE5sX+NewhhA3w/ceh5/dkQAj5EpIiG3wWD3zbRQC4oIarxeSbjhGA2eGV8QQE4AL3NjvNyo8VXpaFJdMvQr1Py7PJK8zc+wlXQUybEN38ZEZ8IqP8jnGNsR046zoe+snCckuDRRGiuyGUAIww32IN+FzwqleKouJyaEXh1eycEy0NwUPlZyT/hTBMYOPOTmtK6grHjlqZ++b8TuCxqTkJVzJdA0czpP54UA51K3I+Ij2X6GzpI46fEJhFSFx0C2/LJq6/8moyNZGhl3+V/G4l88G4kcolwFF9R7/saghGrTXYMtJfJ46Dv2ZQrrkGsKAIypEufyHcbIPamFUuzVEKcMAegVw4G1XtFpWoP/jVtlx2f04DLKEhJ8XEg2P8nAN6ZJ/86Sg='

pr_key = rsa_key_str2std(priv_key_str)
tex = base64.b64decode(tt)
jiemi = (dec_bytes(tex, pr_key))
print(jiemi)
