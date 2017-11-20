# -*- coding: utf-8 -*-
import requests
from lxml import html
import urllib
from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)


class User():

    def  __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
            'Host': 'accounts.douban.com',
            'Referer': 'https://accounts.douban.com/login?source=group',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.session = requests.Session()
        # self.session.headers.update(headers)

        self.url = "https://www.douban.com/accounts/login"

    def getHeader(self):
        return self.header

    def getCookie(self):
        return self.cookie

    def getCookies(self,i):
        return getCookies(i);


    def doLogin(self,username,password):
        cookies = {
            'bid': 'vq6Yeh-gYSY',
            '__utma': '30149280.1384347154.1511076321.1511076321.1511078922.2',
            '__utmc': '30149280',
            '__utmz': '30149280.1511076321.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
            'push_noty_num': '0',
            'push_doumail_num': '0',
            '__utmv': '30149280.15544',
            'ct': 'y',
            '__utmb': '30149280.10.7.1511079546982',
            '__utmt': '1',
            'ap': '1',
            'as': 'https://www.douban.com/group/topic/108719300/?start=0&post=ok',
            'ps': 'y',
        }

        r = requests.get(self.url)
        tree = html.fromstring(r.content)
        captcha = tree.xpath('//*[@id="captcha_image"]/@src')  # 获取验证码图片的链接
        captcha_id = tree.xpath('//*[@id="captcha_field"]/../input[2]/@value')  # 获取验证码id
        print captcha
        print captcha_id

        data = [
            ('source', 'group'),
            ('redir', 'https://www.douban.com/group/topic/108719300/?start=0&post=ok'),
            ('form_email', username),
            ('form_password', password),
            ('login', '\u767B\u5F55'),
        ]

        if(len(captcha) > 0):
            print captcha[0]
            # urllib.urlretrieve(captcha[0],filename="./captcha.png")
            ir = requests.get( captcha[0])
            sz = open('cccccccc.jpg', 'wb').write(ir.content)
            captcha_value = raw_input('查看captcha.png,有验证码请输入:')
            solution = ('captcha-solution',captcha_value)
            captchaID = ('captcha-id',captcha_id)
            data.append(solution)
            data.append(captchaID)

        res = requests.post('https://accounts.douban.com/login', headers=self.headers,data=data)





        print res
        print res.status_code;
        #
        # if res.status_code == 200:
        #     print 'login success cookies is :'
        #     print res.cookies
        #
        #     print {c.name: c.value for c in res.cookies}
        #     self.cookie = res.cookies;
        # else:
        #     print 'login error'



#test
#
# u = User();
#
# u.doLogin('15618311747','15618311747')