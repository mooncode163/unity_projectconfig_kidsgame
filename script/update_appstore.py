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
import xml.etree.ElementTree as ET  
#include common.py
sys.path.append('./common')
import common


DEVICE_IPADPRO = "ipadpro"
DEVICE_IPADPRO_2018 = "ipadpro"
DEVICE_IPHONE_6_5 = "iphone_6_5"
DEVICE_IPHONE_5_5 = "iphone"

list_language = ["cn", "en"] 
listCountry = ["en-US", "zh-Hans","en-CA","en-AU","en-GB"]  
listCountryLanguage = ["en", "cn","en","en","en"] 

totalScreenshot = 5 
list_device = [DEVICE_IPADPRO, DEVICE_IPHONE_5_5]
# list_device = [DEVICE_IPADPRO,DEVICE_IPADPRO_2018, DEVICE_IPHONE_6_5,DEVICE_IPHONE_5_5]
gameName = " "
gameType = " "
enableScrenshot = False

def loadJson(isHd):
    cur_path = common.GetProjectConfigApp()+"/appname"
    jsonfile = cur_path+'/appname.json'
    if isHd:
        jsonfile = cur_path+'/appname_hd.json'

    with open(jsonfile) as json_file:
        data = json.load(json_file)
        return data

def loadXmlDescription(isHd):
    cur_path = common.GetProjectConfigApp()+"/appname"
    xmlfile = cur_path+'/app_description.xml'
    if isHd:
        xmlfile = cur_path+'/app_description_hd.xml'

    tree = ET.parse(xmlfile)  
    root = tree.getroot()  

    # cn = root.find('en')
    # print cn.tag
    # print cn.text

    return root

def getXmlDescriptionText(root,key):
    for child in root.findall(key): 
        return child.text
    # return root.find(key).text

def replaceIAP_noad(filePath,strReplace):
    f = open(filePath, 'r')
    strContent = f.read() 
    
    strStart = "<in_app_purchase>"
    idx = strContent.find(strStart)
    strHead = strContent[0:idx] + strStart

    idx = idx + len(strStart)
    strOther = strContent[idx:]
    
    strMid = "<product_id>"
    idx = strOther.find(strMid)
    strHead2 = strOther[0:idx] + strMid
    strHead += strHead2

    strEnd = "</product_id>"
    idx = strOther.find(strEnd)
    strOther = strOther[idx:] 
    strRet = strHead + strReplace + strOther

    f.close()
    saveString2File(strRet,filePath) 


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

def replaceXmlKey(filepath,language,key,title):
 
    strStart = language
    # <keyword>
    strMid = "<"+key+">" 
    # </keyword>
    strEnd = "</"+key+">" 
    strOut = replaceStringOfFile2(
        filepath, strStart, strMid, strEnd, title)
    saveString2File(strOut, filepath)
# <software_screenshots></software_screenshots>
# <!-- <software_screenshots></software_screenshots> -->
# 注释xmlkey
def disableXmlKey(filePath,key):
    strFrom = "<"+key+">"+"</"+key+">"
    strTo = "<!-- <"+key+">"+"</"+key+"> -->"
    strFile = common.GetFileString(filePath)
    strFile = strFile.replace(strFrom,strTo)
    common.saveString2File(strFile,filePath)
 
def getScreenshotFileName(device,language,idx): 
    return language+"_"+device+"_"+str(idx+1)+".jpg";

def getScreenshotFullFilePath(isHd,device,language,idx): 
    strDir_itmsp = "app.itmsp"
    if isHd:
        strDir_itmsp = "app_pad.itmsp"
    strDirRootTo = common.GetProjectConfigApp()+"/appstore/ios/"+strDir_itmsp
    strFileTo = strDirRootTo+"/"+getScreenshotFileName(device,language,idx)
    return strFileTo

def copy_or_delete_one_screenshot(isHd,device,language,idx,isDel):
    strDirHorV = "shu"
    if isHd:
        strDirHorV = "heng" 

    strDirRootFrom =common.GetProjectOutPutApp()+"/screenshot"
    strFileFrom = strDirRootFrom+"/"+strDirHorV+"/"+language+"/"+device+"/"+str(idx+1)+".jpg";
 
    strFileTo = getScreenshotFullFilePath(isHd,device,language,idx)

    if isDel:
        if os.path.isfile(strFileTo):
            os.remove(strFileTo)
    else:
        print strFileFrom
        if os.path.isfile(strFileFrom):
            shutil.copyfile(strFileFrom,strFileTo)

def copy_screenshots(): 
    list_hd = [False, True]
    
    for device in list_device:
        print "copy_screenshots device="+device
        for language in list_language:
            for ishd in list_hd:
                for i in range(0, totalScreenshot):
                    copy_or_delete_one_screenshot(ishd,device,language,i,False) 


def delete_screenshots(): 
    list_hd = [False, True]
    
    for device in list_device:
        for language in list_language:
            for ishd in list_hd:
                for i in range(0, totalScreenshot):
                    copy_or_delete_one_screenshot(ishd,device,language,i,True) 

# /*
# <software_screenshot display_target="iOS-5.5-in" position="1">
#                                   <file_name>iphone_1.jpg</file_name>
#                                   <size>263616</size>
#                                   <checksum type="md5">dc695d677a5c33392bc88ba4eb9d719f</checksum>
#                                </software_screenshot> 
#                                */
def getXmlStringOneScreenshot(isHd,device,language,idx):  
    filePath = getScreenshotFullFilePath(isHd,device,language,idx)
    strRet = " " 
    if enableScrenshot:
        strRet = "<software_screenshot display_target=\""+getAppStoreScreenshotDeviceName(device)+"\" position=\""+str(idx+1)+"\"> <file_name>"+getScreenshotFileName(device,language,idx)+"</file_name> <size>"+str(common.get_FileSize(filePath))+"</size> <checksum type=\"md5\">"+common.get_MD5_checksum_file(filePath)+"</checksum> </software_screenshot>"       
    return strRet

def getXmlStringScreenshots(isHd,language):
    
    strRet = " "
    for device in list_device:
        for i in range(0, totalScreenshot):
            strFileTo = getScreenshotFullFilePath(isHd,device,language,i)
            if os.path.isfile(strFileTo):
                strRet+="\n"+getXmlStringOneScreenshot(isHd,device,language,i)
    return strRet

def getAppStoreScreenshotDeviceName(device):
    strRet = device
    if device==DEVICE_IPADPRO:
        strRet = "iOS-iPad-Pro"
    if device==DEVICE_IPHONE_5_5:
        strRet = "iOS-5.5-in"
    if device==DEVICE_IPHONE_6_5:
        strRet = "iOS-6.5-in"
        
    return strRet

def updateAppstore(isHd):
    
   
    rootConfig = common.GetProjectConfigApp()
    strHD = "HD"

    metadata_ios = rootConfig + "/appstore/ios/app.itmsp/metadata.xml" 

    if isHd:
        metadata_ios = rootConfig + "/appstore/ios/app_pad.itmsp/metadata.xml" 

    xmlRoot = loadXmlDescription(isHd) 

    # filePath = rootConfig + "appstore/ios/app.itmsp/in_app_purchases_screenshot.png" 
    # print common.get_MD5_checksum_file(filePath)

    # loadJson
    data = loadJson(isHd)
    APP_NAME_CN_ANDROID = data["APP_NAME_CN_ANDROID"]
    APPSTORE_VERSION_UPDATE = data["APPSTORE_VERSION_UPDATE"]
    APPSTORE_TITLE = data["APPSTORE_TITLE"]
    APPSTORE_SUBTITLE = data["APPSTORE_SUBTITLE"]
    APPSTORE_PROMOTION = data["APPSTORE_PROMOTION"]
    PACKAGE = data["PACKAGE_IOS"]
    # APPSTORE_DESCRIPTION = data["APPSTORE_DESCRIPTION"]
    APPSTORE_KEYWORD = data["APPSTORE_KEYWORD"]
    APPVERSION_IOS = data["APPVERSION_IOS"]
    software_url = data["software_url"]
    privacy_url = data["privacy_url"]
    support_url = data["support_url"]
    sku_app = data["sku_app"]
    need_upload_screenshot = data.get("need_upload_screenshot",False)
    global enableScrenshot

    enableScrenshot = need_upload_screenshot
    if APPVERSION_IOS=="1.0.0":
        enableScrenshot = True 
 
# ios
#     sku_app
    strStart = "<vendor_id>"
    strEnd = "</vendor_id>"
    
    strOut = replaceStringOfFile(
        metadata_ios, strStart, strEnd, sku_app)
    saveString2File(strOut, metadata_ios)
    
    # APPVERSION_IOS
    # <version string="1.0.0">
    strStart = "<version string=\""
    strEnd = "\">"
    strOut = replaceStringOfFile(
        metadata_ios, strStart, strEnd, APPVERSION_IOS)
    saveString2File(strOut, metadata_ios)
 
    # 版本更新说明 
    key = "version_whats_new"
    if APPVERSION_IOS=="1.0.0": 
        disableXmlKey(metadata_ios,key)
    else:
        jsonData = APPSTORE_VERSION_UPDATE
        idx = 0
        for country in listCountry:
            lan = listCountryLanguage[idx]
            replaceXmlKey(metadata_ios,country,key,jsonData[lan])
            idx += 1


    # APPSTORE_TITLE
    key = "title"
    jsonData = APPSTORE_TITLE
    idx = 0
    for country in listCountry:
        lan = listCountryLanguage[idx]
        replaceXmlKey(metadata_ios,country,key,jsonData[lan])
        idx += 1

 
    # APPSTORE_TITLE
    key = "subtitle"
    jsonData = APPSTORE_SUBTITLE
    idx = 0
    for country in listCountry:
        lan = listCountryLanguage[idx]
        replaceXmlKey(metadata_ios,country,key,jsonData[lan])
        idx += 1
 
  # APPSTORE_PROMOTION
    key = "promotional_text"
    jsonData = APPSTORE_PROMOTION
    idx = 0
    for country in listCountry:
        lan = listCountryLanguage[idx]
        replaceXmlKey(metadata_ios,country,key,jsonData[lan])
        idx += 1

     # APPSTORE_DESCRIPTION
    key = "description"
    # jsonData = APPSTORE_DESCRIPTION 
    idx = 0
    for country in listCountry:
        lan = listCountryLanguage[idx]
        desc = getXmlDescriptionText(xmlRoot,lan)
        replaceXmlKey(metadata_ios,country,key,desc)
        idx += 1

 
    # APPSTORE_KEYWORD
    key = "keyword"
    jsonData = APPSTORE_KEYWORD
    idx = 0
    for country in listCountry:
        lan = listCountryLanguage[idx]
        replaceXmlKey(metadata_ios,country,key,jsonData[lan])
        idx += 1
 
    # software_url
    key = "software_url"
    jsonData = software_url
    idx = 0
    for country in listCountry: 
        replaceXmlKey(metadata_ios,country,key,jsonData)
        idx += 1

       # support_url
    key = "support_url"
    jsonData = support_url
    idx = 0
    for country in listCountry:
        lan = listCountryLanguage[idx]
        replaceXmlKey(metadata_ios,country,key,jsonData)
        idx += 1

       # privacy_url
    key = "privacy_url"
    jsonData = privacy_url
    idx = 0
    for country in listCountry:
        lan = listCountryLanguage[idx]
        replaceXmlKey(metadata_ios,country,key,jsonData)
        idx += 1

# screenshot
    key = "software_screenshots" 
    if enableScrenshot:
        screenshot_cn = getXmlStringScreenshots(isHd,"cn")
        screenshot_en = getXmlStringScreenshots(isHd,"en")
        replaceXmlKey(metadata_ios,"en-US",key,screenshot_en)
        replaceXmlKey(metadata_ios,"zh-Hans",key,screenshot_cn)
        # replaceXmlKey(metadata_ios,"en-CA",key,screenshot_en)
        # replaceXmlKey(metadata_ios,"en-AU",key,screenshot_en)
        # replaceXmlKey(metadata_ios,"en-GB",key,screenshot_en) 
    else:
        disableXmlKey(metadata_ios,"software_screenshots")


# noad
    replaceIAP_noad(metadata_ios,PACKAGE+".noad")
    # replaceIAP_noad(metadata_ios,"noad")

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
    gameName = common.getGameName()
    gameType = common.getGameType()
   
    print gameName
    print gameType

    if len(sys.argv)>2:
        if sys.argv[2] == "delete_screenshot":
            delete_screenshots()
            sys.exit(0)   


    #先从default 拷贝 文件模版
    dir_default = common.GetProjectConfigDefault()
    dir_to = common.GetProjectConfigApp()
    dir1 = dir_default+"/appstore"
    dir2 = dir_to + "/appstore"
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)

    shutil.copytree(dir1,dir2)

    copy_screenshots()
    

    updateAppstore(False)
    updateAppstore(True)

    print "appname sucess"
