'''
 -*- coding: utf-8 -*-
 @Time : 18-11-13 下午5:18
 @Author : SamSa
 @Site : 
 @File : ext.py
 @Software: PyCharm
'''
from flask_bootstrap import Bootstrap
from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_migrate import Migrate
from flask_session import Session

from App.modles import db

mail = Mail()
cache = Cache(config={'CACHE_TYPE':'redis'})
def init_ext(app):
    migrate = Migrate()
    migrate.init_app(app=app,db=db)
    db.init_app(app=app)
    Session(app=app)

    debugtoolbar = DebugToolbarExtension()
    debugtoolbar.init_app(app=app)

    Bootstrap(app=app)

    cache.init_app(app=app)

    # 邮箱初始化
    mail.init_app(app=app)
