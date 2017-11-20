import requests
from cookie import getCookies
class User():

    def  __init__(self):
        self.cookie = '';
        self.ssrequest = requests.session()

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

        headers = {
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

        data = [
            ('source', 'group'),
            ('redir', 'https://www.douban.com/group/topic/108719300/?start=0&post=ok'),
            ('form_email', username),
            ('form_password', password),
            ('login', '\u767B\u5F55'),
        ]


        res = requests.post('https://accounts.douban.com/login', headers=headers, cookies=cookies, data=data)
        print res
        print res.status_code;

        if res.status_code == 200:
            print 'login success cookies is :'
            print res.cookies

            print {c.name: c.value for c in res.cookies}
            self.cookie = res.cookies;
        else:
            print 'login error'



#test
#
# u = User();
#
# u.doLogin('15618311747','15618311747')