# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:11:09 2018

@author: dingfei
"""

import redis
#r = redis.Redis(host='127.0.0.1',port=6379,db=0)
from RedisHelper import RedisHelper
obj=RedisHelper()
#obj.publish('hello')
re_sub=obj.subscribe()
while True:
    msg=re_sub.parse_response()
    print(msg)