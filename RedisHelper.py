# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:00:00 2018

@author: dingfei
"""

import redis
 
class RedisHelper(object):
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1',port=6379)#连接Redis
        self.channel = 'monitor' #定义名称
 
    def publish(self,msg):#定义发布方法
        self.__conn.publish(self.channel,msg)
        return True
 
    def subscribe(self):#定义订阅方法
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub