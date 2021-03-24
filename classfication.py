#!/usr/bin/env python
# -*- coding:utf-8 -*-

import zipfile
#import git
import os,sys
import csv
import time


import shutil
#from git import Repo
#from git import *


base_path='/home/niuben/classfication'

def is_element_exist(dateList, dataStr):
    if dataStr in dateList:
        print ("find element:%s",dataStr)
        return True
    else:
        print ("not find element %s",dataStr)
        return False

#
# 处理文件及目录
# 
# @dicPath.path 目录路径
# # copyOrMove 复制操作还是移动操作 False为复制操作，True为移动操作
def handle_file(dicPath, copyOrMove=True):
    fileList = os.listdir(dicPath)
    dateList = []
    fileDic = {}
    print(str(fileList))
    for x in fileList:
        filepath = dicPath + "/" + x
        # 判断是文件
        if os.path.isfile(filepath): 
            dataStr = get_format_time(os.path.getctime(filepath))
            print("dataStr is %s",dataStr)
            dicpath = os.path.join(dicPath, dataStr) # dicPath.path + "/" + dataStr 

            # 判断是否已记录
            if not is_element_exist(dateList, dataStr): 
                dateList.append(dataStr)
                # 根据日期创建目录
                dicpath = dicPath + "/" + dataStr
                if not os.path.exists(dicpath):
                    os.mkdir(dicpath)

            fileDic[filepath] = dicpath
            # 操作文件
            if copyOrMove:
                shutil.move(filepath, os.path.join(dicpath, x))
            else:
                shutil.copyfile(filepath, os.path.join(dicpath, x))

#
#   通过时间戳获取时间日期，取年月日
#
def get_format_time(timeStamp):
    timeStruct = time.localtime(int(timeStamp))
    return time.strftime("%Y-%m-%d", timeStruct)
    
    
    
if __name__ == '__main__':
    handle_file(base_path, copyOrMove=True)
     
