'''
 -*- coding: utf-8 -*-
 @Time : 18-11-14 下午7:11
 @Author : SamSa
 @Site : 
 @File : accountApi.py
 @Software: PyCharm
 @Statement:邮箱激活验证
'''

from flask_restful import Resource, reqparse

from App.ext import cache
from App.modles import db
from App.modles.userModel import User

parser = reqparse.RequestParser()

# parser.add_argument('u_name',type=str,required=True,help='Please input username！')
parser.add_argument('token',type=str,required=True,help='激活失败')
'''邮箱激活验证'''


class AccountResource(Resource):
    def get(self):
        # 获取由uuid生成的唯一值token
        info = parser.parse_args()
        token = info.get('token')
        uuid = cache.get(token)

        # 根据token查询数据库  如果查得到说明未过期，进行修改active的状态值
        users = User.query.filter_by(token=uuid)
        if users.count() > 0:
            user = users.first()

            if user:
                try:
                    user.active = 1
                    db.session.add(user)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return {
                        'msg':'Failed to active!'
                    }
                return {
                    'msg':'Success to active!'
                }

        # 如果上面的缓存过期,则查不到,此时通过浏览器的请求返回token来赋值给uuid进行查询
        else:
            user = User.query.filter(User.token == token).first()
            db.session.delete(user)
            db.session.commit()
            return '邮件过期'


