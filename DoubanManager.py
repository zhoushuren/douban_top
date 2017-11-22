# -*- coding: utf-8 -*-
import requests
from lxml import html
import time
import re


class DoubanManager():

    def  __init__(self):
        self.users = []

    def getMyTopicUrls(self,user):
        _res = user.session.get('https://www.douban.com/mine/', )
        urlArr= _res.url.split('/');
        prople_id = urlArr[4]
        res =  user.session.get('https://www.douban.com/group/people/'+ prople_id +'/publish')
        tree = html.fromstring(res.content)
        xpath = '//*[@id="content"]/div/div[1]/div[2]/table/tr/td[1]/a/@href';
        urlArr = tree.xpath(xpath)
        return urlArr

    def setUserList(self,user):
        self.users.append(user);

    def getUser(self,i):
        return self.users[i]

    def setTop(self,url,comment,user):
        data = {
            "rv_comment": comment,
            "ck": "aubV",
            'start': '0',
            'submit_btn': '加上去'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
            'Referer': 'https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001'
        }

        rval = user.session.get(url + '?start=5000#last', headers=headers)
        # 检验是否需要输入验证码?
        ##寻找要提交的ck参数
        data['ck'] = re.search('ck=(\w+)', rval.text).group(1)

        print url + 'add_comment'
        print data

        res = user.session.post(url + 'add_comment', data=data,headers=headers)
        print res
        time.sleep(120);

    def startTop(self,comment):
        userLength  = len(self.users);
        print 'user number is ' + str(userLength)
        for user in self.users:
            urls = self.getMyTopicUrls(user)
            print urls;
            time.sleep(20);
            for url in urls:
                self.setTop(url,comment,user);