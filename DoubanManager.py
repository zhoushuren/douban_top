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

        mat = re.search('src=\"(.*?captcha.*?)\"', rval.text)
        if mat:
            #需要识别验证码
            print '开始识别验证码...'
            captcha_url = mat.group(1)
            import identify_code
            try:
                code = identify_code.recognize_url(captcha_url)#识别验证码
                print '识别到的验证码为:'+str(code)
            except:
                print '没有识别到,3秒后重新识别'
                time.sleep(3);
                return self.setTop(url,comment, user)
            data['captcha-solution'] = code
            data['captcha-id'] = re.search('id=(.*?)&', captcha_url).group(1)

        ##寻找要提交的ck参数
        data['ck'] = re.search('ck=(\w+)', rval.text).group(1)

        print '这次发的帖子是：' +  url + 'add_comment'

        res = user.session.post(url + 'add_comment', data=data,headers=headers)
        if res.content != '':
            xpathStr = '//*[@id="content"]/div/div[1]/div[3]/form/div[2]/text()'
            codeErrorTree = html.fromstring(res.content)
            codeError = codeErrorTree.xpath(xpathStr)

            if len(codeError) > 0:
                print codeError[0]
                time.sleep(5);
                return self.setTop(url, comment, user)
            else:
                print '发帖成功!'
                time.sleep(5);
                return

    def startTop(self,comment):
        userLength  = len(self.users);
        print 'user number is ' + str(userLength)
        for user in self.users:
            urls = self.getMyTopicUrls(user)
            print urls;
            time.sleep(10);
            for url in urls:
                print '开始准备发帖子：' + url
                self.setTop(url,comment,user);