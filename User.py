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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
    'Referer':'https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        self.url = "https://accounts.douban.com/login"

    def getHeader(self):
        return self.header

    def getCookie(self):
        return self.cookie

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

        r =  self.session.get(self.url)

        if r.status_code == 403:
            print '登录太频繁，稍后再试试或者换IP地址试试'
            exit()

        tree = html.fromstring(r.content)
        captcha = tree.xpath('//*[@id="captcha_image"]/@src')  # 获取验证码图片的链接
        captcha_id = tree.xpath('//*[@id="captcha_field"]/../input[2]/@value')  # 获取验证码id
        print captcha
        print captcha_id

        data = [
            ('source', 'group'),
            ('redir', 'https://www.douban.com'),
            ('form_email', username),
            ('form_password', password),
            ('login', '登陆'),
        ]

        if(len(captcha) > 0):
            print captcha[0]
            # urllib.urlretrieve(captcha[0],filename="./captcha.png")
            ir =  self.session.get( captcha[0])
            sz = open('cccccccc.jpg', 'wb').write(ir.content)
            captcha_value = raw_input('cccccccc.jpg,有验证码请输入:')
            solution = ('captcha-solution',captcha_value)
            captchaID = ('captcha-id',captcha_id[0])
            data.append(solution)
            data.append(captchaID)

        res = self.session.post('https://accounts.douban.com/login', data=data)
        print res


        # tree = html.fromstring(_res.content)
        # xpath = '//*[@id="content"]/div/div[1]/div[2]/table/tr/td[1]/a/@href';
        # urlArr = _tree.xpath(xpath)
        # print urlArr
        # 重复登录
        if res.status_code == 200 :
            tow_tree = html.fromstring(r.content)
            tow_captcha = tow_tree.xpath('//*[@id="captcha_image"]/@src')  # 获取验证码图片的链接
            tow_captcha_id = tow_tree.xpath('//*[@id="captcha_field"]/../input[2]/@value')  # 获取验证码id
            print tow_captcha
            print tow_captcha_id
            tow_data = [
                ('source', 'group'),
                ('redir', 'https://www.douban.com'),
                ('form_email', username),
                ('form_password', password),
                ('login', '登陆'),
            ]
            ir = requests.get(tow_captcha[0])
            sz = open('cccccccc.jpg', 'wb').write(ir.content)
            captcha_value = raw_input('查看captcha.png,有验证码请输入:')
            t_solution = ('captcha-solution', captcha_value)
            t_captchaID = ('captcha-id', tow_captcha[0])
            tow_data.append(t_solution)
            tow_data.append(t_captchaID)
            res = requests.post('https://accounts.douban.com/login', cookies=cookies, headers=self.headers, data=tow_data)
        #     print 'tow--------------------------'
        #
        #     print res
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