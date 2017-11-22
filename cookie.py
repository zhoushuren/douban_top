# -*- coding: utf-8 -*-
import requests
from lxml import html


cookies = {
    'bid': 'vq6Yeh-gYSY',
    '__utma': '30149280.1384347154.1511076321.1511078922.1511168445.3',
    '__utmc': '30149280',
    '__utmz': '30149280.1511076321.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'push_noty_num': '0',
    'push_doumail_num': '0',
    '__utmv': '30149280.15544',
    'ct': 'y',
    'ap': '1',
    'ps': 'y',
    'dbcl2': '155449325:Rn0WN4YjD2A',
    'ck': 'FSw1',
    'll': '108296',
    '__utmb': '30149280.1.10.1511168445',
    '__utmt': '1',
    'as': 'https://www.douban.com/',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Host': 'accounts.douban.com',
    'Referer': 'https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = [
  ('source', 'index_nav'),
  ('redir', 'https://www.douban.com/'),
  ('form_email', '15618311747'),
  ('form_password', '15618311747'),
  ('captcha-solution', 'chalk'),
  ('captcha-id', '3ctqGduQpFjHDF2vN5fAWKuy:en'),
  ('login', '\u767B\u5F55'),
]

res = requests.post('https://accounts.douban.com/login', headers=headers, cookies=cookies, data=data)
print res.content;

if res.status_code == 200:
    tow_tree = html.fromstring(res.content)
    tow_captcha = tow_tree.xpath('//*[@id="captcha_image"]/@src')  # 获取验证码图片的链接
    tow_captcha_id = tow_tree.xpath('//*[@id="captcha_field"]/../input[2]/@value')  # 获取验证码id
    print tow_captcha
    print tow_captcha_id
    tow_data = [
        ('source', 'index_nav'),
        ('redir', 'https://www.douban.com/group/topic/108719300/?start=0&post=ok'),
        ('form_email', '15618311747'),
        ('form_password', '15618311747'),
        ('login', '\u767B\u5F55'),
    ]
    ir = requests.get(tow_captcha[0])
    sz = open('aaaaaa.jpg', 'wb').write(ir.content)
    captcha_value = raw_input('查看captcha.png,有验证码请输入:')

    print '输入了' + captcha_value;

    t_solution = ('captcha-solution', captcha_value)
    t_captchaID = ('captcha-id', tow_captcha_id[0])
    tow_data.append(t_solution)
    tow_data.append(t_captchaID)
    print '请求参数'
    print tow_data;
    res = requests.post('https://accounts.douban.com/login', cookies=cookies, headers=headers, data=tow_data)
    print 'tow--------------------------'

    print res

