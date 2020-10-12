from django.shortcuts import render

# Create your views here.
import json
import os,time
import base64
from framework.NoNone import *
from django.shortcuts import render, HttpResponse, redirect
from framework.API import API
from framework.Fanchart import Fanchar
from framework.ScatteRender import ScatterRender
from framework.getImage import Pathlsit
from framework.logger import Logger
logger = Logger(logger="views").getlog()
'''
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
def tetshtml(request):
    logger.info(" tetshtml(request):%s" % '打开tetshtml.html')
    return render(request, "tetshtml.html")
def navigation(request):

    return render(request, "navigation.html", {"dic": ''})
'''
def homepage(request):

    logger.info(" homepage(request):%s" % '打开homepage.html')

    return render(request, "homepage.html")

def AddTestinfo(request):
    if request.method == 'POST':
        logger.info("'threshold	' in request.POST:%s" % request.POST)
        if  "version" in request.POST :
            dic = {
                    "version": request.POST.get("version", None).replace(' ',''),
                   "release_time": request.POST.get("release_time", None).replace(' ',''),
                   "developer": request.POST.get("developer", None).replace(' ',''),
                   }
            if NnNone_dic(dic)==0:
                return HttpResponse('输入值不能为空,请重新填写……')

            elif NnNone_dic(dic) == 1:
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
                "batch": request.POST.get("batch", None).replace(' ',''),
                # "types_num": request.POST.get("types_num"),
                # "total_num": request.POST.get("total_num"),
                "batch_date": request.POST.get("batch_date", None).replace(' ',''),
                "batch_path": request.POST.get("batch_path", None).replace(' ',''),
            }
            logger.info(dic)
            if NnNone_dic(dic)==0:
                return HttpResponse('输入值不能为空,请重新填写……')

            elif NnNone_dic(dic) == 1:
                data = API().APIall('SampleBatch', dic)
                return HttpResponse(data['message'])


    return render(request, "SampleBatch.html", {"dic": ''})




def ViewResults(request):

    dic_summary = {
        "table_name": 'summary',
    }
    data = API().APIall('Getform', dic_summary)

    operation = [['查看', 'see'], ['删除', 'del']]
    entry_name_lies=[['序列','id'],['样本批次','Test_Batch'],['算法版本','Test_Version'],['测试时间','Test_Time'],['样本类型数','Total_Type'],['测试总数量', 'Sum_Numbers'],['通过数', 'Sum_Pass'],['失败数', 'Sum_Fail'],['达标数', 'Standard'],['未达标数', 'UnStandard'],['达标率阀值', 'threshold'],['达标率', 'StandardRate']]
    #operation = [['删除','del']]
    #operation = []
    if request.method == 'POST':
        logger.info("'threshold	' in request.POST:%s" % request.POST)
        if 'threshold' in request.POST and 'see' in request.POST:#测试结果列表页查看单个测试结果详情
            dic={
            'test_version': request.POST.get("Test_Version"),
            'test_batch' : request.POST.get("Test_Batch"),
            }
            connect='GetSummaryData'#'GetSummaryData'
            logger.info("ViewResults(request):%s"%dic)
            data = API().APIall(connect, dic)
            dic_zql=API().APIall('Linechart', dic)#准确率散点图基础数据
            dic_dbl=API().APIall('Proportion_zb', dic)#准确率饼状分布图基础数据
            logger.info("ViewResults(request):%s"%'请求接口')
            logger.info("ViewResults(request):%s"%data)
            logger.info("ViewResults(request) dic_zql:%s" % dic_zql)
            if data['counts']!=0:
                data.update({"dic_dbl":dic_dbl})
                logger.info("添加dic_dbl数据:%s" % data)
                list=Fanchar().Generating(data)
                htmlname = 'zhexiantu_zql.html'
                ScatterRender().scatter_render(dic_zql['datalist'], htmlname)
                list.insert(0,htmlname)
                dic_excle={
                    "filename": '文物算法准确率测试报告.xlsx',
                    'Test_Version': request.POST.get("Test_Version"),
                    'Test_Batch': request.POST.get("Test_Batch"),
                }
                Excledata = API().APIall('DownloadExcle', dic_excle)['datalist']
                logger.info(Excledata)
                filebase64 = Excledata['filebase64']
                filename = dic_excle['filename']
                save_path = os.getcwd() + "\\static\\file\\" + filename
                with open(save_path, 'wb') as f:
                    f.write(base64.b64decode(filebase64))
                    # return render(request, 'Onesheetform.html', {"dic": ''})
                    data.update({"Excleptah":'../static/file/%s'%filename})
                    dic_out={'html': list, 'data': data}
                    logger.info(dic_out)
                    return render(request, 'Onesheetform.html', {"dic": dic_out})
            else:
                return HttpResponse("暂无数据，可能正在在测试数据中……")

        elif 'threshold' in request.POST and 'del' in request.POST:  # 测试结果列表页删除 单个测试结果详情
            dic_data={
                'table_name': 'summary',
            'Test_Version': request.POST.get("Test_Version"),
            'Test_Batch' : request.POST.get("Test_Batch"),
            }
            dic={"dic_data":(dic_data)}
            API().APIall('del_summary_data', dic)  # 删除一行结果

            data = API().APIall('Getform', dic_summary)
            return render(request,'ViewResults.html' ,{"dic": data,'operation':operation,'entry_name_lies':entry_name_lies})#

        if 'GetData' in request.POST and 'GetResultsData' in request.POST:#在单个测试结果界面进入测试结果汇总页
            logger.info("ViewResults(request)-GetData:%s"%request.POST)
            dic={
            'test_version': request.POST.get("Test_Version"),
            'test_batch' : request.POST.get("Test_Batch")
            }
            connect=request.POST.get("GetData")#'GetSummaryData'
            logger.info("ViewResults(request):%s"%dic)
            data = API().APIall(connect, dic)
            logger.info("ViewResults(request):%s"%'请求接口')
            logger.info("ViewResults(request):%s"%data)
            if data['counts']!=0:

                operation = [['查看', 'see'], ['删除', 'del']]
                entry_name_lies = [['序列', 'id'], ['样本批次', 'Test_Batch'], ['算法版本', 'Test_Version'],
                                   ['测试时间', 'Test_Time'],  ['物品名称', 'Cultural_Name'],
                                   ['物品编号', 'Code'], ['测试数', 'Test_Number'], ['通过', 'PASS'],
                                   ['失败', 'FAIL'], ['错误', 'ERROR'], ['准确率', 'Accuracy'],
                                   ]
                # operation = [['删除','del']]
                # operation = []
                return render(request, 'ViewResults.html',
                              {"dic": data, 'operation': [operation[0]], 'entry_name_lies': entry_name_lies})  #
                #return render(request, 'tetshtml.html',{"dic":data})
            else:
                return HttpResponse("暂无数据，可能正在在测试数据中……")

        elif 'GetSheetData' in request.POST:# #在某个测试结果界面进入所有测试记录列表界面
            logger.info("ViewResults(request):%s"%request.POST)
            dic={
            'test_version': request.POST.get("Test_Version"),
            'test_batch' : request.POST.get("Test_Batch")
            }
            connect=request.POST.get("GetData")#'GetSummaryData'
            logger.info("ViewResults(request):%s"%dic)
            data = API().APIall(connect, dic)
            logger.info("ViewResults(request):%s"%'请求接口')
            logger.info("ViewResults(request):%s"%data)
            if data['counts']!=0:

                operation = [['查看', 'see'], ['删除', 'del']]
                entry_name_lies = [['序列', 'id'], ['样本批次', 'Test_Batch'], ['算法版本', 'Test_Version'],
                                   ['测试时间', 'Test_Time'], ['物品名称', 'Cultural_Name'],
                                   ['图片', 'Test_Chart'],['物品编号', 'Code'], ['期望值', 'Expected_Value'],['耗时', 'TimeConsuming'], ['top_1值', 'top1'],
                                   ['top_2值', 'top2'], ['top_3值', 'top3'], ['测试结果', 'Result'],['图片路径', 'Image_Path']]

                # operation = [['删除','del']]
                # operation = []
                return render(request, 'ViewResults.html',
                              {"dic": data, 'operation': [operation[0]], 'entry_name_lies': entry_name_lies})  #
                #return render(request, 'tetshtml.html',{"dic":data})
            else:
                return HttpResponse("暂无数据，可能正在在测试数据中……")


        elif 'Accuracy' in request.POST :#在测试汇总页面进入查看某类物品测试列表

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
                #return render(request, 'tetshtml.html',{"dic":data})

                operation = [['查看', 'see'], ['删除', 'del']]
                entry_name_lies = [['序列', 'id'], ['样本批次', 'Test_Batch'], ['算法版本', 'Test_Version'],
                                   ['测试时间', 'Test_Time'],['物品名称', 'Cultural_Name'],
                                   ['图片', 'Test_Chart'],['物品编号', 'Code'], ['期望值', 'Expected_Value'],['耗时', 'TimeConsuming'], ['top_1值', 'top1'],
                                   ['top_2值', 'top2'], ['top_3值', 'top3'], ['测试结果', 'Result'],['图片路径', 'Image_Path']]

                # operation = [['删除','del']]
                # operation = []
                return render(request, 'ViewResults.html',
                              {"dic": data, 'operation': [operation[0]], 'entry_name_lies': entry_name_lies})  #
                #return render(request, 'tetshtml.html',{"dic":data})
            else:
                return HttpResponse("暂无数据，可能正在在测试数据中……")

        elif 'Image_Path' in request.POST:#查看某张图片测试结果
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
                return render(request,'ViewResults.html' ,{"dic": data,'operation':operation,'entry_name_lies':entry_name_lies})#

    return render(request,'ViewResults.html' ,{"dic": data,'operation':operation,'entry_name_lies':entry_name_lies})#
def Sample_list(request):#样本列表
    dic_sample_batch = {
        "table_name": 'sample_batch',
    }
    data = API().APIall('Getform', dic_sample_batch)
    #operation = [['查看', 'see'], ['删除', 'del']]
    entry_name_lies=[['序列','id'],['样本批次','batch'],['样本类型数','types_num'],['总数量','total_num'],['添加时间', 'batch_date'],['路径', 'batch_path']]
    operation = [['删除','del']]
    #operation = []

    if request.method == 'POST':
        #logger.info("'threshold	' in request.POST:%s" % request.POST)
        if  "batch" in request.POST and 'sees' in request.POST :
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
        elif 'total_num' in request.POST and 'del' in request.POST:
            dic_data={
                'table_name': 'sample_batch',
            'batch': request.POST.get("batch"),
            'batch_path' : request.POST.get("batch_path"),
            }
            dic={"dic_data":(dic_data)}
            API().APIall('del_summary_data', dic)  # 删除一行结果

            data = API().APIall('Getform', dic_sample_batch)
            return render(request, 'ViewResults.html',
                          {"dic": data, 'operation': operation, 'entry_name_lies': entry_name_lies})  #

    return render(request,'ViewResults.html' ,{"dic": data,'operation':operation,'entry_name_lies':entry_name_lies})#


def Algorithm_version_list(request):#算法列表

    dic_table = {
        "table_name": 'algorithm_version',
    }
    data = API().APIall('Getform', dic_table)
    #operation = [['查看', 'see'], ['删除', 'del']]
    entry_name_lies=[['序列','id'],['版本号','version'],['添加/发布时间','release_time'],['开发者','developer']]
    operation = [['删除','del']]
    #operation = []

    if request.method == 'POST':
        #logger.info("'threshold	' in request.POST:%s" % request.POST)
        if  "batch" in request.POST and 'sees' in request.POST :
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
        elif 'version' in request.POST and 'del' in request.POST:
            dic_data={
                'table_name': 'algorithm_version',
            'version': request.POST.get("version"),
            'developer' : request.POST.get("developer"),
            }
            dic={"dic_data":(dic_data)}
            API().APIall('del_summary_data', dic)  # 删除一行结果

            data = API().APIall('Getform', dic_table)
            return render(request,'ViewResults.html' ,{"dic": data,'operation':operation,'entry_name_lies':entry_name_lies})#

    return render(request,'ViewResults.html' ,{"dic": data,'operation':operation,'entry_name_lies':entry_name_lies})#

