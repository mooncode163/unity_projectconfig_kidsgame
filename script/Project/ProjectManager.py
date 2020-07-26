#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path
import time
import datetime
import json

#include common.py
# sys.path.append('./common')

o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径
from Common import common
from Common import config
from Common import source
from Common import adconfig  
from Common.FileUtil import FileUtil 

from xml.dom.minidom import parse
 
 
class ProjectManager():   
    #构造函数
    def __init__(self): 
        name =""
 

    def CopyProjectConfig(self): 
        listname ={"default","script"}
        for name in listname:
            src = common.GetDirProductCommon()+"/ProjectConfig/"+name
            dst = common.GetProjectConfig()+"/"+name
            FileUtil.CopyDir(src,dst)
 

    def SaveProjectConfig(self): 
        listname ={"default","script"}
        for name in listname:
            src = common.GetProjectConfig()+"/"+name
            dst = common.GetDirProductCommon()+"/ProjectConfig/"+name
            print(src)
            print(dst)
            FileUtil.CopyDir(src,dst)

    def CopyCommonScript(self): 
        listname ={"AppBase","Common"}
        for name in listname:
            src = common.GetDirProductCommon()+"/ProjectUnity/Assets/Script/"+name
            dst = common.GetRootUnityAssets()+"/Script/"+name
            FileUtil.CopyDir(src,dst) 

    def SaveCommonScript(self): 
        listname ={"AppBase","Common"}
        for name in listname:
            src = common.GetRootUnityAssets()+"/Script/"+name
            dst = common.GetDirProductCommon()+"/ProjectUnity/Assets/Script/"+name
            print(src)
            print(dst)
            FileUtil.CopyDir(src,dst)  
            

# 主函数的实现
if __name__ == "__main__":
    # 设置为utf8编码
    # reload(sys)
    # sys.setdefaultencoding("utf-8")
    is_auto_plus_version = False
    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1,count):
        print("参数", i, sys.argv[i])
        if i==1:
            cmdPath = sys.argv[i] 

    common.SetCmdPath(cmdPath)
    
    p = ProjectManager()
    arg = sys.argv[2] 
    if arg == "CopyProjectConfig":
        p.CopyProjectConfig() 
    if arg == "SaveProjectConfig":
        p.SaveProjectConfig()
    if arg == "CopyCommonScript":
        p.CopyCommonScript()
    if arg == "SaveCommonScript":
        p.SaveCommonScript()

    print("ProjectManager sucess arg=",arg)
