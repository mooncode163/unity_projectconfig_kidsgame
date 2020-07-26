#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path
import time,  datetime
import platform
import json
from hashlib import md5
g_CmdPath = ""


def isWindowsSystem():
    return 'Windows' in platform.system()
 
def isLinuxSystem():
    return 'Linux' in platform.system()

#http://blog.csdn.net/imzoer/article/details/8733396
#http://blog.sina.com.cn/s/blog_708be8850101bu02.html
##复制文件
#
#shutil.copyfile('listfile.py', 'd:/test.py')
#
##复制目录
#
#shutil.copytree('d:/www', 'c:/temp/')

#把某一目录下的所有文件复制到指定目录中
def copyFiles(sourceDir,  targetDir):
    if sourceDir.find(".svn") > 0:
        return
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(sourceFile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                open(targetFile, "wb").write(open(sourceFile, "rb").read())
#    if os.path.isdir(sourceFile):
#        First_Directory = False
#        copyFiles(sourceFile, targetFile)

#复制一级目录下的所有文件到指定目录：
def coverFiles(sourceDir,  targetDir):
    for file in os.listdir(sourceDir):
        # 过滤文件
        if file == "Thumbs.db":
            continue

        sourceFile = os.path.join(sourceDir,  file)
        targetFile = os.path.join(targetDir,  file)
            #cover the files
        if os.path.isfile(sourceFile):
            # print(sourceFile)
            # open(targetFile, "wb").write(open(sourceFile, "rb").read())
            
            # flag = os.path.exists(targetFile)
            # if flag:
            #     os.remove(targetFile)

            shutil.copyfile(sourceFile, targetFile)

        #目录嵌套
        if os.path.isdir(sourceFile):
            # print(sourceFile)
            coverFiles(sourceFile,targetFile)


#删除一级目录下的所有文件：
def removeFileInFirstDir(targetDir):
     for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(targetFile):
            os.remove(targetFile)
 
 # 复制单个文件
def copyOneFile(sourceFile,  targetFile):
        if os.path.isfile(sourceFile):
            open(targetFile, "wb").write(open(sourceFile, "rb").read())


 # 复制目录
def CopyDir(sourceFile,  targetFile):
    flag = os.path.exists(targetFile)
    if flag:
        shutil.rmtree(targetFile)
    shutil.copytree(sourceFile,targetFile)
    
def copyResourceFiles(sourceDir,  targetDir):

    #  先清除
    for file in os.listdir(targetDir):
        if file=="Common":
            continue
            
        targetFile = os.path.join(targetDir,  file)
        #目录
        if os.path.isdir(targetFile): 
            shutil.rmtree(targetFile)
        else :
            os.remove(targetFile)

    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
        targetFile = os.path.join(targetDir,  file)
        #目录
        if os.path.isdir(sourceFile): 
            shutil.copytree(sourceFile,targetFile)
        else :
            shutil.copyfile(sourceFile,targetFile)


def saveResourceFiles(sourceDir,  targetDir):

    #  先清除
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir,  file)
        #目录
        if os.path.isdir(targetFile): 
            shutil.rmtree(targetFile)
        else :
            os.remove(targetFile)

    for file in os.listdir(sourceDir):

        if file=="Common":
            continue

        sourceFile = os.path.join(sourceDir,  file)
        targetFile = os.path.join(targetDir,  file)
        #目录
        if os.path.isdir(sourceFile): 
            shutil.copytree(sourceFile,targetFile)
        else :
            shutil.copyfile(sourceFile,targetFile)

#   

#返回当前的日期，以便在创建指定目录的时候用：
# def getCurTime():
#           nowTime = time.localtime()
#                 year = str(nowTime.tm_year)
#                     month = str(nowTime.tm_mon)
#                         if len(month) < 2:
#                                 month = '0' + month
#                                 day =  str(nowTime.tm_yday)
#                                     if len(day) < 2:
#                                             day = '0' + day
#     return (year + '-' + month + '-' + day)

#获取脚本文件的当前路径
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

def SetCmdPath(cmdPath): 
    global g_CmdPath
    g_CmdPath = cmdPath 
    print("SetCmdPath cmdPath=",cmdPath)
    idx = cmdPath.find("\\cmd_")
    g_CmdPath = cmdPath[0:idx]
    # if isWindowsSystem():
    #     # windows 系统路径最后一个是\字符，需要删除
    #     g_CmdPath = getLastDirofDir(g_CmdPath)

    # # 跳过cmd_xxx目录
    # g_CmdPath = getLastDirofDir(g_CmdPath)

#last dir
def getLastDir(): 
    return getLastDirofDir(cur_file_dir())

def getLastDirofDir(path): 
    str_split = '/'
    if isWindowsSystem():
        str_split = '\\'
    idx = path.rfind(str_split)

    ret = path[0:idx]
    return ret

# 不包含.
def getFileExt(path):  
    idx = path.rfind(".")+1
    slen=len(path)
    size = slen-idx
    ret = path[idx:]
    # print(path="+path+" idx="+str(idx)+" ret="+ret+" slen="+str(slen)
    return ret

def getPathName():
    return getDirNameofPath(getLastDir())

def getDirNameofPath(path): 
    str_split = '/'
    if isWindowsSystem():
        str_split = '\\'
    idx = path.rfind(str_split)
    s_len=len(path)
    game = path[idx+1:s_len]
    return game
    
def getGameName():
    return getDirNameofPath(g_CmdPath)

def getGameType():
    return getDirNameofPath(getLastDirofDir(g_CmdPath)) 
    
def saveString2File(str, file):
    f = open(file, 'wb')  # 若是'wb'就表示写二进制文件
    b = str.encode('utf-8',"ignore")
    f.write(b)
    f.close()

def get_FileSize(filePath):
    fsize = os.path.getsize(filePath) 
    return fsize

def get_MD5_checksum_file(filename):
    with open(filename, 'rb') as f:
        md5obj = md5()
        while 1:
            buf = f.read(1024)
            if not buf:
                break
            md5obj.update(buf)
    return md5obj.hexdigest()

def GetProjectName(): 
    #  F:\sourcecode\unity\product\kidsgame 
    path = cur_file_dir()
    # print("GetProjectName path=",path)
    key = "\\product\\"
    idx = path.find(key)+len(key) 
    name = path[idx:]
    # print("GetProjectName name=",name)
    idx = name.find("\\")
    name = name[0:idx]
    # path = getLastDirofDir(path)
    # path = getLastDirofDir(path)
    # name = getDirNameofPath(path)
    # print("GetProjectName,name = "+name)
    
    print("GetProjectName name=",name)
    return name

def GetRootDir():
    #Users/moon/sourcecode/unity/product/kidsgame
    return "../../"

def GetDirProduct(): 
    #Users/moon/sourcecode/unity/product
    dir = GetRootDir()+"../"
    return dir

def GetDirProductCommon():  
    return GetDirProduct()+"/Common"

def GetResourceDataRoot(): 
    return GetRootDir()+"/ResourceData"

def GetRootProjectUnity(): 
    return GetRootDir()+"/"+GetProjectName()+"Unity" 

def GetRootUnityAssets(): 
    return GetRootProjectUnity()+"/Assets"

def GetProjectConfig():
    return GetRootDir()+"/ProjectConfig"

def GetProjectIcon():
    return GetRootDir()+"/ProjectIcon"

def GetProjectIconApp():
    gameType = getGameType()
    gameName = getGameName()
    return GetProjectIcon()+"/"+gameType+"/"+gameName

def GetProjectOutPut():
    return GetRootDir()+"/ProjectOutPut"

def GetProjectOutPutIPA():
    dir="shu"
    if AppForPad(True):
        dir="heng" 

    return GetProjectOutPut()+"/IPA/"+dir

def GetOutPutIPAName():
    gameType = getGameType()
    gameName = getGameName()

    ipa="ipa"+"_"+gameType+"_"+gameName+"_"+GetAppVersionIos()+".ipa"
    if AppForPad(True):
        ipa="ipa"+"_"+gameType+"_"+gameName+"_hd_"+GetAppVersionIos()+".ipa" 

    return ipa

def GetProjectOutPutApp():
    gameType = getGameType()
    gameName = getGameName()
    return GetProjectOutPut()+"/"+gameType+"/"+gameName

def GetOutPutApkPath(channel,isHd):
    gameType = getGameType()
    gameName = getGameName() 
    dirapk = GetProjectOutPutApp() + "/apk" 
    if isHd==True:
        dirapk+="/heng"
        gameName += "_hd"
    else:
        dirapk+="/shu"

    return dirapk + "/" + gameType + "_" + gameName + "_" + channel + ".apk"


def GetOutPutApkPathWin32(rootdir,channel,isHd):
    gameType = getGameType()
    gameName = getGameName() 
    # GetProjectOutPut
    dirapk = rootdir+"\\"+gameType+"\\"+gameName + "\\apk" 
    if isHd==True:
        dirapk+="\\heng"
        gameName += "_hd"
    else:
        dirapk+="\\shu"
        
    return dirapk + "\\" + gameType + "_" + gameName + "_" + channel + ".apk"

def GetOutPutIconPathWin32(rootdir,channel,isHd):
    gameType = getGameType()
    gameName = getGameName() 
    # GetProjectOutPut
    dirapk = rootdir+"\\"+gameType+"\\"+gameName  
    if isHd==True:
        dirapk+="\\iconhd" 
    else:
        dirapk+="\\icon"
        
    return dirapk

def GetOutPutCopyRightPathWin32(rootdir,isHd):
    gameType = getGameType()
    gameName = getGameName() 
    # GetProjectOutPut
    dirapk = rootdir+"\\"+gameType+"\\"+gameName  
    if isHd:
        dirapk+="\\copyrighthd" 
    else:
        dirapk+="\\copyright"
        
    return dirapk
    

def GetOutPutScreenshotPathWin32(rootdir,channel,isHd):
    gameType = getGameType()
    gameName = getGameName() 
    # GetProjectOutPut
    dirapk = rootdir+"\\"+gameType+"\\"+gameName+"\\screenshot"
    if isHd==True:
        dirapk+="\\heng" 
    else:
        dirapk+="\\shu"
        
    return dirapk

def GetOutPutAdPathWin32(rootdir,channel,isHd):
    gameType = getGameType()
    gameName = getGameName() 
    # GetProjectOutPut
    dirapk = rootdir+"\\"+gameType+"\\"+gameName+"\\ad" 
    return dirapk

def GetRootProjectIos():
    if IsVMWare():
        return GetRootProjectIosUser()
    return GetRootProjectIosNormal() 

def GetRootProjectIosUser():
    return "/Users/moon/sourcecode/unity/product/"+GetProjectName()+"/project_ios"

def GetRootProjectIosNormal():
    return GetRootDir()+"/project_ios"

def GetRootProjectAndroid():
    return GetRootDir()+"/project_android"

def GetRootProjectWin():
    return GetRootDir()+"/project_win"



def GetRootDirAndroidStudio():
    return GetRootDir()+ "/project_android/"+GetProjectName()

def GetRootDirAndroidOutput():
    # GetRootProjectUnity()+"/OutPut/Android/"+GetProjectName()
    gameType = getGameType()
    gameName = getGameName() 
    return GetProjectOutPut()+"/Unity"+"/"+gameType+"/"+gameName+"/Android/"+"unityLibrary"
    

def GetRootDirAndroidAsset(): 
    return GetRootDirAndroidStudio()+ "/src/main/assets"

def GetRootDirXcode(): 
    if IsVMWare():
        return GetRootDirXcodeUser()

    return GetRootDirXcodeNormal()

def IsVMWare(): 
    my_file =  "/Volumes/VMware Shared Folders"
    if os.path.exists(my_file):
        # 指定的目录存在
        return True
    return False


def GetProjectNameApp():
    gameType = getGameType()
    gameName = getGameName()
    return GetProjectName()+"_device"+"_"+gameType+"_"+gameName

def GetRootDirXcodeNormal():
    return GetRootProjectIosNormal()+"/"+GetProjectNameApp()

def GetRootDirXcodeUser():
    #Users/moon/sourcecode/unity/product/kidsgame
    # "../../"
    return GetRootProjectIosUser()+"/"+GetProjectNameApp()


def GetProjectConfigDefault():
    return GetProjectConfig()+"/default"  

def GetProjectConfigApp():
    gameType = getGameType()
    gameName = getGameName()
    return GetProjectConfig()+"/"+gameType+"/"+gameName

def GetProjectConfigAppType():
    gameType = getGameType()
    return GetProjectConfig()+"/"+gameType

def getAndroidProjectGameData(): 
    path = GetRootDir()+"/project_android/"+GetProjectName()+"/src/main/assets/GameData"
    return path

def getAndroidProjectApk(): 
    # path = GetRootDir()+"/project_android/kidsgame/build/outputs/apk/"+"kidsgame-release.apk"
    path = GetRootDir()+"/project_android/"+GetProjectName()+"/build/outputs/apk/release/"+GetProjectName()+"-release.apk"
    return path

    
def GetConfigDataDir(): 
    apptype = getGameType()
    appname = getGameName()
    ret_dir = GetResourceDataRoot()+"/"+apptype+"/"+appname
    ret_dir+="/ConfigData"
    return ret_dir

def GetGameDataDirOfResourceData(): 
    apptype = getGameType()
    appname = getGameName()
    ret_dir = GetResourceDataRoot()+"/"+apptype+"/"+appname
    ret_dir+="/GameData"
    return ret_dir

def GetAdConfigDir(): 
    return GetGameDataDirOfResourceData()+"/adconfig"

def GetCommonAdConfigDir(): 
    return GetResourceDataRoot()+"/ConfigDataCommon/adconfig/cn"

def GetConfigDir(): 
    return GetConfigDataDir()+"/config"

def GetFileString(filePath):  
    f = open(filePath, 'rb')
    strFile = f.read().decode('utf-8',"ignore")
    f.close()
    return strFile

   
def GetPackageAndroidFromXml():
    fileXml = GetRootDirAndroidStudio()+"/src/main/AndroidManifest.xml"
    strFile = GetFileString(fileXml)
    # package="com.moonma.shapecolor.pad"
    strHead = "package=\""
    strEnd = "\""
    idx = strFile.find(strHead)
    package = ""
    if idx>=0:
        idx +=len(strHead)
        strOther = strFile[idx:]
        idx = strOther.find(strEnd)
        package = strOther[0:idx]
    
    return package


def GetPackageIos():
    xcode_plist = GetRootDirXcode()+ "/Info.plist" 
    print("xcode_plist="+xcode_plist)
    strFile = GetFileString(xcode_plist)
    # 		<key>CFBundleIdentifier</key>
	#	<string>com.moonma.pinpinle.nongchang</string>
    strHead = "CFBundleIdentifier"
    strMid = "<string>"
    strEnd = "</string>"
    idx = strFile.find(strHead)
    package = ""
    if idx>=0:
        idx +=len(strHead)
        strOther = strFile[idx:] 
        idx = strOther.find(strMid)
        if idx>=0:
            idx +=len(strMid)
            strOther = strOther[idx:] 
            idx = strOther.find(strEnd)
            package = strOther[0:idx]
    
    return package


def GetAppVersionIos():
    xcode_plist = GetRootDirXcode()+ "/Info.plist" 
    print("xcode_plist="+xcode_plist)
    strFile = GetFileString(xcode_plist)
    # 		<key>CFBundleIdentifier</key>
	#	<string>com.moonma.pinpinle.nongchang</string>
    strHead = "CFBundleShortVersionString"
    strMid = "<string>"
    strEnd = "</string>"
    idx = strFile.find(strHead)
    package = ""
    if idx>=0:
        idx +=len(strHead)
        strOther = strFile[idx:] 
        idx = strOther.find(strMid)
        if idx>=0:
            idx +=len(strMid)
            strOther = strOther[idx:] 
            idx = strOther.find(strEnd)
            package = strOther[0:idx]
    
    return package

def AppForPad(isIos):
    package = GetPackageAndroidFromXml()
    if isIos: 
        package = GetPackageIos()

    print("package="+package)

    ret = False
    if package.find(".ipad")>=0 or package.find(".pad")>=0:
        ret = True

    return ret


def DeleteMetaFiles(sourceDir):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
            #cover the files
        if os.path.isfile(sourceFile):
            # print(sourceFile)
            # 分割文件名与后缀
            temp_list = os.path.splitext(file)
            # name without extension
            src_apk_name = temp_list[0]
            # 后缀名，包含.   例如: ".apk "
            ext = getFileExt(file) 
            # print(file="+file+" ext="+ext 
            apk_ext='meta'
            if apk_ext==ext:
                 print(sourceFile)
                 os.remove(sourceFile)
                
        #目录嵌套
        if os.path.isdir(sourceFile):
            # print(sourceFile)
            DeleteMetaFiles(sourceFile)

def SaveJson(filePath,dataRoot):   
    # 保存json 
    # json.dumps(dataRoot, f, ensure_ascii=False,indent=4,sort_keys = True).encode('utf8',"ignore")
    json_str = json.dumps(dataRoot,ensure_ascii=False,indent=4,sort_keys = True)
    saveString2File(json_str,filePath)
    # json.dumps(dataRoot, f, ensure_ascii=False,indent=4,sort_keys = True)


 