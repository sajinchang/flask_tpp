'''
 -*- coding: utf-8 -*-
 @Time : 18-11-15 下午8:29
 @Author : SamSa
 @Site : 
 @File : permissionContorl.py
 @Software: PyCharm
 @Statement:添加电影权限控制
'''

from flask_restful import Resource, reqparse, abort

# 获取token来查询权限
from App.modles.movieModel import Movies
from App.modles.userModel import User

get_parser = reqparse.RequestParser()
get_parser.add_argument('token',type=str)

# 复制get_parser对象,获取它的token,来进行添加电影
post_parser = get_parser.copy()
post_parser.add_argument('id',type=str,required=True,help='亲输入电影的id')
post_parser.add_argument('showname',type=str,required=True,help='请输入电影名字')



#普通用户
USER = 2
# VIP
SUPERUSER = 1
# 管理员
ROOT = 0


# 权限控制装饰器
def check_permission(permission):
    def check_permission_func(func):
        def check(*args,**kwargs):
            parse = post_parser.parse_args()
            token = parse.get('token')
            users = User.query.filter(User.token == token)
            if users.count() > 0:
                user = users.first()
                if user.permission.__eq__(permission):
                    print('你拥有管理员权限!可以添加电影!')
                    return func(*args,**kwargs)
                else:
                    # abort(401,message='请联系管理员添加电影')
                    return '无权限,请联系管理员'

            else:
                # abort(402,message='您尚未登陆,请先登陆!')
                return '尚未登陆'
        return check
    return check_permission_func

class PermissionResource(Resource):


    @check_permission(ROOT)
    def post(self):
        parse = post_parser.parse_args()
        id = parse.get('id')
        showname = parse.get('showname')
        movie = Movies()
        movie.id = id
        movie.showname = showname
        data = movie.save()
        return data
