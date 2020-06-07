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
    # print(strOther2:"+strOther
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


def updateChannel(channel,ishd): 
    print("updateChannel")
    # project_config = common.GetProjectConfigApp() + "/android" + "/gradle"
    targetDir = common.GetRootDirAndroidStudio()
    sourceDir = common.GetProjectConfigApp()
    project_android = "android/project"
    rootAndroidStudio = common.GetRootDirAndroidStudio()
    targetDir = rootAndroidStudio+"/src/main"

    if ishd==True: 
        project_android = "android/project_hd"

    if channel == source.GP:
        config_adsdk_android.SetAdSdk(source.ADMOB, True) 
        config_adsdk_android.SetAdSdk(source.ADVIEW, False)
        config_adsdk_android.SetAdSdk(source.GDT, False)
        config_adsdk_android.SetAdSdk(source.XIAOMI, False)
        config_adsdk_android.SetAdSdk(source.UNITY, True)
        config_adsdk_android.SetAdSdk(source.MOBVISTA, False)   
            # 
        project_config = sourceDir+"/"+project_android+"/config" 
        xml = sourceDir+"/"+project_android+"/xml_gp" 

    else:
        xml = sourceDir+"/"+project_android+"/xml"
        config_adsdk_android.SetAdSdk(source.ADMOB, True)
        config_adsdk_android.SetAdSdk(source.MOBVISTA, False)
        config_adsdk_android.SetAdSdk(source.UNITY, True)
            # 
        project_config = sourceDir+"/"+project_android+"/config"
        
    common.coverFiles(project_config,   targetDir)
    common.coverFiles(xml,   targetDir)

    build_gradle = common.GetProjectConfigApp() + "/android" + "/gradle/build"
    # or (channel == source.GP)
    if (channel == source.TAPTAP) :
        build_gradle = build_gradle+"_"+channel 

    build_gradle = build_gradle+".gradle"

    #配置build.grade
    #common.coverFiles(build_gradle,   targetDir)

    build_gradle_dst = rootAndroidStudio+"/build.gradle"
    flag = os.path.exists(build_gradle_dst)
    if flag:
        os.remove(build_gradle_dst)

    common.copyOneFile(build_gradle,build_gradle_dst)

    #  "channel_android": "xiaomi"
    file = getConfigJsonFile()
    print ("channel_android="+file)
    strStart = "channel_android\": \""
    strEnd = "\""
    strOut = replaceStringOfFile(file, strStart, strEnd, channel)
    saveString2File(strOut, file)


# 主函数的实现
if __name__ == "__main__":
    # 设置为utf8编码
    # reload(sys)
    # sys.setdefaultencoding("utf-8")

    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1, count):
        print("参数", i, sys.argv[i])
        if i == 1:
            cmdPath = sys.argv[i]

    common.SetCmdPath(cmdPath)

    # updateChannel(source.TAPTAP)

    print ("appchannel sucess")
