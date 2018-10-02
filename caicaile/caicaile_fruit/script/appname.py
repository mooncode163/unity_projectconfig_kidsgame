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

#include common.py
sys.path.append('./common')
import common


def loadJson(isHd):
    cur_path = common.getLastDir()+"/appname"
    jsonfile = cur_path+'/appname.json'
    if isHd:
        jsonfile = cur_path+'/appname_hd.json'

    with open(jsonfile) as json_file:
        data = json.load(json_file)
        return data


def replaceString(strContent, strStart, strEnd, strReplace):
    idx = strContent.find(strStart)
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


def replaceString2(strContent, strStart, strMid, strEnd, strReplace):
    idx = strContent.find(strStart)
    strHead = strContent[0:idx] + strStart

    idx = idx + len(strStart)
    strOther = strContent[idx:]
    # print "strOther1:"+strOther
    idx = strOther.find(strMid)
    strHead2 = strOther[0:idx] + strMid
    strHead += strHead2

    idx = strOther.find(strEnd)
    strOther = strOther[idx:]
    # print "strOther2:"+strOther
    strRet = strHead + strReplace + strOther
    return strRet


def replaceStringOfFile2(filePath, strStart, strMid, strEnd, strReplace):
    f = open(filePath, 'r')
    strFile = f.read()
    # print strFile
    strOut = replaceString2(strFile, strStart, strMid, strEnd, strReplace)
    # print strOut
    # fp_name.seek(0)
    # fp_name.write(strOut)
    f.close()
    return strOut


def saveString2File(str, file):
    f = open(file, 'w')  # 若是'wb'就表示写二进制文件
    f.write(str)
    f.close()


def replaceGoogleServiceFile(file, package):

    strStart = "client_id\": \"android:"
    strEnd = "\""
    strOut = replaceStringOfFile(file, strStart, strEnd, package)
    saveString2File(strOut, file)

    strStart = "package_name\": \""
    strEnd = "\""
    strOut = replaceStringOfFile(file, strStart, strEnd, package)
    saveString2File(strOut, file)

    strStart = "\"android_info\""
    strMid = "package_name\": \""
    strEnd = "\","
    strOut = replaceStringOfFile2(file, strStart, strMid, strEnd, package)
    saveString2File(strOut, file)


def updateName(isHd):
    
    rootConfig = "../"
    strHD = "HD"

    project_ios = rootConfig + "ios/project"
    project_android = rootConfig + "android/project"

    if isHd:
        project_ios = rootConfig + "ios/project_hd"
        project_android = rootConfig + "android/project_hd"

    # android
    file_name_cn_android = project_android + "/res/values/strings.xml"
    file_name_en_android = project_android + "/res/values-en/strings.xml"
    file_package_android = project_android + "/xml/AndroidManifest.xml"
    file_google_service_android = project_android + "/xml/google-services.json"

    # ios
    file_name_cn_ios = project_ios + "/appname/zh-Hans.lproj/InfoPlist.strings"
    file_name_en_ios = project_ios + "/appname/en.lproj/InfoPlist.strings"
    file_package_ios = project_ios + "/Info.plist"

    # loadJson
    data = loadJson(isHd)
    APP_NAME_CN_ANDROID = data["APP_NAME_CN_ANDROID"]
    APP_NAME_EN_ANDROID = data["APP_NAME_EN_ANDROID"]
    APP_NAME_CN_IOS = data["APP_NAME_CN_IOS"]
    APP_NAME_EN_IOS = data["APP_NAME_EN_IOS"]

    PACKAGE_ANDROID = data["PACKAGE_ANDROID"]
    # if data.has_key("PACKAGE_HD_ANDROID"):
    #     PACKAGE_HD_ANDROID = data["PACKAGE_HD_ANDROID"]

    PACKAGE_IOS = data["PACKAGE_IOS"]

    APPVERSION_ANDROID = data["APPVERSION_ANDROID"]
    APPVERSION_CODE_ANDROID = data["APPVERSION_CODE_ANDROID"]
    APPVERSION_IOS = data["APPVERSION_IOS"]

    print APP_NAME_CN_ANDROID
    print APP_NAME_EN_ANDROID
    print APP_NAME_CN_IOS
    print APP_NAME_EN_IOS
    print PACKAGE_ANDROID

 # android
    # name
    strStart = "app_name\">"
    strEnd = "<"
    # cn
    strOut = replaceStringOfFile(
        file_name_cn_android, strStart, strEnd, APP_NAME_CN_ANDROID)
    saveString2File(strOut, file_name_cn_android)
    # en
    strOut = replaceStringOfFile(
        file_name_en_android, strStart, strEnd, APP_NAME_EN_ANDROID)
    saveString2File(strOut, file_name_en_android)

    # package
    strStart = "package=\""
    strEnd = "\""
    strOut = replaceStringOfFile(
        file_package_android, strStart, strEnd, PACKAGE_ANDROID)
    saveString2File(strOut, file_package_android)

    # version
    strStart = "versionName=\""
    strEnd = "\""
    strOut = replaceStringOfFile(
        file_package_android, strStart, strEnd, APPVERSION_ANDROID)
    saveString2File(strOut, file_package_android)

    strStart = "versionCode=\""
    strEnd = "\""
    strOut = replaceStringOfFile(
        file_package_android, strStart, strEnd, APPVERSION_CODE_ANDROID)
    saveString2File(strOut, file_package_android)

    # admob
    replaceGoogleServiceFile(file_google_service_android, PACKAGE_ANDROID)

# ios
    strStart = "CFBundleDisplayName\" = \""
    strEnd = "\""
    # cn
    strOut = replaceStringOfFile(
        file_name_cn_ios, strStart, strEnd, APP_NAME_CN_IOS)
    saveString2File(strOut, file_name_cn_ios)
    # en
    strOut = replaceStringOfFile(
        file_name_en_ios, strStart, strEnd, APP_NAME_EN_IOS)
    saveString2File(strOut, file_name_en_ios)

    # package
    strStart = "CFBundleIdentifier"
    strMid = "<string>"
    strEnd = "</string>"
    strOut = replaceStringOfFile2(
        file_package_ios, strStart, strMid, strEnd, PACKAGE_IOS)
    saveString2File(strOut, file_package_ios)

    strStart = "CFBundleDisplayName"
    strMid = "<string>"
    strEnd = "</string>"
    strOut = replaceStringOfFile2(
        file_package_ios, strStart, strMid, strEnd, APP_NAME_CN_IOS)
    saveString2File(strOut, file_package_ios)

    # version
    strStart = "CFBundleShortVersionString"
    strMid = "<string>"
    strEnd = "</string>"
    strOut = replaceStringOfFile2(
        file_package_ios, strStart, strMid, strEnd, APPVERSION_IOS)
    saveString2File(strOut, file_package_ios)

    strStart = "CFBundleVersion"
    strMid = "<string>"
    strEnd = "</string>"
    strOut = replaceStringOfFile2(
        file_package_ios, strStart, strMid, strEnd, APPVERSION_IOS)
    saveString2File(strOut, file_package_ios)


# 主函数的实现
if __name__ == "__main__":
    # 设置为utf8编码
    reload(sys)
    sys.setdefaultencoding("utf-8")

    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    print "脚本名：", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "参数", i, sys.argv[i]
    
    dir_default = "../../../default"
    dir_to = "../"

#先从default 拷贝 工程文件模版
    # ios project file
    dir1 = dir_default+"/ios";
    dir2 = dir_to + "/ios"
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)

    # android project file
    dir1 = dir_default+"/android";
    dir2 = dir_to + "/android"
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)
#

    updateName(False)
    updateName(True)

    print "appname sucess"
