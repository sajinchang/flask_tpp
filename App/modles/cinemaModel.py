'''
 -*- coding: utf-8 -*-
 @Time : 18-11-15 上午11:55
 @Author : SamSa
 @Site : 
 @File : cinemaModel.py
 @Software: PyCharm
 @Statement:插入影院信息
'''

from App.modles import db
from App.modles.ModelUtil import Settings


class Cinemas(db.Model,Settings):

    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(64))
    city = db.Column(db.String(32))
    district = db.Column(db.String(32))
    address = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    score = db.Column(db.Float)
    hallnum = db.Column(db.Integer)
    servicecharge = db.Column(db.Float)
    astrict = db.Column(db.Integer)
    flag = db.Column(db.Integer)
    isdelete = db.Column(db.Boolean)