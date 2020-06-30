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

o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径 
from common import source 
from common import common

jsonCommonRoot = ""
jsonRoot = ""
jsonShare = ""
jsonPlat = ""
 

def GetConfigCommonFile(dir): 
    filepath = dir + "/config_common.json"
    return filepath


def GetConfigFile(osSrc, isHd):
    dir = common.GetConfigDir()
    if isHd:
        filepath = dir + "/config_" + osSrc + "_hd" + ".json"
    else:
        filepath = dir + "/config_" + osSrc + ".json"
    return filepath


def LoadCommonJson(dir):
    global jsonCommonRoot 
    jsonfile = GetConfigCommonFile(dir)
    with open(jsonfile) as json_file:
        jsonCommonRoot = json.load(json_file) 


def LoadJson(osSrc, isHd):
    global jsonRoot
    global jsonShare
    global jsonPlat
     
    jsonfile = GetConfigFile(osSrc, isHd)
    with open(jsonfile) as json_file:
        jsonRoot = json.load(json_file)
        jsonShare = jsonRoot["SHARE"] 
        jsonPlat = jsonShare["platform"]

def GetConfigAppType(dir):
    LoadCommonJson(dir) 
    return jsonCommonRoot["APP_TYPE"]
def GetConfigAppName(dir):
    LoadCommonJson(dir) 
    return jsonCommonRoot["APP_NAME_KEYWORD"]

def GetShareAppId(src, osSrc, isHd):
    LoadJson(osSrc, isHd)
    appid = "0"
    for jsontmp in jsonPlat:
        if jsontmp["source"] == src:
            appid = jsontmp["id"]
    return appid


def GetShareAppKey(src, osSrc, isHd):
    LoadJson(osSrc, isHd)
    appkey = "0"
    for jsontmp in jsonPlat:
        if jsontmp["source"] == src:
            appkey = jsontmp["key"]
    return appkey



# qq: appID：100424468 1、tencent100424468 
# 2、QQ05fc5b14	QQ05fc5b14为100424468转十六进制而来，因不足8位向前补0，然后加"QQ"前缀
def QQEncodeAppID(appid):
    ret ="QQ" 
    str_hex = hex(int(appid))
    len_hex = len(str_hex)

    # 去除 0x 前缀
    str_hex = str_hex[2:len_hex]

    len_hex = len(str_hex)
    if len_hex<8:
        for i in range(0,8-len_hex):
            ret+="0" 
    
    ret+=str_hex
    return ret
# CFBundleURLSchemes
def XcodeUrlScheme(src, appid, idx):
    ret = appid
    if src == source.WEIBO:
        ret = "wb" + appid
    if src == source.WEIXIN or src == source.WEIXINFRIEND:
        ret = appid
    if src == source.QQ or src == source.QQZONE:
        if idx ==0:
            ret = QQEncodeAppID(appid)
        if idx ==1:
            ret = "tencent"+appid


    if ret=="0" or len(ret)==0:
        # xcode UrlScheme 首字母不能为数字
        ret = "wx0"

    return ret 
 
