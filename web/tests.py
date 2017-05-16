from django.test import TestCase
from bs4 import BeautifulSoup


import requests, time, re, os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# response = requests.get(
#     url='https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={}'.format(
#         int(time.time())),
# )
#
# QRLogin_uuid = re.search('window.QRLogin.uuid = "(?P<uuid>\w+)==";', response.text).group('uuid')
# print(QRLogin_uuid)
# url = 'https://login.weixin.qq.com/qrcode/{uuid}=='.format(uuid=QRLogin_uuid)
# QR_code_img = requests.get(
#     url=url
# )
#
# with open(os.path.join(BASE_DIR, 'static/img', '{}.jpg'.format(QRLogin_uuid)), 'wb') as f:
#     f.write(QR_code_img.content)
#
# while True:
#     print('正在连接中...')
#     time.sleep(3)
#     response = requests.get(
#         url='https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}==&tip=1&r=140686053&_={1}'.format(
#             QRLogin_uuid, int(time.time())),
#     )
#     print('等待中...')
#     print(response.text)
# html = '<error><ret>0</ret><message></message><skey>@crypt_1b093f5f_84ae03f818b65ead1dceba0c23f3a952</skey><wxsid>pJ4EDsE8eeyjnvM/</wxsid><wxuin>1207706561</wxuin><pass_ticket>BXN9cjQQTPOyvioxyuZEgTbikLice2bTO9IBg1vmDVq8qG5GDMU3jJ9ThG6Z0b0p</pass_ticket><isgrayscale>1</isgrayscale></error>'
#
# soup = BeautifulSoup(html, features="html.parser")
#
# for item in soup.find('error').children:
#     print(item.name, item.get_text())


# ret = requests.post(
#     url='https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=79901605&lang=zh_CN&pass_ticket=BXN9cjQQTPOyvioxyuZEgTbikLice2bTO9IBg1vmDVq8qG5GDMU3jJ9ThG6Z0b0p'
# )
#
# print(ret.text)

















