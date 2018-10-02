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

    reousceDataRoot = "../../../../ResourceData"+"/"+gameType
    reousceUnity = "../../../../KidsGameUnity/Assets/Resources"
    # resoucedata
    dirname = "Resources"
    dir1 = reousceDataRoot+"/"+resDataName+"/"+dirname
    dir2 = reousceUnity
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)



    print "copy_resource sucess"
