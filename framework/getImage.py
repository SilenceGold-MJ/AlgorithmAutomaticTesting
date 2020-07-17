#!/user/bin/env python3
# -*- coding: utf-8 -*-
import os,imghdr,shutil
from framework.API import API
# from framework.logger import Logger
# logger = Logger(logger="Getimage").getlog()


def Getimage(rootdir):#所有文件列表
    _files = []
    dirs=[]
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])  # 合并路径，将rootdir和list合并
        if os.path.isdir(path):
            _files.extend(Getimage(path)[0]) # 递归调用函数
            dirs.extend(Getimage(path)[1])
        if os.path.isfile(path):
            if imghdr.what(path) in ["bmp", "jpg", "png", "gif", "jpeg"]:
                _files.append(path)

                dirs.append(int(path.split('\\')[-1].split('_')[0]))

    return [_files,dirs]


def Pathlsit(rootdir):#排序
    datalist = (Getimage(rootdir))
    testNO = list(set(datalist[1]))
    testNO.sort()
    Pathlist = []
    for i in testNO:
        for n in datalist[0]:
            if i == int(n.split('\\')[-1].split('_')[0]):
                dic={
                    'name_pic':n.split('\\')[-1],
                        'data':API().getwwdata(i)['datalist'][0]
                }

                Pathlist.append(dic)
    return Pathlist

