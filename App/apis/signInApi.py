'''
 -*- coding: utf-8 -*-
 @Time : 18-11-14 下午5:18
 @Author : SamSa
 @Site :
 @File : signInApi.py
 @Software: PyCharm
 @Statement:注册 发送激活邮件
'''
'''注册并发送激活邮件'''


from uuid import uuid4

from flask import render_template
from flask_mail import Message
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash

from App.ext import cache, mail
from App.modles import db
from App.modles.userModel import User

'''利用parser获取数据'''
parser = reqparse.RequestParser()
parser.add_argument('u_name',type=str,required=True,help='Please input username！')
parser.add_argument(name='u_passwd',type=str,required=True,help='Please input password!')
parser.add_argument('email',type=str,required=True,help='Please inpit emial!')


class SignResource(Resource):

    def post(self):
        info = parser.parse_args()
        name = info.get('u_name')
        passwd = info.get('u_passwd')
        passwd = generate_password_hash(passwd)
        email = info.get('email')

        # 创建User对象，进行数据库插入
        user = User()
        user.u_name = name
        user.u_passwd = passwd
        user.email = email

        # uuid返回的不是str类型，需要强转
        token = str(uuid4())
        user.token = token

        # 插入数据库
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            return {
                'msg':'注册失败',
                'statuCode':400
            }

        # token放入缓存，进行邮箱激活过期使用
        cache.set(token,token,timeout=30)

        '''邮箱验证'''
        message = Message(subject='邮箱验证',sender='sajinde@163.com',recipients=[email])
        url = 'http://127.0.0.1:5000/account/?token='+token
        content = render_template('sign.html',name=name,url=url)
        message.html = content
        mail.send(message)

        return {
            'msg':'添加成功',
            'statuCode':200
        }




