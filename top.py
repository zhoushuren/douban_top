# -*- coding: utf-8 -*-
import requests

def setTop(url,comment,cookie) :

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Host': 'www.douban.com',
        'Referer': 'https://www.douban.com/group/topic/108719221/?start=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = [
        ('ck', 'YTbU'),
        ('rv_comment',
         comment),
        ('start', '0'),
        ('submit_btn', '\u52A0\u4E0A\u53BB'),
    ]

    res = requests.post( url +'/add_comment#last', headers=headers, cookies=cookie,
                  data=data)
    print res;