'''
 -*- coding: utf-8 -*-
 @Time : 18-11-15 上午11:39
 @Author : SamSa
 @Site : 
 @File : ModelUtil.py
 @Software: PyCharm
 @Statement:工具类
'''
from App.modles import db


class Settings:
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            return {
                'msg':'Insert failed!',
                'returnCode':402

            }
        return 'Insert successful!'