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

#主函数的实现
if  __name__ =="__main__":
    
    #入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    print "脚本名：", sys.argv[0]
    # for i in range(1, len(sys.argv)):
    #     print "参数", i, sys.argv[i]


    # rootDir ="/Users/jaykie/sourcecode/cocos2dx/product/game/ertong"
    rootAndroidStudio ="../../../../project_android/kidsgame"
    rootiOSXcode ="../../../../project_ios/kidsgame_device"
    rootiOSXcodeEmu ="../../../../project_ios/kidsgame"
    rootCode ="../../../../ios_code_unity_moon"
    
  
 
    # 
    targetDir = rootiOSXcode+"/Classes"
    common.copyFiles(rootCode,   targetDir)

    targetDir = rootiOSXcodeEmu+"/Classes"
    common.copyFiles(rootCode,   targetDir)

    print "copy_ios_code sucess"
