'''
 -*- coding: utf-8 -*-
 @Time : 18-11-17 上午10:15
 @Author : SamSa
 @Site : 
 @File : payApi.py
 @Software: PyCharm
 @Statement:支付,调用支付宝接口
'''
from alipay import AliPay
from flask import request
from flask_restful import Resource

from App.settings import ALIPAY_APPID, APP_PRIVATE_KEY, APP_PUBLIC_KEY


class PayResource(Resource):
    def get(self):
        order_id = request.args.get('order_id')

        # 构建支付
        alipay_client = AliPay(
            appid = ALIPAY_APPID,
            # 默认回调
            app_notify_url=None,
            app_private_key_string=APP_PRIVATE_KEY,
            alipay_public_key_string= APP_PUBLIC_KEY,

            sign_type='RSA',
            debug=False
        )

        subject = 'I20 系列 30核 '

        # 电脑网站支付,跳转:https://openapi.alipay.com/gateway.do? + order_string
        order_string = alipay_client.api_alipay_trade_app_pay(
            out_trade_no ='1100000',
            total_amount ='10000',
            subject = subject,
            return_url = 'https://github.com/sajinchang',
            notify_url = 'https://github.com/sajinchang'    #可选

        )

        # 手机网站支付
        # order_string = alipay_client.api_alipay_trade_wap_pay(
        #     out_trade_no = '1100000',
        #     total_amount = '10000',
        #     subject = subject,
        #     return_url = 'https://github.com/sajinchang',
        #     notify_url = 'https://github.com/sajincahng'
        #
        # )

        # 客户端支付
        pay_url = "https://openapi.alipaydev.com/gateway.do?" + order_string

        data = {
            'msg':'ok',
            'status':200,
            'data':{
                'pay_url':pay_url,
                'order_id':order_id
            }
        }
        return data
