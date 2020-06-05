#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time,  datetime
import sys

#include appinfo.py
# sys.path.append('./common')
import appname
import source

sys.path.append('./common')
import common
  
#主函数的实现
if  __name__ =="__main__":
    
    print ("脚本名：", sys.argv[0])
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    isHD = False

    for i in range(1,count):
        print ("参数", i, sys.argv[i])
        if i==1:
            cmdPath = sys.argv[i]

        if i==2: 
            if sys.argv[i]=="hd":
                isHD = True
     
    common.SetCmdPath(cmdPath)
    gameName = common.getGameName()
    gameType = common.getGameType() 

    # package = appname.GetPackage(source.source.SOURCE_ANDROID,isHD) 
    package = common.GetPackageAndroidFromXml()
    print package
    os.system("adb uninstall "+package)
    os.system("adb install "+common.getAndroidProjectApk()) 
        
    print "installapk sucess"






