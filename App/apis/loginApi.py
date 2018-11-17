'''
 -*- coding: utf-8 -*-
 @Time : 18-11-14 下午7:58
 @Author : SamSa
 @Site : 
 @File : loginApi.py
 @Software: PyCharm
 @Statement:登陆
'''
from flask import g

'''登陆'''

from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash

from App.modles.userModel import User

parser = reqparse.RequestParser()
parser.add_argument('username',type=str,required=True,help='请输入用户名')
parser.add_argument('passwd',type=str,required=True,help='请输入密码')


class LoginResource(Resource):

    def post(self):
        info = parser.parse_args()
        username = info.get('username')
        passwd = info.get('passwd')
        users = User.query.filter_by(u_name = username)
        if users.count() > 0:
            g.user = users.first()

            # g.usr = user
            if check_password_hash(g.user.u_passwd,passwd):
                if g.user.active.__eq__(True):
                    return '登陆成功'
                return '账户被锁定，尚未激活'
            return '密码错误'
        return '用户不存在，请先注册在登陆'



