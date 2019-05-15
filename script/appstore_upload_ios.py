#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time,  datetime
import sys

#include appinfo.py
sys.path.append('./common')
import common
import source

##获取脚本文件的当前路径
def cur_file_dir():
    #获取脚本路径
    path = sys.path[0]
    return path
  
# http://help.apple.com/itc/appsspec/#/itc6e4198248
# Transporter 上传工具
# https://help.apple.com/itc/transporteruserguide
#主函数的实现
if  __name__ =="__main__":
    
    print "脚本名：", sys.argv[0] 
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1,count):
        print "参数", i, sys.argv[i]
        if i==1:
            cmdPath = sys.argv[i]
    
    common.SetCmdPath(cmdPath)
    gameName = common.getGameName()
    gameType = common.getGameType()
    
    print gameType 
    print gameName 

    isHD = False 
    if count>2:
        argvHD = sys.argv[2]
        if argvHD=="hd":
            isHD = True 
    strFile = "app.itmsp"
    if isHD:
        strFile = "app_pad.itmsp"
    
    if common.isWindowsSystem():
        strCmd = " "
    else:
        # ／"/Applications/Xcode.app/Contents/Applications/Application\ Loader.app/Contents/itms/bin/iTMSTransporter -m upload -u chyfemail163@163.com -p ayww-hcnh-uaau-lsgh -f ./appstore/ios/app.itmsp -v eXtreme""/Applications/Xcode.app/Contents/Applications/Application\ Loader.app/Contents/itms/bin/iTMSTransporter -m upload -u chyfemail163@163.com -p ayww-hcnh-uaau-lsgh -f ./appstore/ios/app.itmsp -v eXtreme"
        strCmd = "/Applications/Xcode.app/Contents/Applications/Application\ Loader.app/Contents/itms/bin/iTMSTransporter -m upload -u "+source.APPSTORE_USER+" -p "+source.APPSTORE_PASSWORD+"  -v eXtreme -f "+common.GetProjectConfigApp()+ "/appstore/ios/"+strFile
    
    os.system(strCmd) 
        
    print "appstore_upload_ios sucess"






