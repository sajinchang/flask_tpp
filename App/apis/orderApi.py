'''
 -*- coding: utf-8 -*-
 @Time : 18-11-17 上午11:46
 @Author : SamSa
 @Site : 
 @File : orderApi.py
 @Software: PyCharm
 @Statement:订单模块
'''
from datetime import datetime
from re import sub

from flask import request, g, session
from flask_restful import Resource

from App.modles.orderModel import Orders
# from manager import app


class OrderResource(Resource):
    def get(self):
        # user_id = g.userId
        # print(user_id)

        user_id = session.get('userId')
        print(user_id)
        movie_id = request.args.get('movie_id')
        seat = int(request.args.get('seat'))
        # print(seat,type(seat))
        # 获取当前的时间并格式化
        pay_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        order = Orders()
        order.user_id = user_id
        order.seat_num = seat


        order.movie_id = movie_id
        order.pay_time = str(pay_time)

        # order.pay_time = datetime.now() + datetime.__delattr__(minute=15)

        order.total_price = seat * 40

        # 拼接一个唯一的id
        order.id = str(user_id) + str(movie_id) + sub(r'[-|:| ]*','',pay_time)

        data = order.save()
        return data

    # @.before_request
    # def get_user(self):
    #     g.user = g.user