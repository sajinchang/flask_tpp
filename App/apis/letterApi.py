'''
 -*- coding: utf-8 -*-
 @Time : 18-11-14 上午11:54
 @Author : SamSa
 @Site :
 @File : letterApi.py
 @Software: PyCharm
 @Statement:查询所有的城市
'''


from flask_restful import Resource, marshal_with, fields

from App.modles.letter_citiesModel import Letter, Cities

city_fields = {
    'id':fields.Integer,
    'parents':fields.Integer,
    'regionName':fields.String,
    'cityCode':fields.Integer,
    'pinYin':fields.String

}

value_fields = {
    'A': fields.List(fields.Nested(city_fields)),
    'B': fields.List(fields.Nested(city_fields)),
    'C': fields.List(fields.Nested(city_fields)),
    'D': fields.List(fields.Nested(city_fields)),
    'E': fields.List(fields.Nested(city_fields)),
    'F': fields.List(fields.Nested(city_fields)),
    'G': fields.List(fields.Nested(city_fields)),
    'H': fields.List(fields.Nested(city_fields)),
    'J': fields.List(fields.Nested(city_fields)),
    'K': fields.List(fields.Nested(city_fields)),
    'L': fields.List(fields.Nested(city_fields)),
    'M': fields.List(fields.Nested(city_fields)),
    'N': fields.List(fields.Nested(city_fields)),
    'P': fields.List(fields.Nested(city_fields)),
    'Q': fields.List(fields.Nested(city_fields)),
    'R': fields.List(fields.Nested(city_fields)),
    'S': fields.List(fields.Nested(city_fields)),
    'T': fields.List(fields.Nested(city_fields)),
    'W': fields.List(fields.Nested(city_fields)),
    'X': fields.List(fields.Nested(city_fields)),
    'Y': fields.List(fields.Nested(city_fields)),
    'Z': fields.List(fields.Nested(city_fields)),
}

res_fields = {
    'returnCode':fields.Integer,
    'returnValue':fields.Nested(value_fields)
}
class SearchAllCitiesResource(Resource):
    @marshal_with(res_fields)
    def get(self):
        returnValue = {}
        letters = Letter.query.all()
        for letter in letters:
            cities = Cities.query.filter_by(letter_id = letter.id)
            returnValue[letter.letter] = cities
        data = {
            'returnCode':"0",
            'returnValue':returnValue
        }
        return data