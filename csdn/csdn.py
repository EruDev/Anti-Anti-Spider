# coding: utf-8

import requests
from requests.exceptions import RequestException
from lxml import html


class CSDN:

    def __init__(self):
        self.s = requests.session()
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7',
            'Host': 'passport.csdn.net',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        self.base_url = 'https://passport.csdn.net/'
        self.login_url = 'https://passport.csdn.net/account/verify'

    def get_params(self):
        try:
            resp = self.s.get(self.base_url, headers=self.headers)
            if resp.status_code == 200:
                el = html.fromstring(resp.text)
                lt = el.xpath('//input[@name="lt"]/@value')[0]
                execution = el.xpath('//input[@name="execution"]/@value')[0]
                eventId = el.xpath('//input[@name="_eventId"]/@value')[0]

                return lt, execution, eventId
        except RequestException:
            pass

    def login(self, username, password, *args):
        payload = {
            'username': username,
            'password': password,
            'rememberMe': True,
            'lt': args[0],
            'execution': args[1],
            '_eventId': args[2]
        }
        resp = self.s.get(self.login_url, headers=self.headers, params=payload)
        return resp

    def main(self):
        lt, executin, eventId = self.get_params()
        username = input('请输入你的账号:')
        password = input('请输入你的密码:')
        resp = self.login(username, password, lt, executin, eventId)
        print(resp.text)
        print(resp.cookies.get_dict())


if __name__ == '__main__':
    csdn = CSDN()
    csdn.main()

