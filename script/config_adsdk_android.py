#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path

# sys.path.append('./common')
# import common

o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径  
from common import common

# sys.path.append('./ziputils')
from common import ziputils 
 


def GetRootDirLibs():
    return common.GetRootDirAndroidStudio() + "/libs"

def GetRootDirAdSdk():
    return GetRootDirLibs() + "/ad_lib"

def GetDirAdSdk(src):
    return GetRootDirAdSdk() + "/"+src
  
def GetZipFileAdSdk(src):
    return GetDirAdSdk(src) +".zip"

def GetRootDirAdSdkJavaCode():
    return common.GetRootDirAndroidStudio() + "/src/main/java/com/moonma/common/adkit/platform"
def GetDirAdSdkJavaCode(src):
    return GetRootDirAdSdkJavaCode() + "/"+src
def GetZipFileAdSdkJavaCode(src,noad):
    ret =""
    if noad:
        ret = GetDirAdSdkJavaCode(src) +"_noad.zip"
    else:
        ret = GetDirAdSdkJavaCode(src) +".zip"
    return ret


# 
def DeleteMACOSX(root_dir):
    macosx_dir = root_dir+"/__MACOSX"
    flag = os.path.exists(macosx_dir)
    if flag:
        shutil.rmtree(macosx_dir)

def SetAdSdk(src,enable):
    SetAdSdkLib(src,enable)
    SetAdSdkJavaCode(src,not enable)


def GetDirShareSdkLib():
    return common.GetRootDirAndroidStudio() + "/libs/share"

def SetShareSdk(enable): 
    # lib
    dir_lib = GetDirShareSdkLib()
    file_zip = common.GetRootDirAndroidStudio() + "/libs/share.zip"
    rootdir_lib = common.GetRootDirAndroidStudio() + "/libs"

    flag = os.path.exists(dir_lib)
    if flag:
        shutil.rmtree(dir_lib) 

    if enable:
        flag = os.path.exists(file_zip)
        if flag:
            ziputils.un_zip(file_zip,rootdir_lib)

    DeleteMACOSX(rootdir_lib)

    # F:\sourcecode\unity\product\kidsgame\project_android\kidsgame\src\main\java\com\moonma\common\share
    # code
    dir_code = common.GetRootDirAndroidStudio() + "/src/main/java/com/moonma/common/share"
    file_zip_enable = common.GetRootDirAndroidStudio() + "/src/main/java/com/moonma/common/share.zip"
    file_zip_disable = common.GetRootDirAndroidStudio() + "/src/main/java/com/moonma/common/share_disable.zip"
    rootdir_code = common.GetRootDirAndroidStudio() + "/src/main/java/com/moonma/common"

    flag = os.path.exists(dir_code)
    if flag:
        shutil.rmtree(dir_code) 

    file_zip = file_zip_disable
    if enable:
        file_zip = file_zip_enable 

    flag = os.path.exists(file_zip)
    if flag:
        ziputils.un_zip(file_zip,rootdir_code)

    DeleteMACOSX(rootdir_code)

 

# 备份游戏代码到CodeZip  压缩zip
def SetAdSdkLib(src,enable):
    rootdir_ad = GetRootDirAdSdk()
    file_zip = GetZipFileAdSdk(src)   
    

    print (rootdir_ad)
    print(file_zip)

    dir_adsdk = GetDirAdSdk(src)
    flag = os.path.exists(dir_adsdk)
 
    if flag:
        shutil.rmtree(dir_adsdk) 

    if enable:
        flag = os.path.exists(file_zip)
        if flag:
            ziputils.un_zip(file_zip,rootdir_ad) 

    DeleteMACOSX(rootdir_ad)


def SetAdSdkJavaCode(src,noad):
    rootdir_ad = GetRootDirAdSdkJavaCode()
    file_zip = GetZipFileAdSdkJavaCode(src,noad)   
    dir_adsdk = GetDirAdSdkJavaCode(src)
    print (dir_adsdk)
    print(file_zip)

    flag = os.path.exists(dir_adsdk)
    if flag:
        shutil.rmtree(dir_adsdk)  
    
    dir_adsdk_noad = dir_adsdk+"_noad"
    flag = os.path.exists(dir_adsdk_noad)
    if flag:
        shutil.rmtree(dir_adsdk_noad)
        

    ziputils.un_zip(file_zip,rootdir_ad)

    DeleteMACOSX(rootdir_ad)
