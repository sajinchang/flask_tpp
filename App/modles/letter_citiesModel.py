'''
 -*- coding: utf-8 -*-
 @Time : 18-11-14 上午11:58
 @Author : SamSa
 @Site : 
 @File : letter_citiesModel.py
 @Software: PyCharm
'''

from App.modles import db


class Letter(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    letter = db.Column(db.String(2))


class Cities(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=False)
    parentId = db.Column(db.Integer,default=0)
    regionName = db.Column(db.String(32))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(32))
    letter_id = db.Column(db.Integer,db.ForeignKey(Letter.id))
