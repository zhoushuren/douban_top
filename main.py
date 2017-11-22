# -*- coding: utf-8 -*-

from DoubanManager import DoubanManager

from User import User

def main():

    accounts = [
        {
            'email': '15618311747',
            'password' : '15618311747'
         },
        {
            'email' : '15821203908',
            'password' : '15821203908'
        },
        {
            'email': '13621913710',
            'password': 'guxiaobook520'
        }
    ]

    douban = DoubanManager();

    for account in accounts :
        user = User()
        user.doLogin(account.get('email'),account.get('password'));

        douban.setUserList(user);

    while True:
        douban.startTop('非常好，赞');

if __name__ == '__main__':
    main()