'''
 -*- coding: utf-8 -*-
 @Time : 18-11-15 下午7:18
 @Author : SamSa
 @Site : 
 @File : cinemaApi.py
 @Software: PyCharm
 @Statement:根据关键字查询所有电影院    支持模糊查询
'''
from flask import request
from flask_restful import Resource, marshal_with, fields

from App.modles.cinemaModel import Cinemas

cinema_field = {
    'name':fields.String,
    'city':fields.String
}


class CinemaResource(Resource):
    resultField = {
        'msg':fields.String,
        'returnValue':fields.List(fields.Nested(cinema_field))
    }

    @marshal_with(resultField)
    def get(self):
        name = request.args.get('name')
        if name == None:
            cinemas = Cinemas.query.all()
            return {
                'msg':'ok',
                'returnValue':cinemas
            }
        else:
            cinemas = Cinemas.query.filter(Cinemas.name.contains(name))
            return {
                'msg':'ok',
                'returnValue':cinemas
            }

