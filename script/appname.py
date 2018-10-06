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
import config
import source

def GetPackage(osSrc,isHD): 
    jsonData = loadJson(isHD) 
    key = "PACKAGE_IOS"
    if osSrc == source.ANDROID:
        key = "PACKAGE_ANDROID" 
    ret = jsonData[key]
    return ret

def GetJsonFile(isHd):
    cur_path = common.GetProjectConfigApp()+"/appname"
    jsonfile = cur_path+'/appname.json'
    if isHd:
        jsonfile = cur_path+'/appname_hd.json'
    return jsonfile

def loadJson(isHd): 
    jsonfile = GetJsonFile(isHd) 
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


def replaceFile(filePath, strOld, strReplace):
    f = open(filePath, 'r')
    strFile = f.read() 
    strOut = strFile.replace(strOld, strReplace)
    f.close()
    saveString2File(strOut, filePath)


def replaceStringOfFile(filePath, strStart, strEnd, strReplace):
    f = open(filePath, 'r')
    strFile = f.read()
    # strFile.decode('utf-8')
    # print strFile
    strOut = replaceString(strFile, strStart, strEnd, strReplace)
    # print strOut
    # fp_name.seek(0)
    # fp_name.write(strOut)
    f.close()
    return strOut

def replacePackage(filePath,package):
    f = open(filePath, 'r')
    strFile = f.read()
    f.close() 
    strFile = strFile.replace("_PACKAGE_", package)
    common.saveString2File(strFile,filePath)
     

def replaceString2(strContent, strStart, strMid, strEnd, strReplace):
    idx = strContent.find(strStart)
    if idx<0:
        return strContent
    strHead = strContent[0:idx] + strStart

    idx = idx + len(strStart)
    strOther = strContent[idx:] 
    idx = strOther.find(strMid)
    strHead2 = strOther[0:idx] + strMid
    strHead += strHead2

    # print "strOther1="+strOther 
    strOther = strOther[idx+len(strMid):]
    # print "strOther2="+strOther

    idx = strOther.find(strEnd)
    strOther = strOther[idx:] 
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

def replaceXcodeUrlScheme(filePath, src, appid,idx):
    f = open(filePath, 'r')
    strFile = f.read() 
    f.close()

    # <string>WEIXIN_APPID</string>
    if src==source.WEIXIN or src==source.WEIXINFRIEND:
        strOld = "<string>WEIXIN_APPID</string>"
    if src==source.WEIBO:
        strOld = "<string>WEIBO_APPID</string>"
    if src==source.QQ or src==source.QQZONE:
        if idx==0:
            strOld = "<string>QQ_APPID0</string>"
        if idx==1:
            strOld = "<string>QQ_APPID1</string>"

    strNew = "<string>"+config.XcodeUrlScheme(src,appid,idx)+"</string>"  

    strOut = strFile.replace(strOld, strNew) 
    saveString2File(strOut,filePath)
    



def updateXiaoASOkeyword(jsonData,isHd):
    jsonfile = GetJsonFile(isHd)
    APPSTORE_KEYWORD = jsonData["APPSTORE_KEYWORD"]
    cn = APPSTORE_KEYWORD["cn"]
    en = APPSTORE_KEYWORD["en"]
    cn = cn.replace(","," ")
    en = en.replace(","," ")

    strStart = "XIAOMI_KEYWORD"
    strEnd = "\""

    strFile = common.GetFileString(jsonfile)

    strMid = "\"cn\": \""
    strFile = replaceString2(strFile, strStart, strMid, strEnd, cn)

    strMid = "\"en\": \""
    strFile = replaceString2(strFile, strStart, strMid, strEnd, en)
    common.saveString2File(strFile, jsonfile)

def copyResFiles(str):
    dir_default = common.GetProjectConfigDefault()
    # "../../../default"
    dir_to = common.GetProjectConfigApp()

    dir1 = dir_default+"/"+str
    dir2 = dir_to + "/"+str
    print(dir2)
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)

def updateName(isHd):
    
    rootConfig = common.GetProjectConfigApp()
    strHD = "HD"

    project_ios = rootConfig + "/ios/project"
    project_android = rootConfig + "/android/project"

    if isHd:
        project_ios = rootConfig + "/ios/project_hd"
        project_android = rootConfig + "/android/project_hd"

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

    print "android version:"+APPVERSION_ANDROID
    print "ios version:"+APPVERSION_IOS
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
    replacePackage(file_package_android,PACKAGE_ANDROID) 
    
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
    file_name_cn_ios = project_ios + "/appname/zh-Hans.lproj/InfoPlist.strings"
    file_name_en_ios = project_ios + "/appname/en.lproj/InfoPlist.strings"
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

    # CFBundleURLSchemes
    src = source.WEIBO
    appid = config.GetShareAppId(src,source.IOS,isHd)
    replaceXcodeUrlScheme(file_package_ios,src,appid,0)

    src = source.WEIXIN
    appid = config.GetShareAppId(src,source.IOS,isHd)
    replaceXcodeUrlScheme(file_package_ios,src,appid,0)

    src = source.QQ
    appid = config.GetShareAppId(src,source.IOS,isHd)
    replaceXcodeUrlScheme(file_package_ios,src,appid,0)
    replaceXcodeUrlScheme(file_package_ios,src,appid,1)

    # xiaomi aso keyword
    updateXiaoASOkeyword(data,isHd)

# win
    updateNameWin(isHd)


def updateNameWin(isHd):
    strOld = "_APP_NAME_"
    rootConfig = common.GetProjectConfigApp()
    project = rootConfig + "/win"
    file_name_cn = project + "/strings/zh-cn/resources.resw"
    file_name_en= project + "/strings/en-us/resources.resw"

    data = loadJson(isHd)
    APP_NAME_CN= data["APP_NAME_CN_ANDROID"]
    APP_NAME_EN = data["APP_NAME_EN_ANDROID"] 

    # cn
    replaceFile(file_name_cn, strOld, APP_NAME_CN)
    # en
    replaceFile(file_name_en, strOld, APP_NAME_EN)

    PACKAGE = data["PACKAGE_ANDROID"]
   
    filepath= project + "/strings/common.resw"
    replaceFile(filepath, "_APP_PACKAGE_", PACKAGE)
 
    # # <Identity Name="47113moonma.KidsShapeColor"
    # strStart = "<Identity Name=\""
    # strEnd = "\""
    # filepath= common.GetRootProjectWin()+"/"+ common.GetProjectName()+ "/Package.appxmanifest"
    # strOut = replaceStringOfFile(file, strStart, strEnd, PACKAGE)
    # saveString2File(strOut, file)



# 主函数的实现
if __name__ == "__main__":
    # 设置为utf8编码
    reload(sys)
    sys.setdefaultencoding("utf-8")

    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1,count):
        print "参数", i, sys.argv[i]
        if i==1:
            cmdPath = sys.argv[i]
    
    common.SetCmdPath(cmdPath)
    


#先从default 拷贝 工程文件模版
    # ios project file
    copyResFiles(source.IOS)
    # android project file
    copyResFiles(source.ANDROID)
    # win 
    copyResFiles(source.WIN)

    updateName(False)
    updateName(True)

    print "appname sucess"
