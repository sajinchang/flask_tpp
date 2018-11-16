'''
 -*- coding: utf-8 -*-
 @Time : 18-11-14 下午4:42
 @Author : SamSa
 @Site : 
 @File : userModel.py
 @Software: PyCharm
'''
from App.modles import db


class User(db.Model):
    u_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    u_name = db.Column(db.String(32),unique=True)
    u_passwd = db.Column(db.String(256),nullable=False)
    active = db.Column(db.Boolean,default=0)
    # 权限
    permission = db.Column(db.Integer)
    token = db.Column(db.String(128),unique=True)
    email = db.Column(db.String(64))