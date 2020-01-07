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

# include appinfo.py
# sys.path.append('./common')
import appname
import appchannel
import source
import apk_build

sys.path.append('./common')
import common 

 
    

UNITYPATH="E:/Unity/2019.2.0f1/Editor/Unity.exe"
# PROJECT_PATH="F:\sourcecode\unity\product\kidsgame\kidsgameUnity"
PROJECT_PATH="F:/sourcecode/unity/product/kidsgame/kidsgameUnity"
companyName="moonma"
productName="kidsgame"
platform="0"
outPath="F:\sourcecode\unity\product\kidsgame\project_android_output_cmd"
arg0="参数谁便定义"
# E:\Program Files\Unity_All\2019.1.2f1\2019.1.2f1\Editor\Unity.exe -quit -batchmode -projectPath F:\sourcecode\unity\product\kidsgame\kidsgameUnity -executeMethod  ProjectBuild.BuildAndroid -buildTarget Android -exportPackage project_android_output_cmd kidsgame
# subprocess.call(UNITYPATH+" -quit "+" -batchmode "+" -projectPath "+PROJECT_PATH+" -executeMethod  ProjectBuild.BuildAndroid "+companyName+" "+productName+" "+platform+" "+outPath+" "+arg0)

# Unity.exe -quit -batchmode -projectPath F:\sourcecode\unity\product\kidsgame\kidsgameUnity -executeMethod  BuildPlayer.PerformAndroidUCBuild
#  os.system("adb connect "+myaddr)
print "unity_build  start"
os.system(UNITYPATH+" -quit "+" -batchmode "+" -projectPath "+PROJECT_PATH+" -executeMethod  BuildPlayer.PerformAndroidBuild")
print "unity_build  end"
