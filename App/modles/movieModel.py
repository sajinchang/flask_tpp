'''
 -*- coding: utf-8 -*-
 @Time : 18-11-15 上午11:44
 @Author : SamSa
 @Site : 
 @File : movieModel.py
 @Software: PyCharm
 @Statement:插入电影模型
'''

from App.modles import db
from App.modles.ModelUtil import Settings


class Movies(db.Model,Settings):
    id = db.Column(db.Integer,primary_key=True,autoincrement=False)
    showname = db.Column(db.String(128))
    shownameen = db.Column(db.String(128))
    director = db.Column(db.String(64))
    leadingRole = db.Column(db.String(256))
    type = db.Column(db.String(64))
    country = db.Column(db.String(64))
    language = db.Column(db.String(64))
    duration = db.Column(db.Integer)
    screeningmodel = db.Column(db.String(32))
    openday = db.Column(db.Date)
    backgroundpicture = db.Column(db.String(64))
    flag = db.Column(db.Integer)
    isdelete = db.Column(db.Boolean)