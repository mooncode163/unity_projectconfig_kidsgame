#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path
import time,  datetime

#include common.py
sys.path.append('./common')
import common

def getGameName():
    path = common.getLastDir()
    idx = path.rfind('/')
    s_len=len(path)
    game = path[idx+1:s_len]
    return game

def getGameType():
    name = getGameName()
    idx = name.find('_')
    s_len=len(name)
    game = name[0:idx]
    return game

def getGameResName():
    name = getGameName()
    idx = name.rfind('_')
    s_len=len(name)
    game = name[idx+1:s_len]
    return game

#主函数的实现
if  __name__ =="__main__":
    
    #入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    print "脚本名：", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "参数", i, sys.argv[i]

    gameName = getGameName()
    gameType = getGameType()
    print gameName
    print gameType

    resDataName = getGameName()#sys.argv[1]
    gameResName = getGameResName()

    gameResCommonRoot = "../../../../ResourceData"+"/GameResCommon"+"/"+gameResName
    gameResRoot = "../../../../ResourceData"+"/"+gameType+"/"+gameName+"/GameRes"
    flag = os.path.exists(gameResRoot)
    if not flag:
        #目录不存在的话到gamerescommon里copy
        gameResRoot = gameResCommonRoot;

    gameDataRoot = "../../../../ResourceData"+"/"+gameType+"/"+gameName+"/GameData"

    streamingAssetsUnity = "../../../../KidsGameUnity/Assets/StreamingAssets"
    rootAndroidStudio ="../../../../project_android/kidsgame"
    rootiOSXcode ="../../../../project_ios/kidsgame_device"

    
 # copy GameData 游戏配置等数据 
    dirname = "GameData/screenshot"
    # ios
    dir2 = rootiOSXcode+"/Data/Raw/"+dirname
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2) 

    dirname = "GameData/screenshot"
   # android asset
    dir2 = rootAndroidStudio+"/src/main/assets/"+dirname
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2) 


    print "clean_screenshot sucess"
