'''
 -*- coding: utf-8 -*-
 @Time : 18-11-15 下午7:40
 @Author : SamSa
 @Site : 
 @File : movieAdd.py
 @Software: PyCharm
 @Statement:添加电影    查询所有flag为1的电影
'''
from flask import request
from flask_restful import Resource, reqparse, marshal_with, fields

from App.modles.movieModel import Movies

parser = reqparse.RequestParser()

parser.add_argument('id',type=str,required=True,help='id')
parser.add_argument('showname',type=str,required=True,help='showname')
parser.add_argument('shownameen',type=str,help='shownameen')
parser.add_argument('director',type=str,help='director')
parser.add_argument('leadingRole',type=str,help='leadingRole')
parser.add_argument('type',type=str,help='type')
parser.add_argument('country',type=str,help='country')
parser.add_argument('language',type=str,help='language')
parser.add_argument('duration',type=int,help='duration')
parser.add_argument('screeningmodel',type=str,help='screeningmodel')
parser.add_argument('openday',type=str,help='openday')
parser.add_argument('backgroundpicture',type=str,help='backgroundpicture')
parser.add_argument('flag',type=int,help='flag')
parser.add_argument('isdelete',type=int,help='isdelete')


class MovieAddResource(Resource):

    def post(self):
        parse = parser.parse_args()
        id = parse.get('id')
        showname = parse.get('showname')

        movie = Movies()
        movie.id = id
        movie.showname = showname

        data = movie.save()
        return data

    field_movie = {
        'id':fields.String,
        'showname':fields.String
    }
    field_movies = {
        'msg':fields.String,
        'returnValue':fields.List(fields.Nested(field_movie))
    }

    @marshal_with(field_movies)
    def get(self):
        flag = request.args.get('flag')

        '''
        在使用filter以及filter_by查询的时候,若想使用marshal_with
        格式化输出时,必须使用List类型进行嵌套,如果是query.all()查询
        所有时,既可以使用List也可以使用Nested.
        
        request请求的是数值类型时,可以不进行int强转即可直接查询
        '''
        movies = Movies.query.filter(Movies.flag == flag)
        # print(movies)
        data = {
            'msg':'ok',
            'returnValue':movies
        }
        return data
