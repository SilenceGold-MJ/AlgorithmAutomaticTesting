from django.shortcuts import render

# Create your views here.
import json
import os,time
import base64
from django.shortcuts import render, HttpResponse, redirect
from framework.API import API
from framework.Fanchart import Fanchar
from framework.ScatteRender import ScatterRender
from framework.getImage import Pathlsit
from framework.logger import Logger
logger = Logger(logger="views").getlog()

def SelectPage(request):
    if request.method == 'POST':
        if  "Test_Version" in request.POST and 'Test_Batch' in request.POST and "content" in request.POST :

            logger.info("SelectPage(request):%s"%request.POST)
            dic={
            'test_version': request.POST.get("Test_Version"),
            'test_batch' : request.POST.get("Test_Batch")
            }
            connect=request.POST.get("content")#'GetSummaryData'
            logger.info("SelectPage(request):%s"%dic)
            data = API().APIall(connect, dic)
            logger.info("SelectPage(request):%s"%'请求接口')
            logger.info("SelectPage(request):%s"%data)
            if data['counts']!=0:
                return render(request, 'tetshtml.html',{"dic":data})
            else:
                return HttpResponse("暂无数据，可能正在在测试数据中……")

        elif  "Test_Version" in request.POST and 'Test_Batch' in request.POST and 'Accuracy' in request.POST :

            logger.info("SelectPage(request):%s"%request.POST)
            dic={
            'test_version': request.POST.get("Test_Version"),
            'test_batch' : request.POST.get("Test_Batch"),
                'Code': request.POST.get("Code"),
            }
            connect='GetOnesheet'#'GetSummaryData'
            logger.info("SelectPage(request):%s"%dic)
            data = API().APIall(connect, dic)
            logger.info("SelectPage(request):%s"%'请求接口')
            logger.info("SelectPage(request):%s"%data)
            if data['counts']!=0:
                return render(request, 'tetshtml.html',{"dic":data})
            else:
                return HttpResponse("暂无数据，可能正在在测试数据中……")

        elif 'Image_Path' in request.POST:
            logger.info("SelectPage(request):%s" % request.POST)

            dic={
                'test_version': request.POST.get("Test_Version"),
                'test_batch': request.POST.get("Test_Batch"),
                'Code': request.POST.get("Code"),
                "Test_Chart": request.POST.get("Test_Chart"),
            }
            connect='GetPic'#'GetSummaryData'
            logger.info("SelectPage(request):%s"%dic)
            data = API().APIall(connect, dic)
            logger.info("SelectPage(request):%s"%'请求接口')
            logger.info("SelectPage(request):%s"%data)

            imagepath=data['datalist'][0]['Image_Path'].split('/')
            data['datalist'][0].update({'Image_Path':'../static/images/testpci/%s/%s'%(imagepath[-2],imagepath[-1])})
            logger.info(data)

            if data['counts']!=0:
                return render(request, 'pic.html',{"dic":data['datalist'][0]})##'../static/images/testpci/%s/%s'%(imagepath[-2],imagepath[-1])
            else:
                return HttpResponse("暂无数据，可能正在在测试数据中……")
        elif 'threshold' in request.POST:



            logger.info("'threshold	' in request.POST:%s"%request.POST)
            dic={
            'test_version': request.POST.get("Test_Version"),
            'test_batch' : request.POST.get("Test_Batch"),
            }
            connect='GetSummaryData'#'GetSummaryData'
            logger.info("SelectPage(request):%s"%dic)
            data = API().APIall(connect, dic)
            dic_zql=API().APIall('Linechart', dic)#准确率散点图基础数据
            dic_dbl=API().APIall('Proportion_zb', dic)#准确率饼状分布图基础数据
            logger.info("SelectPage(request):%s"%'请求接口')
            logger.info("SelectPage(request):%s"%data)
            logger.info("SelectPage(request) dic_zql:%s" % dic_zql)
            if data['counts']!=0:
                data.update({"dic_dbl":dic_dbl})
                logger.info("添加dic_dbl数据:%s" % data)
                list=Fanchar().Generating(data)
                htmlname = 'zhexiantu_zql.html'
                ScatterRender().scatter_render(dic_zql['datalist'], htmlname)
                list.insert(0,htmlname)

                #return render(request, 'Onesheetform.html', {"dic": ''})
                return render(request, 'Onesheetform.html',{"dic":{'html':list,'data':data}})
            else:
                return HttpResponse("暂无数据，可能正在在测试数据中……")


    dic=API().GetStart()

    logger.info("SelectPage(request):%s"%'打开SelectPage')
    return render(request, "SelectPage.html", {"dic": dic})

def homepage(request):

    logger.info(" homepage(request):%s" % '打开homepage.html')

    return render(request, "homepage.html")
def tetshtml(request):
    logger.info(" tetshtml(request):%s" % '打开tetshtml.html')
    return render(request, "tetshtml.html")

def AddTestinfo(request):
    if request.method == 'POST':
        logger.info("'threshold	' in request.POST:%s" % request.POST)
        if  "version" in request.POST :
            dic = {
                    "version": request.POST.get("version", None),
                   "release_time": request.POST.get("release_time", None),
                   "developer": request.POST.get("developer", None),
                   }
            data = API().APIall('Addtestinfo', dic)
            return HttpResponse(data['message'])

    return render(request, "AddTestinfo.html", {"dic": ''})

    # logger.info(" AddTestinfo:%s" % '打开AddTestinfo.html')
    # return render(request, "AddTestinfo.html", {"dic": ''})

def SampleBatch(request):
    if request.method == 'POST':
        logger.info("'threshold	' in request.POST:%s" % request.POST)
        if  "batch" in request.POST :
            dic = {
                "batch": request.POST.get("batch", None),
                # "types_num": request.POST.get("types_num"),
                # "total_num": request.POST.get("total_num"),
                "batch_date": request.POST.get("batch_date", None),
                "batch_path": request.POST.get("batch_path", None),
            }
            logger.info(dic)
            data = API().APIall('SampleBatch', dic)
            return HttpResponse(data['message'])

    return render(request, "SampleBatch.html", {"dic": ''})


def navigation(request):

    return render(request, "navigation.html", {"dic": ''})

