'''
 -*- coding: utf-8 -*-
 @Time : 18-11-13 下午5:04
 @Author : SamSa
 @Site : 
 @File : __init__.py.py
 @Software: PyCharm
 @Statement:初始化app
'''
from flask import Flask

from App import settings
from App.apis import init_api
from App.ext import init_ext
# from App.modles.letter_cities import Letter, Cities
# from App.modles.userModel import User
# from App.modles.cinemaModel import Cinemas
# from App.modles.movieModel import Movies
# from App.modles.orderModel import Orders


def create_app(ENV_NAME):
    app = Flask(__name__)
    app.config.from_object(settings.ENV_NAME.get(ENV_NAME))
    # 使用session如报错添加以下配置
    app.config['SESSION_TYPE'] = 'redis'
    # 解决浏览器响应为乱码情况
    app.config.update(RESTFUL_JSON=dict(ensure_ascii = False))

    init_ext(app)
    init_api(app)
    # user = User()
    # letter = Letter()
    # cities = Cities()
    # moive = Movies()
    # cinema = Cinemas()
    # order = Orders()
    return app