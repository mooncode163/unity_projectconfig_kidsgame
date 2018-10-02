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
 

def getGameName():
    path = common.getLastDir()
    idx = path.rfind('/')
    s_len=len(path)
    game = path[idx+1:s_len]
    return game

def getGameType():
    name = getGameName()
    idx = name.find('_')
    s_len=len(name)
    game = name[0:idx]
    return game

#主函数的实现
if  __name__ =="__main__":
    
    #入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    print "脚本名：", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "参数", i, sys.argv[i]

    gameName = getGameName()
    gameType = getGameType()
    print gameName
    print gameType
    # rootDir ="/Users/jaykie/sourcecode/cocos2dx/product/game/ertong"
    rootAndroidStudio ="../../../../project_android/kidsgame"
    rootiOSXcode ="../../../../project_ios/kidsgame_device"
    resDataName = getGameName()#sys.argv[1]
    iconDirName = sys.argv[1]
    adDirName = sys.argv[2]

    project_ios = "ios/project"
    project_android = "android/project"
    if iconDirName=="iconhd":
        project_ios = "ios/project_hd"
        project_android = "android/project_hd"

    # resources_data
    # sourceDir = rootDir + "/resources_data/" + resDataName
    # dataDir = rootDir+"/Resources/data"
    # targetDir = dataDir + "/" + resDataName
    # assetDir = rootDir+"/proj.android-studio/app/assets"


    #data
    # flag = os.path.exists(dataDir)
    # if flag:
    #     shutil.rmtree(dataDir)

    # dir1 = sourceDir;
    # dir2 = targetDir;
    # shutil.copytree(dir1,dir2)

    # sourceFile = sourceDir + "/config/app_name_keyword.plist"
    # targetFile = dataDir + "/app_name_keyword.plist"

    # copyOneFile(sourceFile,targetFile)


    # assets
    # dir1 = rootDir+"/Resources";
    # dir2 = assetDir;
    # flag = os.path.exists(dir2)
    # if flag:
    #     shutil.rmtree(dir2)
        
    # shutil.copytree(dir1,dir2)





    # project
    iconRoot = "../../../../ProjectIcon"+"/"+gameType
    reousceDataRoot = "../../../../ResourceData"
    reousceUnity = "../../../../KidsGameUnity/Assets/Resources"
    sourceDir = "../"
    sourceAdDir = "../../../../ad_src/"+adDirName
    adCommonDir = "../../../../../common_ad"
    adSrcDir = adCommonDir+"/ad_src/"+adDirName
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
    dir1 = "../../../LaunchScreenIcon_ios/Unity-iPhone";
    dir2 = rootiOSXcode + "/Unity-iPhone"
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)

    dir1 = iconRoot+"/"+"/icon_"+resDataName+"/"+iconDirName+"/ios"
    dir2 = rootiOSXcode + "/Unity-iPhone/Images.xcassets/AppIcon.appiconset"
    common.coverFiles(dir1,   dir2)


    #android icon
    dir1 = iconRoot+"/icon_"+resDataName+"/"+iconDirName+"/android"
    # dir2 = sourceDir+"/res"
    dir2 = "../"+project_android+"/res"
    # if iconDirName=="iconhd":
    #     dir2 = "./android/project/res_hd"
    common.coverFiles(dir1,dir2);

    # 
    project = sourceDir+"/"+project_android+"/xml"
    common.coverFiles(project,   targetDir)

    project = sourceDir+"/"+project_android+"/grade"
    targetDir = rootAndroidStudio
    common.coverFiles(project,   targetDir)


    
    #res android
    dir1 = sourceDir+"/"+project_android + "/res"
    # if iconDirName=="iconhd":
    targetDir = rootAndroidStudio+"/src/main"
    dir2 = targetDir+"/res";
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)

    shutil.copytree(dir1,dir2)

    # #ad
    # dir1 = sourceAdDir;
    # dir2 = javaLibDir+"/ad";
    # flag = os.path.exists(dir2)
    # if flag:
    #     shutil.rmtree(dir2)

    # shutil.copytree(dir1,dir2)

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

    common.copyOneFile(file1,file2)

    # ad libs
    dir1 = adCommonDir+"/libs_"+adDirName;
    dir2 = rootAndroidStudio+"/libs/ad";
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)

    shutil.copytree(dir1,dir2)

# ad src
    dir1 = adSrcDir;
    dir2 =  rootAndroidStudio+"/src/main/java/com/moonma/common/ad"
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)

    shutil.copytree(dir1,dir2)


    print "copy_config sucess"
