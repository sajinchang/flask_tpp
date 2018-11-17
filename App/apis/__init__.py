'''
 -*- coding: utf-8 -*-
 @Time : 18-11-13 下午5:09
 @Author : SamSa
 @Site : 
 @File : apis.py
 @Software: PyCharm
'''
from flask_restful import Api

from App.apis.accountApi import AccountResource
from App.apis.cinemaApi import CinemaResource
from App.apis.letterApi import SearchAllCitiesResource
from App.apis.loginApi import LoginResource
from App.apis.movieAdd import MovieAddResource
from App.apis.orderApi import OrderResource
from App.apis.payApi import PayResource
from App.apis.permissionContorl import PermissionResource
from App.apis.signInApi import SignResource

api = Api()

def init_api(app):
    api.init_app(app=app)


api.add_resource(SearchAllCitiesResource,'/cities/')
api.add_resource(SignResource,'/signin/')
api.add_resource(AccountResource,'/account/')
api.add_resource(LoginResource,'/login/')
api.add_resource(CinemaResource,'/cinema/')
api.add_resource(MovieAddResource,'/addmovie/')
api.add_resource(PermissionResource,'/check/')
api.add_resource(PayResource,'/pay/')
api.add_resource(OrderResource,'/order/')