#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time
import datetime
import sys
import subprocess

# include AppInfo.py
# sys.path.append('./common')
import AppInfo
import appchannel
import source
import apk_build

sys.path.append('./common')
import common 

# 主函数的实现
if __name__ == "__main__":

    # 设置为utf8编码
    # reload(sys)
    # sys.setdefaultencoding("utf-8")
    is_auto_plus_version = False
    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    stros = ""
    for i in range(1,count):
        print("参数", i, sys.argv[i])
        if i==1:
            cmdPath = sys.argv[i]
        if i==2:
            stros = sys.argv[i] 

    common.SetCmdPath(cmdPath)
    # 0f6 2f1
    UNITYPATH=""
    if common.isWindowsSystem():
        UNITYPATH="E:/Unity/"+source.UNITY_VERSION_WIN+"/Editor/Unity.exe"
        if not os.path.exists(UNITYPATH):
            # 阿里云添加环境变量 C:\Program Files\Unity\Hub\Editor\2019.3.2f1\Editor
            # UNITYPATH="C:/Program Files/Unity/Hub/Editor/"+source.UNITY_VERSION+"/Editor/Unity.exe"
            UNITYPATH= "Unity.exe"
    else:
        UNITYPATH="/Applications/Unity/Hub/Editor/"+source.UNITY_VERSION_MAC+"/Unity.app/Contents/MacOS/Unity" 


    
    PROJECT_PATH= common.GetRootProjectUnity()

    
    methond = ""
    if stros == source.ANDROID:
        methond = "BuildPlayer.PerformAndroidBuild"
    if stros == source.IOS:
        methond = "BuildPlayer.PerformiPhoneBuild"

    print("unity_build  start")
    cmd = UNITYPATH+" -quit "+" -batchmode "+" -projectPath "+PROJECT_PATH+" -executeMethod  "+methond
    # ps = subprocess.Popen(cmd)
    # ps.wait()#让程序阻塞
    os.system(cmd)
    print("unity_build  end")

    


# PROJECT_PATH="F:\sourcecode\unity\product\kidsgame\kidsgameUnity"

# companyName="moonma"
# productName="kidsgame"
# platform="0"
# outPath="F:\sourcecode\unity\product\kidsgame\project_android_output_cmd"
# arg0="参数谁便定义"
# E:\Program Files\Unity_All\2019.1.2f1\2019.1.2f1\Editor\Unity.exe -quit -batchmode -projectPath F:\sourcecode\unity\product\kidsgame\kidsgameUnity -executeMethod  ProjectBuild.BuildAndroid -buildTarget Android -exportPackage project_android_output_cmd kidsgame
# subprocess.call(UNITYPATH+" -quit "+" -batchmode "+" -projectPath "+PROJECT_PATH+" -executeMethod  ProjectBuild.BuildAndroid "+companyName+" "+productName+" "+platform+" "+outPath+" "+arg0)

# Unity.exe -quit -batchmode -projectPath F:\sourcecode\unity\product\kidsgame\kidsgameUnity -executeMethod  BuildPlayer.PerformAndroidUCBuild
#  os.system("adb connect "+myaddr)

