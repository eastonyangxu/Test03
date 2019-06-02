# encoding=utf-8
import hashlib
import json
from collections import OrderedDict

import requests

APP_CONF = {
    '1069573': {
        'API_KEY': 'umSgDOaYxg5ckWk7jrtZ5IKOqu35VWpQ',
        'gateway': 'http://api.meowspay.com/index/unifiedorder',
        'query_gateway': 'http://api.meowspay.com/index/unifiedorder?format=json',
    }
}


def _get_api_key(mch_id):
    return APP_CONF[mch_id]['API_KEY']


def _get_gateway(mch_id):
    return APP_CONF[mch_id]['gateway']


def _get_query_gateway(mch_id):
    return APP_CONF[mch_id]['query_gateway']


def generate_sign(parameter, key):
    m = hashlib.md5()
    for k, v in parameter.items():
        if v == '':
            parameter.pop(k)
    par = sorted(parameter.items())
    print(par)
    param = ''
    for k, v in par:
        param += k + '=' + v + '&'
    par_key = param + 'key=' + key
    print(par_key)
    m.update(par_key.encode('utf-8'))
    sign = m.hexdigest().upper()
    print(sign)
    return sign


def create_charge(info):
    app_id = info['app_id']
    api_key = _get_api_key(app_id)

    paramter_dict = OrderedDict((
        ('appid', str(app_id)),
        ('pay_type', 'alipay'),
        ('amount', '100.00'),
        ('callback_url', 'http://baidu.com'),
        ('success_url', 'http://baidu.com'),
        ('error_url', 'http://baidu.com'),
        ('out_uid', '1234'),
        ('out_trade_no', '12592258235321'),
        ('version', 'v1.1'),
    ))
    paramter_dict['sign'] = generate_sign(paramter_dict, api_key)
    print(paramter_dict)
    print('-' * 20)
    r = requests.post(_get_gateway(app_id), json=paramter_dict, timeout=3)
    text = r.text
    print(text)
    print(r)
    print(r.headers)


def t():
    info = {'app_id': '1069573'}
    create_charge(info)


t()
