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


def loadJson(isHd):
    cur_path = common.getLastDir()+"/appname"
    jsonfile = cur_path+'/appname.json'
    if isHd:
        jsonfile = cur_path+'/appname_hd.json'

    with open(jsonfile) as json_file:
        data = json.load(json_file)
        return data

def loadXmlDescription(isHd):
    cur_path = common.getLastDir()+"/appname"
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

def enableShowVersionUpdate(filePath,enbale):
# <!--  <version_whats_new>Fixed a bug.</version_whats_new> -->
    f = open(filePath, 'r')
    strFile = f.read()

    if enbale:
        # 打开 version_whats_new
      
            strFile = strFile.replace("<!--  <version_whats_new>", "<version_whats_new>")
            strFile = strFile.replace("</version_whats_new> -->", "</version_whats_new>")
    else:
        # xml注释version_whats_new
        strHead = "<!--  <version_whats_new>"
        idx = strFile.find(strHead)
        if idx<0:
            strFile = strFile.replace("<version_whats_new>","<!--  <version_whats_new>")
            strFile = strFile.replace("</version_whats_new>","</version_whats_new> -->")
 
    f.close()
    saveString2File(strFile, filePath)

def getScreenshotFileName(device,language,idx): 
    return language+"_"+device+"_"+str(idx+1)+".jpg";

def getScreenshotFullFilePath(isHd,device,language,idx): 
    strDir_itmsp = "app.itmsp"
    if isHd:
        strDir_itmsp = "app_pad.itmsp"
    strDirRootTo = "../appstore/ios/"+strDir_itmsp
    strFileTo = strDirRootTo+"/"+getScreenshotFileName(device,language,idx)
    return strFileTo;

def copy_one_screenshot(isHd,device,language,idx):
    strDirHorV = "竖屏"
    if isHd:
        strDirHorV = "横屏" 

    strDirRootFrom = "../../../../ProjectIcon/pintu/icon_pintu_plant/screenshot"
    strFileFrom = strDirRootFrom+"/"+strDirHorV+"/"+language+"/"+device+"/"+str(idx+1)+".jpg";
 
    strFileTo = getScreenshotFullFilePath(isHd,device,language,idx)

    if os.path.isfile(strFileFrom):
        shutil.copyfile(strFileFrom,strFileTo)

def copy_screenshots():
    total = 5
    list_device = ["ipadpro", "iphone"]
    list_language = ["cn", "en"]
    list_hd = [False, True]
    
    for device in list_device:
        for language in list_language:
            for ishd in list_hd:
                for i in range(0, total):
                    copy_one_screenshot(ishd,device,language,i) 

# /*
# <software_screenshot display_target="iOS-5.5-in" position="1">
#                                   <file_name>iphone_1.jpg</file_name>
#                                   <size>263616</size>
#                                   <checksum type="md5">dc695d677a5c33392bc88ba4eb9d719f</checksum>
#                                </software_screenshot> 
#                                */
def getXmlStringOneScreenshot(isHd,device,language,idx):  
    filePath = getScreenshotFullFilePath(isHd,device,language,idx)
    strRet = "<software_screenshot display_target=\""+getAppStoreScreenshotDeviceName(device)+"\" position=\""+str(idx+1)+"\"> <file_name>"+getScreenshotFileName(device,language,idx)+"</file_name> <size>"+str(common.get_FileSize(filePath))+"</size> <checksum type=\"md5\">"+common.get_MD5_checksum_file(filePath)+"</checksum> </software_screenshot>"            
    return strRet

def getXmlStringScreenshots(isHd):
    total = 5
    list_device = ["ipadpro", "iphone"]
    list_language = ["cn", "en"] 
    strRet = " "

    for language in list_language:
        for device in list_device:
            for i in range(0, total):
                strRet+="\n"+getXmlStringOneScreenshot(isHd,device,language,i)
    return strRet

def getAppStoreScreenshotDeviceName(device):
    strRet = "iOS-iPad-Pro"
    if device=="ipadpro":
        strRet = "iOS-iPad-Pro"
    if device=="iphone":
        strRet = "iOS-5.5-in"
    return strRet

def updateAppstore(isHd):
    
   
    rootConfig = "../"
    strHD = "HD"

    metadata_ios = rootConfig + "appstore/ios/app.itmsp/metadata.xml" 

    if isHd:
        metadata_ios = rootConfig + "appstore/ios/app_pad.itmsp/metadata.xml" 

    xmlRoot = loadXmlDescription(isHd) 
    # loadJson
    data = loadJson(isHd)
    APP_NAME_CN_ANDROID = data["APP_NAME_CN_ANDROID"]
    APPSTORE_VERSION_UPDATE = data["APPSTORE_VERSION_UPDATE"]
    APPSTORE_TITLE = data["APPSTORE_TITLE"]
    APPSTORE_SUBTITLE = data["APPSTORE_SUBTITLE"]
    APPSTORE_PROMOTION = data["APPSTORE_PROMOTION"]
    # APPSTORE_DESCRIPTION = data["APPSTORE_DESCRIPTION"]
    APPSTORE_KEYWORD = data["APPSTORE_KEYWORD"]
    APPVERSION_IOS = data["APPVERSION_IOS"]
    software_url = data["software_url"]
    privacy_url = data["privacy_url"]
    support_url = data["support_url"]
    sku_app = data["sku_app"]

 
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


# <!--  <version_whats_new>Fixed a bug.</version_whats_new> -->
# 版本更新说明 
    key = "version_whats_new"
    jsonData = APPSTORE_VERSION_UPDATE
    replaceXmlKey(metadata_ios,"en-US",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"zh-Hans",key,jsonData["cn"])
    replaceXmlKey(metadata_ios,"en-CA",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"en-AU",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"en-GB",key,jsonData["en"])

    if APPVERSION_IOS=="1.0.0":
        enableShowVersionUpdate(metadata_ios,False)
    else:
        enableShowVersionUpdate(metadata_ios,True) 

    # APPSTORE_TITLE
    key = "title"
    jsonData = APPSTORE_TITLE
    replaceXmlKey(metadata_ios,"en-US",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"zh-Hans",key,jsonData["cn"])
    replaceXmlKey(metadata_ios,"en-CA",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"en-AU",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"en-GB",key,jsonData["en"])
 
    # APPSTORE_TITLE
    key = "subtitle"
    jsonData = APPSTORE_SUBTITLE
    replaceXmlKey(metadata_ios,"en-US",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"zh-Hans",key,jsonData["cn"])
    replaceXmlKey(metadata_ios,"en-CA",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"en-AU",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"en-GB",key,jsonData["en"])
 
  # APPSTORE_PROMOTION
    key = "promotional_text"
    jsonData = APPSTORE_PROMOTION
    replaceXmlKey(metadata_ios,"en-US",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"zh-Hans",key,jsonData["cn"])
    replaceXmlKey(metadata_ios,"en-CA",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"en-AU",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"en-GB",key,jsonData["en"])

     # APPSTORE_DESCRIPTION
    key = "description"
    # jsonData = APPSTORE_DESCRIPTION
    desc_cn = getXmlDescriptionText(xmlRoot,"cn")
    desc_en = getXmlDescriptionText(xmlRoot,"en")
    replaceXmlKey(metadata_ios,"en-US",key,desc_en)
    replaceXmlKey(metadata_ios,"zh-Hans",key,desc_cn)
    replaceXmlKey(metadata_ios,"en-CA",key,desc_en)
    replaceXmlKey(metadata_ios,"en-AU",key,desc_en)
    replaceXmlKey(metadata_ios,"en-GB",key,desc_en)
 
    # APPSTORE_KEYWORD
    key = "keyword"
    jsonData = APPSTORE_KEYWORD
    replaceXmlKey(metadata_ios,"en-US",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"zh-Hans",key,jsonData["cn"])
    replaceXmlKey(metadata_ios,"en-CA",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"en-AU",key,jsonData["en"])
    replaceXmlKey(metadata_ios,"en-GB",key,jsonData["en"])
 
    # software_url
    key = "software_url"
    jsonData = software_url
    replaceXmlKey(metadata_ios,"en-US",key,jsonData)
    replaceXmlKey(metadata_ios,"zh-Hans",key,jsonData)
    replaceXmlKey(metadata_ios,"en-CA",key,jsonData)
    replaceXmlKey(metadata_ios,"en-AU",key,jsonData)
    replaceXmlKey(metadata_ios,"en-GB",key,jsonData)

       # support_url
    key = "support_url"
    jsonData = support_url
    replaceXmlKey(metadata_ios,"en-US",key,jsonData)
    replaceXmlKey(metadata_ios,"zh-Hans",key,jsonData)
    replaceXmlKey(metadata_ios,"en-CA",key,jsonData)
    replaceXmlKey(metadata_ios,"en-AU",key,jsonData)
    replaceXmlKey(metadata_ios,"en-GB",key,jsonData)

       # privacy_url
    key = "privacy_url"
    jsonData = privacy_url
    replaceXmlKey(metadata_ios,"en-US",key,jsonData)
    replaceXmlKey(metadata_ios,"zh-Hans",key,jsonData)
    replaceXmlKey(metadata_ios,"en-CA",key,jsonData)
    replaceXmlKey(metadata_ios,"en-AU",key,jsonData)
    replaceXmlKey(metadata_ios,"en-GB",key,jsonData)



# 主函数的实现
if __name__ == "__main__":
    # 设置为utf8编码
    reload(sys)
    sys.setdefaultencoding("utf-8")

    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    print "脚本名：", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "参数", i, sys.argv[i]
    
    copy_screenshots()
    print getXmlStringScreenshots(True)

    updateAppstore(False)
    updateAppstore(True)

    print "appname sucess"
