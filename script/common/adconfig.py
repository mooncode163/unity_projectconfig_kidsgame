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

import common

global jsonRoot
global jsonPlat

def GetConfigFile(osSrc, isHd):
    dir = common.GetAdConfigDir()
    if isHd:
        filepath = dir + "/ad_config_" + osSrc + "_hd"+".json"
    else:
        filepath = dir + "/ad_config_" + osSrc+".json"
    return filepath


def LoadJson(osSrc, isHd):
    global jsonRoot
    global jsonPlat
    jsonfile = GetConfigFile(osSrc, isHd)
    with open(jsonfile) as json_file:
        jsonRoot = json.load(json_file)
        jsonPlat = jsonRoot["platform"]

def GetAppId(src, osSrc, isHd):
    LoadJson(osSrc, isHd)
    appid = "0"
    for jsontmp in jsonPlat:
        if jsontmp["source"] == src:
            appid = jsontmp["appid"]
    return appid

def GetAppKey(src, osSrc, isHd):
    LoadJson(osSrc, isHd)
    appkey = "0"
    for jsontmp in jsonPlat:
        if jsontmp["source"] == src:
            appkey = jsontmp["appkey"]
    return appkey
