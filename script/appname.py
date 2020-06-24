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
import adconfig
import AppVersionHuawei

versionCode = 100

def GetJsonAppId(jsonData, channel):  
    return jsonData["appid"][channel] 
 

def GetPackage(osSrc,isHD): 
    jsonData = loadJson(isHD) 
    isOld = IsOldVersion(jsonData)
    ret = ""
    if isOld:
        key = "PACKAGE_IOS"
        if osSrc == source.ANDROID:
            key = "PACKAGE_ANDROID" 
        ret = jsonData[key]
    else:      
        if osSrc == source.ANDROID:
            ret = jsonData["apppackage"][source.ANDROID]["default"] 
        if osSrc == source.IOS:
            ret = jsonData["apppackage"][source.IOS]["default"]

    return ret

def GetJsonFile(isHd):
    cur_path = common.GetProjectConfigApp()+"/appinfo"
    jsonfile = cur_path+'/appname.json'
    if isHd:
        jsonfile = cur_path+'/appname_hd.json'
    return jsonfile

def loadJson(isHd): 
    jsonfile = GetJsonFile(isHd) 
    
    with  open(jsonfile, 'rb') as json_file:
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
    strFile = common.GetFileString(filePath)
    strOut = strFile.replace(strOld, strReplace) 
    saveString2File(strOut, filePath)


def replaceStringOfFile(filePath, strStart, strEnd, strReplace):
    # f = open(filePath)
    # f = open(filePath,'r', encoding='UTF-8') 
    strFile = common.GetFileString(filePath)
    # strFile.decode('utf-8')
    # print strFile
    strOut = replaceString(strFile, strStart, strEnd, strReplace)
    # print strOut
    # fp_name.seek(0)
    # fp_name.write(strOut) 
    return strOut

def replacePackage(filePath,package):
    strFile = common.GetFileString(filePath) 
    strFile = strFile.replace("_PACKAGE_", package)
    common.saveString2File(strFile,filePath)

def replaceFileForKey(filePath,key,content):
    # f = open(filePath, 'rb')
    # f = open(filePath,'r', encoding='utf-8')
    strFile = common.GetFileString(filePath) 
    strFile = strFile.replace(key, content)
    common.saveString2File(strFile,filePath)

def replaceFile(filePath,key,value):
    strFile = common.GetFileString(filePath) 
    strFile = strFile.replace(key, value)
    common.saveString2File(strFile,filePath) 

def replaceScreenOrientation(filePath,isHd):
    strFile = common.GetFileString(filePath)

    str = "sensorPortrait"
    if isHd:
        str = "sensorLandscape"

    strFile = strFile.replace("_SCREENORIENTATION_", str)

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
    strFile = common.GetFileString(filePath)
    # print strFile
    strOut = replaceString2(strFile, strStart, strMid, strEnd, strReplace)
    # print strOut
    # fp_name.seek(0)
    # fp_name.write(strOut) 
    return strOut


def saveString2File(str, file):
    common.saveString2File(str, file)


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
    strFile = common.GetFileString(filePath)

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
    isOld = IsOldVersion(jsonData)
    if isOld:
        APPSTORE_KEYWORD = jsonData["APPSTORE_KEYWORD"]
        strStart = "XIAOMI_KEYWORD"
    else:
        APPSTORE_KEYWORD =  jsonData["appstore"]["aso"]
        strStart = "aso_xiaomi"

    
    cn = APPSTORE_KEYWORD["cn"]
    en = APPSTORE_KEYWORD["en"]
    cn = cn.replace(","," ")
    en = en.replace(","," ")

    
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

def SaveJson(filePath,dataRoot): 
    oldvalue = ""
    # "huawei": "0",
    # str1 = "\""+key+"\""+": \""+oldvalue+"\""
    # str2 = "\""+key+"\""+": \""+value+"\""
    # replaceFile(filePath, str1, str2)

    # 保存json
    with open(filePath, 'w') as f:
        json.dump(dataRoot, f, ensure_ascii=False,indent=4,sort_keys = True)


def autoPlusVersion(isHd,jsonData):
    global versionCode
    isOld = IsOldVersion(jsonData)
    if isOld:
        autoPlusVersionOldVersion(isHd,jsonData)
    else:
        jsonfile = GetJsonFile(isHd) 
        int_v = int(versionCode)
        int_v=int_v+1
        versionCode = str(int_v)
        dataCode = jsonData["appversion"][source.ANDROID]
        dataCode["code"]=versionCode

        data = jsonData["appversion"][source.ANDROID]
        data["value"]=versionCodeToVersion()

        
        data = jsonData["appversion"][source.IOS]
        codeios = data["code"]
        int_v = int(codeios)
        int_v=int_v+1
        codeios = str(int_v)
        data["code"]=codeios
        versionCode = codeios
        data["value"]=versionCodeToVersion()

        SaveJson(jsonfile,jsonData)  
        # strnew_version_ios = "\"APPVERSION_IOS\": \""+versionCodeToVersion()+"\""



def autoPlusVersionOldVersion(isHd,jsonData): 
    global versionCode 
    strold = "\"APPVERSION_CODE_ANDROID\": \""+versionCode+"\""
    strold_version_android = "\"APPVERSION_ANDROID\": \""+jsonData["APPVERSION_ANDROID"]+"\""
    strold_version_ios = "\"APPVERSION_IOS\": \""+jsonData["APPVERSION_IOS"]+"\""
    int_v = int(versionCode)
    int_v=int_v+1
    versionCode = str(int_v)
    strnew = "\"APPVERSION_CODE_ANDROID\": \""+versionCode+"\"" 
    strnew_version_android = "\"APPVERSION_ANDROID\": \""+versionCodeToVersion()+"\""
    strnew_version_ios = "\"APPVERSION_IOS\": \""+versionCodeToVersion()+"\""

    # 替换json
    jsonfile = GetJsonFile(isHd) 
 
    strOut = common.GetFileString(jsonfile)
    strOut = strOut.replace(strold, strnew)
    strOut = strOut.replace(strold_version_android, strnew_version_android)
    strOut = strOut.replace(strold_version_ios, strnew_version_ios) 

    saveString2File(strOut, jsonfile) 


     


# 161 to 1.6.1
def versionCodeToVersion():
    code_v = int(versionCode)
    # 
    v0 = int(code_v/100)
    v1 =int((code_v-v0*100)/10)
    v2 = code_v-v0*100-v1*10
    ret = str(v0)+"."+str(v1)+"."+str(v2)
    return ret

def updateAndroidManifest(filepath,package,appversion,appversioncode,isHd):
    # version 
    replaceFileForKey(filepath,"_VERSIONNAME_",appversion) 
 
    replaceFileForKey(filepath,"_VERSIONCODE_",appversioncode) 

    # package 
    replaceFileForKey(filepath,"_PACKAGE_",package) 
    # ScreenOrientation
    replaceScreenOrientation(filepath,isHd) 



def IsOldVersion(data):
    isOld = True
    if ("appname" in data) :
        isOld = False  
    
    return isOld

def GetCSVName(strContent,isHd): 
    idxstart = strContent.find("APP_NAME")
    if isHd:
        idxstart = strContent.find("APP_NAME_HD")

    strContent = strContent[idxstart:] 
    idxend = strContent.find("\r\n")
    if idxend<0:
        idxend = strContent.find("\n")

    strContent = strContent[0:idxend] 
    return strContent


def UpdateLanguageName(name_cn,name_en,ishd): 
    dirconfig = common.GetConfigDataDir()
    csvfile = dirconfig+"/language/language.csv"

    strContent = common.GetFileString(csvfile)
    key_name = GetCSVName(strContent,ishd) 

    head = "APP_NAME"
    if ishd:
        head = "APP_NAME_HD"

    str_new = head+","+name_cn+"," +name_en
    # +"\n"
    replaceFile(csvfile,key_name,str_new)


def GetConfigDataAppId(os,chanel,ishd):
    dirconfig = common.GetConfigDataDir()
    filepath = ""
    appid = ""
    if os==source.ANDROID:
        filepath = dirconfig+"/config/config_android.json"
        if ishd:
            filepath = dirconfig+"/config/config_android_hd.json"
   
    if os==source.IOS:
        filepath = dirconfig+"/config/config_ios.json"
        if ishd:
            filepath = dirconfig+"/config/config_ios_hd.json"
     

    with open(filepath) as json_file:
        data = json.load(json_file)
        appid = data["APPID"][chanel] 

    return appid

def SetConfigDataAppId(os,chanel,appid,ishd):
    dirconfig = common.GetConfigDataDir()
    filepath = ""
    if os==source.ANDROID:
        filepath = dirconfig+"/config/config_android.json"
        if ishd:
            filepath = dirconfig+"/config/config_android_hd.json"
   
    if os==source.IOS:
        filepath = dirconfig+"/config/config_ios.json"
        if ishd:
            filepath = dirconfig+"/config/config_ios_hd.json"
     

    with open(filepath) as json_file:
        data = json.load(json_file)
        data["APPID"][chanel] = appid
        SaveJson(filepath,data)

    

def updateName(isHd,isAuto):
    
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
    file_AndroidManifest = project_android + "/xml/AndroidManifest.xml"
    file_AndroidManifest_GP = project_android + "/xml_gp/AndroidManifest.xml"
    

    file_google_service_android = project_android + "/config/google-services.json"

    # ios
    file_name_cn_ios = project_ios + "/appname/zh-Hans.lproj/InfoPlist.strings"
    file_name_en_ios = project_ios + "/appname/en.lproj/InfoPlist.strings"
    file_info_plist_ios = project_ios + "/Info.plist"

    # loadJson
    data = loadJson(isHd) 

    isOld = IsOldVersion(data)
    global versionCode
    
    if not isOld : 
        appname = data["appname"]

    if isOld:
        APP_NAME_CN_ANDROID = data["APP_NAME_CN_ANDROID"]
        APP_NAME_EN_ANDROID = data["APP_NAME_EN_ANDROID"]
        APP_NAME_CN_IOS = data["APP_NAME_CN_IOS"]
        APP_NAME_EN_IOS = data["APP_NAME_EN_IOS"]
        PACKAGE_ANDROID = data["PACKAGE_ANDROID"]
        PACKAGE_IOS = data["PACKAGE_IOS"]
        versionCode = data["APPVERSION_CODE_ANDROID"]
        APPVERSION_IOS = data["APPVERSION_IOS"]
        appid_huawei = GetConfigDataAppId(source.ANDROID,source.HUAWEI,isHd)
    else:
        APP_NAME_CN_ANDROID = appname[source.ANDROID]["cn"]
        APP_NAME_EN_ANDROID = appname[source.ANDROID]["en"]
        APP_NAME_CN_IOS = appname[source.IOS]["cn"]
        APP_NAME_EN_IOS = appname[source.IOS]["en"]       
        PACKAGE_ANDROID = data["apppackage"][source.ANDROID]["default"]
        PACKAGE_IOS = data["apppackage"][source.IOS]["default"]
        versionCode = data["appversion"][source.ANDROID]["code"]
        APPVERSION_IOS =  data["appversion"][source.IOS]["value"]
        
        #appid 
        appid_ios = GetJsonAppId(data,source.APPSTORE)
        appid_taptap = GetJsonAppId(data,source.TAPTAP)
        appid_huawei = GetJsonAppId(data,source.HUAWEI)
        SetConfigDataAppId(source.IOS,source.APPSTORE,appid_ios,isHd)
        SetConfigDataAppId(source.ANDROID,source.TAPTAP,appid_taptap,isHd)
        SetConfigDataAppId(source.ANDROID,source.HUAWEI,appid_huawei,isHd)
        UpdateLanguageName(APP_NAME_CN_ANDROID,APP_NAME_EN_ANDROID,isHd)

    
    # if data.has_key("PACKAGE_HD_ANDROID"):
    #     PACKAGE_HD_ANDROID = data["PACKAGE_HD_ANDROID"]


    
 
    if isAuto==True: 
        autoPlusVersion(isHd,data)
        # 重新加载
        data = loadJson(isHd)

    APPVERSION_ANDROID = versionCodeToVersion()
    APPVERSION_CODE_ANDROID = versionCode
    

    # appversion.json
    if isAuto==False: 
        src = common.GetProjectConfigDefault()+"/appinfo/appversion.json"
        dst = common.GetProjectConfigApp()+"/appinfo/appversion.json"
        flag = os.path.exists(dst)
        # 
        if not isHd:
            shutil.copyfile(src,dst)

        strfile = common.GetFileString(dst)
        key = "_VERSION_ANDROID_"
        if isHd:
            key = "_VERSION_HD_ANDROID_"

                 
        version_web = AppVersionHuawei.ParseVersion(appid_huawei)
        strfile = strfile.replace(key,version_web) 
        common.saveString2File(strfile,dst)




    print (APP_NAME_CN_ANDROID)
    print (APP_NAME_EN_ANDROID)
    print (APP_NAME_CN_IOS)
    print (APP_NAME_EN_IOS)
    print (PACKAGE_ANDROID)

    print("android version:"+APPVERSION_ANDROID)
    print("ios version:"+APPVERSION_IOS)

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

    updateAndroidManifest(file_AndroidManifest,PACKAGE_ANDROID,APPVERSION_ANDROID,APPVERSION_CODE_ANDROID,isHd)
    updateAndroidManifest(file_AndroidManifest_GP,PACKAGE_ANDROID,APPVERSION_ANDROID,APPVERSION_CODE_ANDROID,isHd)

    # admob
    replaceGoogleServiceFile(file_google_service_android, PACKAGE_ANDROID)

# ios

    #appname
    replaceFile(file_info_plist_ios,"_APP_NAME_",APP_NAME_CN_IOS)
    file_name_cn_ios = project_ios + "/appname/zh-Hans.lproj/InfoPlist.strings"
    file_name_en_ios = project_ios + "/appname/en.lproj/InfoPlist.strings" 
    # cn
    replaceFile(file_name_cn_ios,"_APP_NAME_",APP_NAME_CN_IOS) 
    # en
    replaceFile(file_name_en_ios,"_APP_NAME_",APP_NAME_EN_IOS)  


    # package 
    replaceFile(file_info_plist_ios,"_APP_PACKAGE_",PACKAGE_IOS)

     
    # version 
    replaceFile(file_info_plist_ios,"_APP_VERSION_",APPVERSION_IOS) 

    #admob appid  
    appid = adconfig.GetCommonAppId(source.ADMOB,source.IOS,isHd)
    replaceFile(file_info_plist_ios,"_APP_ID_ADMOB_",appid) 

    # CFBundleURLSchemes
    src = source.WEIBO
    appid = config.GetShareAppId(src,source.IOS,isHd)
    replaceXcodeUrlScheme(file_info_plist_ios,src,appid,0)

    src = source.WEIXIN
    appid = config.GetShareAppId(src,source.IOS,isHd)
    replaceXcodeUrlScheme(file_info_plist_ios,src,appid,0)

    src = source.QQ
    appid = config.GetShareAppId(src,source.IOS,isHd)
    replaceXcodeUrlScheme(file_info_plist_ios,src,appid,0)
    replaceXcodeUrlScheme(file_info_plist_ios,src,appid,1)

    # xiaomi aso keyword
    updateXiaoASOkeyword(data,isHd)



# win
    updateNameWin(isHd,isAuto)


def updateNameWin(isHd,isAuto):
    strOld = "_APP_NAME_"
    rootConfig = common.GetProjectConfigApp()
    project = rootConfig + "/win/project"
    if isHd:
        project = rootConfig + "/win/project_hd"

    file_name_cn = project + "/strings/zh-cn/resources.resw"
    file_name_en= project + "/strings/en-us/resources.resw"

    data = loadJson(isHd)
    isOld = IsOldVersion(data)
    
    if not isOld : 
        appname = data["appname"]

    if isOld:
        APP_NAME_CN= data["APP_NAME_CN_ANDROID"]
        APP_NAME_EN = data["APP_NAME_EN_ANDROID"]
        PACKAGE = data["PACKAGE_ANDROID"]
    else:
        APP_NAME_CN = appname["android"]["cn"]
        APP_NAME_EN = appname["android"]["en"]
        PACKAGE = data["apppackage"]["android"]["default"]
 
    # cn
    replaceFile(file_name_cn, strOld, APP_NAME_CN)
    # en
    replaceFile(file_name_en, strOld, APP_NAME_EN)

    
   
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
    # reload(sys)
    # sys.setdefaultencoding("utf-8")
    is_auto_plus_version = False
    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1,count):
        print("参数", i, sys.argv[i])
        if i==1:
            cmdPath = sys.argv[i]
        if i==2:
            if sys.argv[i]=="true":
                is_auto_plus_version = True

    common.SetCmdPath(cmdPath)
    


#先从default 拷贝 工程文件模版
    # ios project file
    copyResFiles(source.IOS)
    # android project file
    copyResFiles(source.ANDROID)
    # win 
    copyResFiles(source.WIN)
   
    # rename
    src = common.GetProjectConfigApp()+"/appname"
    dst = common.GetProjectConfigApp()+"/appinfo"
    flag = os.path.exists(src)
    if flag:
        os.rename(src,dst)
     
    updateName(False,is_auto_plus_version)
    updateName(True,is_auto_plus_version)
 
    
    print("appname sucess")
