
import requests
from lxml import html
import time
from top import setTop


class DoubanManager():

    def  __init__(self):
        self.users = []

    def getMyTopicUrls(self,cookies):
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'https://www.douban.com/group/people/155449325/likes',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
        }

        # print cookies


        res = requests.get('https://www.douban.com/group/people/155449325/publish', headers=headers, cookies=cookies)
        tree = html.fromstring(res.content)
        xpath = '//*[@id="content"]/div/div[1]/div[2]/table/tr/td[1]/a/@href';
        urlArr = tree.xpath(xpath)

        return urlArr

    def setUserList(self,user):
        self.users.append(user);

    def getUser(self,i):
        return self.users[i]

    def setTop(self,url,comment,cookie):
        setTop(url, comment,cookie)
        time.sleep(25);

    def startTop(self,comment):
        userLength  = len(self.users);
        print 'user number is ' + str(userLength)
        for user in self.users:
            urls = self.getMyTopicUrls(user.cookie)
            print urls;
            time.sleep(10);
            for url in urls:
                self.setTop(url,comment,user.cookie);