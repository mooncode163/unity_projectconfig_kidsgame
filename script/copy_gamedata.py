#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path
import time,  datetime
 

o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径  
from common import common
from common import source 

def getGameResName():
    name = common.getGameName()
    idx = name.rfind('_')
    s_len=len(name)
    game = name[idx+1:s_len]
    return game

def CopyConfigDataToAndroid(): 
    dir1 = common.GetConfigDataDir()
    dir2 = common.GetRootDirAndroidAsset()+ "/ConfigData"
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    # print "CopyConfigDataToAndroid:dir1=",dir1," dir2=",dir2
    shutil.copytree(dir1,dir2)

def DoCopy():
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
        gameResRoot = gameResCommonRoot

    gameDataCommonRoot = common.GetResourceDataRoot()+"/GameDataCommon"
    gameDataRoot = common.GetResourceDataRoot()+"/"+gameType+"/"+gameName+"/GameData"

    streamingAssetsUnity = common.GetRootProjectUnity()+"/Assets/StreamingAssets"
    rootAndroidStudio =common.GetRootDirAndroidStudio()
    rootiOSXcode =common.GetRootDirXcode()

    # copy GameRes 游戏图片等资源
    dirname = "GameRes"

    # unity editor 
    dir1 = gameResRoot
    dir2 = streamingAssetsUnity+"/"+dirname
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)

    # ios
    # dir2 = rootiOSXcode+"/Data/Raw/"+dirname
    # flag = os.path.exists(dir2)
    # if flag:
    #     shutil.rmtree(dir2)
    # shutil.copytree(dir1,dir2)

   # android asset
    dir2 = rootAndroidStudio+"/src/main/assets/"+dirname
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)


 # copy GameData 游戏配置等数据 
    dirname = "GameData"

    # unity editor 
    dir1 = gameDataRoot
    dir2 = streamingAssetsUnity+"/"+dirname
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)

    # ios
    # dir2 = rootiOSXcode+"/Data/Raw/"+dirname
    # flag = os.path.exists(dir2)
    # if flag:
    #     shutil.rmtree(dir2)
    # shutil.copytree(dir1,dir2)

   # android asset
    dir2 = rootAndroidStudio+"/src/main/assets/"+dirname
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)


    dirname = "GameData/common"

    # unity editor 
    dir1 = gameDataCommonRoot
    dir2 = streamingAssetsUnity+"/"+dirname
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)

    # ios
    # dir2 = rootiOSXcode+"/Data/Raw/"+dirname
    # flag = os.path.exists(dir2)
    # if flag:
    #     shutil.rmtree(dir2)
    # shutil.copytree(dir1,dir2)

   # android asset
    dir2 = rootAndroidStudio+"/src/main/assets/"+dirname
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)

    CopyConfigDataToAndroid()

#主函数的实现
if  __name__ =="__main__":
    
    # 设置为utf8编码
    # reload(sys)
    # sys.setdefaultencoding("utf-8")
 

    #入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1,count):
        print ("参数", i, sys.argv[i])
        if i==1:
            cmdPath = sys.argv[i]
    
    common.SetCmdPath(cmdPath)
    DoCopy()

    print ("copy_gamedata sucess")
