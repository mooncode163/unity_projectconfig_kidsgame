#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path
import time
import datetime
import json

# include common.py
sys.path.append('./common')
import common
import config
import source
import config_adsdk_android


def getConfigJsonFile():
    return common.getAndroidProjectGameData() + "/common/channel.json"


def replaceString(strContent, strStart, strEnd, strReplace):
    idx = strContent.find(strStart)
    if idx < 0:
        return strContent

    strHead = strContent[0:idx]

    idx = idx + len(strStart)
    strOther = strContent[idx:]
    # print "strOther1:"+strOther
    idx = strOther.find(strEnd)
    strOther = strOther[idx:]
    # print "strOther2:"+strOther
    strRet = strHead + strStart + strReplace + strOther
    return strRet


def replaceStringOfFile(filePath, strStart, strEnd, strReplace):
    f = open(filePath, 'r')
    strFile = f.read()
    # print strFile
    strOut = replaceString(strFile, strStart, strEnd, strReplace)
    # print strOut
    # fp_name.seek(0)
    # fp_name.write(strOut)
    f.close()
    return strOut


def saveString2File(str, file):
    f = open(file, 'w')  # 若是'wb'就表示写二进制文件
    f.write(str)
    f.close()


def updateChannel(channel): 
    
    project = common.GetProjectConfigApp() + "/android" + "/grade"
    targetDir = common.GetRootDirAndroidStudio()
    if channel == source.GP:
        config_adsdk_android.SetAdSdk(source.ADMOB, True)
        project = common.GetProjectConfigApp() + "/android" + "/grade_"+source.GP
    else:
        config_adsdk_android.SetAdSdk(source.ADMOB, True)

    #配置build.grade
    common.coverFiles(project,   targetDir)

    #  "channel_android": "xiaomi"
    file = getConfigJsonFile()
    strStart = "channel_android\": \""
    strEnd = "\""
    strOut = replaceStringOfFile(file, strStart, strEnd, channel)
    saveString2File(strOut, file)


# 主函数的实现
if __name__ == "__main__":
    # 设置为utf8编码
    reload(sys)
    sys.setdefaultencoding("utf-8")

    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1, count):
        print "参数", i, sys.argv[i]
        if i == 1:
            cmdPath = sys.argv[i]

    common.SetCmdPath(cmdPath)

    # updateChannel(source.TAPTAP)

    print "appchannel sucess"
