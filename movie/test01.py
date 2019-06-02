from collections import OrderedDict

import requests

test_dict = OrderedDict({
    ('fxid', '2019100'),
    ('fxddh', '123'),
    ('fxdesc', '123'),
    ('fxfee', '100'),
    ('fxnotifyurl', '123'),
    ('fxnotifyurl', '123'),
    ('fxpay', 'demo'),
    ('fxip', '123.123.123'),
    ('fxattch', 'demo'),
    ('fxsign', 'demo'),
})

test_dict2 = OrderedDict({
    'fxid': '2019100',
    'fxddh': '123',
    'fxdesc': '123',
    'fxfee': '100',
    'fxnotifyurl': '123',
    'fxnotifyurl2': '123',
    'fxpay': 'demo',
    'fxip': '123.123.123',
    'fxattch': 'demo',
    'fxsign': 'demo',
})

# headers = {'Content-type': 'application/json;charset=utf-8'}
# response = requests.get('https://www.baidu.com')
# # print(type(response))
# print(response)

print(test_dict)
print(type(test_dict))

print(test_dict2)
print(test_dict2['fxid'])