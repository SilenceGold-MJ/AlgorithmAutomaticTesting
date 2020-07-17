#!/user/bin/env python3
# -*- coding: utf-8 -*-
from framework.API import API
from framework.Fanchart import Fanchar

# # print(API().GetStart())
# dic={'Test_Version': 'v1.0_201912181512', 'Test_Batch': '20200619_1'}
# connect='GetSummaryData'
# data = API().APIall(connect, dic)
# print(data)
import json
from framework.ScatteRender import ScatterRender
def tets():
    import requests

    url = "http://192.168.1.182:8408/Linechart"

    payload = "{\r\n    \"test_version\":\"v1.0_201912181512\",\r\n    \"test_batch\":\"20200619_1\"\r\n}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return (json.loads(response.text))
dic_zql=tets()['datalist']
htmlname='zhexiantu_zql.html'
print(ScatterRender().scatter_render(dic_zql,htmlname))
