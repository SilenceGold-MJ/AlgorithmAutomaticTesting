#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests,json
from framework.logger import Logger
logger = Logger(logger="API").getlog()

address,port='http://192.168.1.182','8408'

class API():
    def GetStart(self):
        url = "%s:%s/GetStart"%(address,port)
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        data = json.loads(response.text)
        return data

    def APIall(self,connect, dic):
        url = "%s:%s/%s"%(address,port,connect)
        payload = json.dumps(dic)
        logger.info( url )
        logger.info(payload)
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info(response.text)
        data = json.loads(response.text)
        logger.info(data)
        return data
