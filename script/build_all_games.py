#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time
import datetime
import sys


sys.path.append('./common')
import common


def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

def ScanDir(sourceDir,channel,dir2):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file) 
        if os.path.isdir(sourceFile):
            # python 里无法直接执行cd目录，想要用chdir改变当前的工作目录
            if common.isWindowsSystem():
                os.chdir(sourceFile+"/cmd_win")
                os.system("echo.| copy_cmd.bat")
            else:
                dirapp = dir2+"/"+file+"/cmd_mac" 
                if common.IsVMWare():
                    dirapp = "/Volumes/VMware\\ Shared\\ Folders/"+dir2+"/"+file+"/cmd_mac"
                    # os.system("cd /Volumes/VMware\\ Shared\\ Folders")
                    
                    # cmdPath="/Volumes/VMware Shared Folders/"+cmdPath
                
                    os.system("cd "+dirapp)
                else:
                    os.chdir(dirapp)
                
                os.system("sh "+"./copy_cmd")
                # os.system("sh "+dirapp+"/build_all_ios")

            print(file)
            # update_appname build_huawei
            
            if channel=="huawei":
                os.system("echo.| call build_huawei.bat")
            if channel=="gp":
                os.system("echo.| call build_gp.bat")
            if channel=="android":
                os.system("echo.| call build_all_android.bat")
            if channel=="ios":
                if common.isWindowsSystem():
                    os.system("echo.| build_all_ios.bat")
                # else:
                    # os.system("build_all_ios")
                    # os.system("cd "+dirapp)
                    os.system("sh "+"./build_all_ios")
            
            if channel=="ios_copy_cmd":
                print("ios_copy_cmd")

            

    
# 主函数的实现
if __name__ == "__main__":

     # 设置为utf8编码
    # reload(sys)
    # sys.setdefaultencoding("utf-8")

    print ("脚本名：", sys.argv[0])
    cmdPath = cur_file_dir()
    count = len(sys.argv)
    channel = ""

    for i in range(1, count):
        print ("参数", i, sys.argv[i])
        if i == 1:
            cmdPath = sys.argv[i]

        if i == 2:
            channel = sys.argv[i] 

    dir2 = cmdPath
    if common.IsVMWare():
        cmdPath="/Volumes/VMware Shared Folders/"+cmdPath

    print ("dir2="+dir2)


    ScanDir(cmdPath,channel,dir2)

    print  ("build_huawei sucess")
