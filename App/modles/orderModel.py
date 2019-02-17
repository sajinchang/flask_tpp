'''
 -*- coding: utf-8 -*-
 @Time : 18-11-17 上午11:06
 @Author : SamSa
 @Site : 
 @File : orderModel.py
 @Software: PyCharm
 @Statement:订单表
'''
from App.modles import db
from App.modles.ModelUtil import Settings
from App.modles.movieModel import Movies
from App.modles.userModel import User


class Orders(db.Model,Settings):
    id = db.Column(db.String(128),primary_key=True,autoincrement=False)
    total_price = db.Column(db.Float)
    user_id = db.Column(db.Integer,db.ForeignKey(User.u_id))
    movie_id = db.Column(db.Integer,db.ForeignKey(Movies.id))
    # order_time = db.Column(db.DateTime)
    pay_time = db.Column(db.DateTime)
    seat_num = db.Column(db.Integer)
