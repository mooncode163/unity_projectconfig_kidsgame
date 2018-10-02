#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path
import time,  datetime

#http://blog.csdn.net/imzoer/article/details/8733396
#http://blog.sina.com.cn/s/blog_708be8850101bu02.html
##复制文件
#
#shutil.copyfile('listfile.py', 'd:/test.py')
#
##复制目录
#
#shutil.copytree('d:/www', 'c:/temp/')

#把某一目录下的所有文件复制到指定目录中
def copyFiles(sourceDir,  targetDir):
    if sourceDir.find(".svn") > 0:
        return
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(sourceFile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                open(targetFile, "wb").write(open(sourceFile, "rb").read())
#    if os.path.isdir(sourceFile):
#        First_Directory = False
#        copyFiles(sourceFile, targetFile)

#复制一级目录下的所有文件到指定目录：
def coverFiles(sourceDir,  targetDir):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
        targetFile = os.path.join(targetDir,  file)
            #cover the files
        if os.path.isfile(sourceFile):
            # print sourceFile
            open(targetFile, "wb").write(open(sourceFile, "rb").read())
        #目录嵌套
        if os.path.isdir(sourceFile):
            # print sourceFile
            coverFiles(sourceFile,targetFile)


#删除一级目录下的所有文件：
def removeFileInFirstDir(targetDir):
     for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(targetFile):
            os.remove(targetFile)
 
 # 复制单个文件
def copyOneFile(sourceFile,  targetFile):
        if os.path.isfile(sourceFile):
            open(targetFile, "wb").write(open(sourceFile, "rb").read())


#返回当前的日期，以便在创建指定目录的时候用：
# def getCurTime():
#           nowTime = time.localtime()
#                 year = str(nowTime.tm_year)
#                     month = str(nowTime.tm_mon)
#                         if len(month) < 2:
#                                 month = '0' + month
#                                 day =  str(nowTime.tm_yday)
#                                     if len(day) < 2:
#                                             day = '0' + day
#     return (year + '-' + month + '-' + day)

#获取脚本文件的当前路径
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

#last dir
def getLastDir():
    path = cur_file_dir()
    idx = path.rfind('/')
    ret = path[0:idx]
    return ret

def getGameName():
    path = cur_file_dir()
    idx = path.rfind('/')
    s_len=len(path)
    game = path[idx+1:s_len]
    return game

def getGameType():
    name = getGameName()
    idx = name.find('_')
    s_len=len(name)
    game = name[0:idx]
    return game 
