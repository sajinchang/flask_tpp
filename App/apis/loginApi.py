'''
 -*- coding: utf-8 -*-
 @Time : 18-11-14 下午7:58
 @Author : SamSa
 @Site : 
 @File : loginApi.py
 @Software: PyCharm
 @Statement:登陆
'''
# from datetime import datetime
# from re import sub

from flask import session

# from App.modles.orderModel import Orders

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
            user = users.first()

            session['userId'] = user.u_id
            # g.userId = user.u_id
            # print(g.userId)
            if check_password_hash(user.u_passwd,passwd):
                if user.active.__eq__(True):
                    return '登陆成功'
                return '账户被锁定，尚未激活'
            return '密码错误'
        return '用户不存在，请先注册再登陆'



