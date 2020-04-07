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
import source
import appname
import adconfig
import config_adsdk_android
 

def UpdateXcodeProjectFile(fileProject,isHD):
    flag = os.path.exists(fileProject)
    if not flag:
        return

    package = appname.GetPackage(source.IOS,isHD) 

    # 读取xcode文件的包名
    # PRODUCT_BUNDLE_IDENTIFIER = com.moonma.xiehanzi.pad;
    strFile = common.GetFileString(fileProject)
    strHead = "PRODUCT_BUNDLE_IDENTIFIER = "
    strEnd = ";"
    idx = strFile.find(strHead)
    if idx>=0:
        idx +=len(strHead)
        strOther = strFile[idx:]
        idx = strOther.find(strEnd)
        packageold = strOther[0:idx]
        print "packageold="+packageold
        strFile = strFile.replace(packageold,package)
        common.saveString2File(strFile,fileProject)

    


    
def CopyAndroidJavaFile_Weixin(rootStudio,isHD):
    dirroot = common.GetProjectConfigApp()
    strFileFrom = dirroot+"/android/src/wxapi/WXEntryActivity.java"
    strFileTo = rootStudio+"/src/main/java/com/moonma/common/share/wxapi/WXEntryActivity.java"
    
    # loadJson
    package = appname.GetPackage(source.ANDROID,isHD)  
    # 替换包名
    f = open(strFileFrom, 'r')
    strFile = f.read()
    f.close()  

    strOut = strFile.replace("_PACKAGE_", package)
    common.saveString2File(strOut,strFileTo)
 

#主函数的实现
if  __name__ =="__main__":
    
      # 设置为utf8编码
    reload(sys)
    sys.setdefaultencoding("utf-8")
    
    #入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir() 
    count = len(sys.argv)
    for i in range(1,count):
        print "参数", i, sys.argv[i]
        if i==1:
            cmdPath = sys.argv[i] 

    common.SetCmdPath(cmdPath)
    gameName = common.getGameName()
    gameType = common.getGameType()
    print gameName
    print gameType
    # rootDir ="/Users/jaykie/sourcecode/cocos2dx/product/game/ertong"
    rootAndroidStudio = common.GetRootDirAndroidStudio()
    rootiOSXcode = common.GetRootDirXcode()
    xcodeProject = rootiOSXcode+"/Unity-iPhone.xcodeproj/project.pbxproj"
    resDataName = common.getGameName()#sys.argv[1]
    iconDirName = sys.argv[2]
    # adDirName = sys.argv[3]

    project_ios = "ios/project"
    project_android = "android/project"

    isHD = False
    if iconDirName=="iconhd":
        isHD = True
        project_ios = "ios/project_hd"
        project_android = "android/project_hd"
 
 
    # project
    iconRoot =common.GetProjectOutPutApp()
    reousceDataRoot = common.GetResourceDataRoot() 
    sourceDir = common.GetProjectConfigApp()
    # sourceAdDir = "../../../../ad_src/"+adDirName
    # adCommonDir = "../../../../../common_ad"
    # adSrcDir = adCommonDir+"/ad_src/"+adDirName
    targetDir = rootAndroidStudio+"/src/main"
     
    # resoucedata 
    # dirname = "Resources"
    # dir1 = reousceDataRoot+"/"+resDataName+"/"+dirname
    # dir2 = reousceUnity
    # flag = os.path.exists(dir2)
    # if flag:
    #     shutil.rmtree(dir2)
    # shutil.copytree(dir1,dir2)

  
    # ios icon
    #先清除unity自动生成的目录
    dir1 =common.GetProjectConfig()+"/LaunchScreenIcon_ios/Unity-iPhone"
    dir2 = rootiOSXcode + "/Unity-iPhone"
    flag = os.path.exists(dir1) and os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)

    dir1 = iconRoot+"/"+iconDirName+"/ios"
    dir2 = rootiOSXcode + "/Unity-iPhone/Images.xcassets/AppIcon.appiconset"
    flag = os.path.exists(dir1) and os.path.exists(dir2)
    if flag:
        common.coverFiles(dir1,   dir2)


    #android icon
    dir1 = iconRoot+"/"+iconDirName+"/android"
    # dir2 = sourceDir+"/res"
    dir2 = common.GetProjectConfigApp()+"/"+project_android+"/res"
    # if iconDirName=="iconhd":
    #     dir2 = "./android/project/res_hd"
    common.coverFiles(dir1,dir2)

    # 
    project = sourceDir+"/"+project_android+"/xml"
    common.coverFiles(project,   targetDir)

    project = sourceDir+"/android"+"/gradle"
    targetDir = rootAndroidStudio
    # common.coverFiles(project,   targetDir)


    
    #res android
    dir1 = sourceDir+"/"+project_android + "/res"
    # if iconDirName=="iconhd":
    targetDir = rootAndroidStudio+"/src/main"
    dir2 = targetDir+"/res"
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)

    shutil.copytree(dir1,dir2)
 

    # ios
    # appname
    dir1 = sourceDir+"/"+project_ios+"/appname"
    dir2 = rootiOSXcode+"/appname"
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)

    #info
    file1 = sourceDir + "/"+project_ios+"/info.plist"
    file2 = rootiOSXcode + "/info.plist"
    print("info.plist file1= "+file1)
    print("info.plist file2= "+file2)
    common.copyOneFile(file1,file2) 


    # win res 
    dir1 = iconRoot+"/"+iconDirName+"/microsoft"
    dir2 = common.GetRootProjectWin()+"/"+common.GetProjectName()+"/Assets"
    if os.path.exists(dir2):
        common.coverFiles(dir1,   dir2)

    # win strings 
    dir_src_string = common.GetProjectConfigApp()+"/"+source.WIN + "/project"
    if isHD:
        dir_src_string = common.GetProjectConfigApp()+"/"+source.WIN + "/project_hd"
    dir1 = dir_src_string+"/strings"
    dir2 = common.GetRootProjectWin()+"/"+common.GetProjectName()+"/strings" 
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
        shutil.copytree(dir1,dir2)
    
    

# ad src
    # dir1 = adSrcDir;
    # dir2 =  rootAndroidStudio+"/src/main/java/com/moonma/common/ad"
    # flag = os.path.exists(dir2)
    # if flag:
    #     shutil.rmtree(dir2)

    # shutil.copytree(dir1,dir2)

    CopyAndroidJavaFile_Weixin(rootAndroidStudio,isHD)

    # if not common.isWindowsSystem():
    UpdateXcodeProjectFile(xcodeProject,isHD)

    # AD LIB JAVA CODE

    appid_xiaomi = adconfig.GetAppId(source.XIAOMI,source.ANDROID,isHD)
    if "0"==appid_xiaomi:
        print "no xiaomi ad appid"
        # VUNGLE 和 XIAOMI sdk gson库 冲突
        config_adsdk_android.SetAdSdk(source.XIAOMI, False)
        # True
        config_adsdk_android.SetAdSdk(source.VUNGLE, False)
    else:
        config_adsdk_android.SetAdSdk(source.XIAOMI, False)
        config_adsdk_android.SetAdSdk(source.VUNGLE, False)
   
      
    appid_gdt = adconfig.GetAppId(source.GDT,source.ANDROID,isHD)
    if "0"==appid_gdt:
        print "no gdt ad appid"
        config_adsdk_android.SetAdSdk(source.GDT, False)
    else:
        config_adsdk_android.SetAdSdk(source.GDT, True)


    config_adsdk_android.SetAdSdk(source.ADVIEW, False) 
    
    config_adsdk_android.SetAdSdk(source.UNITY, True)
    config_adsdk_android.SetAdSdk(source.ADMOB, True)
 

    print "copy_config sucess"
