# ！/usr/bin/env python
# -*- coding:utf-8 -*-
# __Author__ Jianer

import requests, time, re, json
from bs4 import BeautifulSoup

TIME = None
QR_CODE = None
COOKIES = None
AUTH_DICT = {}


def get_url():
    """
    动态获取二维码
    :return: 
    """
    global TIME
    TIME = str(time.time())
    response = requests.get(
        url='https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={}'.format(
            TIME),
    )

    QRLogin_uuid = re.search('window.QRLogin.uuid = "(?P<uuid>\w+)==";', response.text)
    global QR_CODE
    QR_CODE = QRLogin_uuid.group('uuid')
    return QRLogin_uuid.group('uuid')


def scan_code():
    """
    实时监听用户扫码
    :return: 
    """
    login_url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}==&tip=1&r=140686053&_={1}'.format(
        QR_CODE, TIME
    )
    result = requests.get(login_url).text
    return result


def analysis_task(response):
    """
    解析返回值
    :param response: 
    :return: 
    """
    result = {'status': None, 'data': None}
    code_status = re.search('window\.code=(?P<code>\d+)', response)
    if code_status:
        code_status = code_status.group('code')
        if code_status == '408':
            result.update({'status': code_status})
        elif code_status == '201':
            userAvatar = re.search("window\.userAvatar = '(?P<data>.*)'", response)
            result.update({'status': code_status, 'data': userAvatar.group('data')})
        elif code_status == '200':
            redirect_url = re.search('window\.redirect_uri="(?P<data>.*)"', response).group('data')
            ret = requests.get(
                url=redirect_url + '&fun=new&version=v2&lang=zh_CN'
            )
            cookie = ret.cookies.get_dict()
            global COOKIES
            COOKIES = cookie
            soup = BeautifulSoup(ret.text, features="html.parser")
            for tag in soup.find('error').children:
                AUTH_DICT[tag.name] = tag.get_text()
            # 获取个人信息
            get_user_info = requests.post(
                url='https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=79901605&lang=zh_CN&pass_ticket={0}'.format(
                    AUTH_DICT['pass_ticket']
                    ),
                json={
                    'BaseRequest': {
                        'Uin': AUTH_DICT['wxuin'],
                        'Sid': AUTH_DICT['wxsid'],
                        'Skey': AUTH_DICT['skey'],
                        'DeviceID': 'e534613002685375'
                    }
                },
                # cookies=cookies
            )
            get_user_info.encoding = 'utf-8'
            user_info = json.loads(get_user_info.text)
            contact_url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket={}&r=1494572433224&seq=0&skey={}'
            # 获取所有联系人
            contact_list = requests.get(
                url=contact_url.format(AUTH_DICT['pass_ticket'], AUTH_DICT['skey']),
                cookies=cookie
            )
            contact_list.encoding = 'utf-8'
            user_contact_list = json.loads(contact_list.text)
            user = {'user_info': user_info, 'user_contact_list': user_contact_list}
            result.update({'status': code_status, 'data': user})
            # send_msg(cookie, user_info)
    return result


def send_msg(data):
    """
    发送消息
    :param data: 
    :return: 
    """
    send_msg_data = {
        'BaseRequest': {
            'Uin': AUTH_DICT['wxuin'],
            'Sid': AUTH_DICT['wxsid'],
            'Skey': AUTH_DICT['skey'],
            'DeviceID': 'e534613002685375'
        },
        'Msg': {
            'Type': 1,
            'Content': data.get('Content'),
            'FromUserName': data.get('FromUserName'),
            'ToUserName': data.get('ToUserName'),
            'Local': time.time(),
            'ClientMsgId': time.time()
        },
        'Scene': 0
    }
    send_msg_url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket={}'
    response = requests.post(
        url=send_msg_url.format(AUTH_DICT['pass_ticket']),
        data=json.dumps(send_msg_data, ensure_ascii=False).encode(encoding='utf-8'),
        # cookies=cookie
    )
    return response.text


def push_msg():
    """
    登陆成功之后发起长轮询 监听返回的消息
    :return: 
    """
    result = {'status': None, 'data': None}
    response = requests.get(
        url='https://webpush.wx.qq.com/cgi-bin/mmwebwx-bin/synccheck',
        params={
            'r': time.time(),
            'skey': AUTH_DICT['skey'],
            'sid': AUTH_DICT['wxsid'],
            'uin': AUTH_DICT['wxuin'],
            'deviceid': 'e534613002685375',
            'synckey': '1_658666240|2_658666276|3_658666277|11_658665222|13_658642505|201_1494775684|1000_1494754922|1001_1494754952|1004_1494344568',
            '_': time.time()
        },
        cookies=COOKIES
    )
    print(response.text)
    selector = re.findall('selector: "(\d+)"', response.text)
    if len(selector):
        result['status'] = selector[0]
    # window.synccheck = {retcode: "0", selector: "2"}
    return result