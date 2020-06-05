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

  
def getGameResName():
    name = common.getGameName()
    idx = name.rfind('_')
    s_len=len(name)
    game = name[idx+1:s_len]
    return game

#主函数的实现
if  __name__ =="__main__":
    
    #入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1,count):
        print("参数", i, sys.argv[i])
        if i==1:
            cmdPath = sys.argv[i]
    
    common.SetCmdPath(cmdPath)

    gameName = common.getGameName()
    gameType = common.getGameType()
    print(gameName)
    print(gameType)

    resDataName = common.getGameName()#sys.argv[1]
    gameResName = getGameResName()

    gameResCommonRoot = common.GetResourceDataRoot()+"/GameResCommon"+"/"+gameResName
    gameResRoot = common.GetResourceDataRoot()+"/"+gameType+"/"+gameName+"/GameRes"
    flag = os.path.exists(gameResRoot)
    if not flag:
        #目录不存在的话到gamerescommon里copy
        gameResRoot = gameResCommonRoot;

    gameDataRoot = common.GetResourceDataRoot()+"/"+gameType+"/"+gameName+"/GameData"

    streamingAssetsUnity = common.GetRootProjectUnity()+"/Assets/StreamingAssets"
    rootAndroidStudio = common.GetRootDirAndroidStudio()
    rootiOSXcode =common.GetRootDirXcode()

    
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


    print("clean_screenshot sucess")
