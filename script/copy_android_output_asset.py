#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path
import time,  datetime
import json
 

o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径  
from common import common
from common import source 

import copy_gamedata

def CopyConfigDataToAndroid(): 
    dir1 = common.GetConfigDataDir()
    dir2 = common.GetRootDirAndroidAsset()+ "/ConfigData"
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    # print(CopyConfigDataToAndroid:dir1=",dir1," dir2=",dir2
    shutil.copytree(dir1,dir2)

def LoadJsonAndroidAssetConfigCommon():  
    jsonfile = common.GetRootDirAndroidAsset()+"/ConfigData/config/config_common.json"
    with  open(jsonfile, 'rb') as json_file:
        data = json.load(json_file)
        return data


# 复制从unity打包输出的assets目录
#主函数的实现
if  __name__ =="__main__":
    
    #入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1,count):
        print("参数", i, sys.argv[i])
        if i==1:
            cmdPath = sys.argv[i]

    cmdPath = common.getLastDirofDir(cmdPath)
    common.SetCmdPath(cmdPath)
    gameName = common.getGameName()
    gameType = common.getGameType()
    print(gameName)
    print(gameType)

    rootAndroidStudio =common.GetRootDirAndroidStudio()
 
   # android asset
    dir_asset = "/src/main/assets/bin"
    dir1 = common.GetRootDirAndroidOutput()+dir_asset
    dir2 = rootAndroidStudio+dir_asset
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)
 
    dir_asset = "/src/main/assets/baidu_tts_data"
    dir1 = common.GetRootDirAndroidOutput()+dir_asset
    dir2 = rootAndroidStudio+dir_asset
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)


    # android jniLibs
    dir_asset = "/src/main/jniLibs"
    dir1 = common.GetRootDirAndroidOutput()+dir_asset
    dir2 = rootAndroidStudio+dir_asset
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)


    filename = "/libs/unity-classes.jar"
    shutil.copy2(common.GetRootDirAndroidOutput()+filename, rootAndroidStudio+filename)

    dataJson = LoadJsonAndroidAssetConfigCommon()
    appNameAndroidAsset = dataJson["APP_NAME_KEYWORD"]
    appTypeAndroidAsset = dataJson["APP_TYPE"]
    print(appTypeAndroidAsset)
    print(appNameAndroidAsset)

    if appTypeAndroidAsset!=gameType or appNameAndroidAsset!=gameName:
        copy_gamedata.DoCopy()

    CopyConfigDataToAndroid()


  

    print("copy_android_output_asset sucess")
