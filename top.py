# -*- coding: utf-8 -*-
import requests

def setTop(url,comment,user) :

    data = [
        ('ck', 'YTbU'),
        ('rv_comment',
         comment),
        ('start', '0'),
        ('submit_btn', '加上去'),
    ]

    res = user.session.post( url +'/add_comment#last', data=data)
    print res.content;