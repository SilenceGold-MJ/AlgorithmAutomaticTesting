#!/user/bin/env python3
# -*- coding: utf-8 -*-
from framework.API import API
from framework.Fanchart import Fanchar
import base64,os
# # print(API().GetStart())
# dic={'Test_Version': 'v1.0_201912181512', 'Test_Batch': '20200619_1'}
# connect='GetSummaryData'
# data = API().APIall(connect, dic)
# print(data)
import json
from framework.logger import Logger
logger = Logger(logger="views").getlog()
from framework.ScatteRender import ScatterRender
def tets():
    import requests

    url = "http://192.168.1.182:8408/DownloadExcle"

    payload ={
    "filename": 'wwcese.xlsx',
    "Test_Version":'v1.0_201812181345' ,
    "Test_Batch":'20200619_1'}
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    return (json.loads(response.text))

dtat=tets()['datalist']

# 获取图片base64字节流
filebase64 = dtat['filebase64']
# 获取图片名称
filename = dtat['filename']
save_path = os.getcwd()+"\\static\\file\\"+filename
with open(save_path, 'wb') as f:
    f.write(base64.b64decode(filebase64))

