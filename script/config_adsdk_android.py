#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path

sys.path.append('./common')
import common


sys.path.append('./ziputils')
import ziputils
 


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

# 备份游戏代码到CodeZip  压缩zip
def SetAdSdkLib(src,enable):
    rootdir_ad = GetRootDirAdSdk()
    file_zip = GetZipFileAdSdk(src)   

    print rootdir_ad
    print file_zip

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
    print dir_adsdk
    print file_zip

    flag = os.path.exists(dir_adsdk)
    if flag:
        shutil.rmtree(dir_adsdk)  
    
    dir_adsdk_noad = dir_adsdk+"_noad"
    flag = os.path.exists(dir_adsdk_noad)
    if flag:
        shutil.rmtree(dir_adsdk_noad)
        

    ziputils.un_zip(file_zip,rootdir_ad)

    DeleteMACOSX(rootdir_ad)
