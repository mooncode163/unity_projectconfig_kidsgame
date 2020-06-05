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
import source

sys.path.append('./ziputils')
import ziputils

def UploadAllIPA(dir):
    if dir.find(".svn") > 0:
        return
    for file in os.listdir(dir):
        srcfile = os.path.join(dir,  file) 
        if os.path.isfile(srcfile): 
            UploadOneIPA(srcfile)

        if os.path.isdir(srcfile): 
            UploadAllIPA(srcfile)

def UploadOneIPA(ipafile):
    print ("UploadOneIPA= "+ipafile)
    # 上传ipa
    if IsXcode10():
        strCmd = "/Applications/Xcode.app/Contents/Applications/Application\ Loader.app/Contents/Frameworks/ITunesSoftwareService.framework/Versions/A/Support/altool --upload-app -f " + ipafile + " -t ios -u "+source.APPSTORE_USER+" -p "+source.APPSTORE_PASSWORD 
    #    xcode 11
    else:
        strCmd = "xcrun altool --upload-app -f " +  ipafile +  " -t ios -u "+source.APPSTORE_USER+" -p "+source.APPSTORE_PASSWORD 
   
    # + "--output-format xml"
    os.system(strCmd)


def ExportIPA(ipafile):
    RootDir = common.GetRootProjectIos()
    archive_file = RootDir + "/app.xcarchive"
    exportOptionPlist_file = RootDir + "/ExportOptions.plist"
    target = "Unity-iPhone"
    
    # 导出ipa
    strCmd = "xcodebuild -allowProvisioningUpdates -exportArchive " + " -archivePath " + \
        archive_file + " -exportPath " + ipafile + \
        " -exportOptionsPlist " + exportOptionPlist_file
    os.system(strCmd)

    CopyIPA(common.GetRootProjectIos() + "/app/" + target+"/" + target + ".ipa")


def BuildIPA(ipafile):
    CopyExportOptionsPlist()
    ChmodSh()
    # curDir = "/Users/moon/Library/MobileDevice/Provisioning Profiles"
    curDir = "/Users/moon/Library/MobileDevice/Provisioning Profiles"
    DeleteProvisioningProfiles(curDir)  

    RootDir = common.GetRootProjectIos()
    archive_file = RootDir + "/app.xcarchive"
    target = "Unity-iPhone"
    xcode_project = common.GetRootDirXcode()+ "/Unity-iPhone.xcodeproj" 

    flag = os.path.exists(archive_file)
    if flag:
        shutil.rmtree(archive_file)

    flag = os.path.exists(ipafile)
    if flag:
        shutil.rmtree(ipafile)



    RootDir = common.GetRootProjectIos() 
    AppDir = RootDir + "/app"
    flag = os.path.exists(AppDir)
    if flag:
        shutil.rmtree(AppDir)
    
    AppDir = RootDir + "/app_export_ipa"
    flag = os.path.exists(AppDir)
    if flag:
        shutil.rmtree(AppDir)


    strCmd = "xcodebuild -allowProvisioningUpdates -project " + xcode_project + " -scheme " + \
        target + " -configuration Release clean archive" + " -archivePath " + archive_file
    os.system(strCmd)

def CopyExportOptionsPlist():   
    src =common.GetProjectConfig() + "/ExportOptions.plist"
    dst =common.GetRootProjectIos() + "/ExportOptions.plist"
    if not os.path.isfile(dst):
        shutil.copyfile(src,dst)


def CopyIPA(ipafile):
#copy ipa 到共享目录
    # if common.IsVMWare():
    ipa_file_src = ipafile 

        #GetRootProjectIosVMVare
    dir_ipa = common.GetProjectOutPutIPA()
    if not os.path.exists(dir_ipa):
        os.makedirs(dir_ipa) 

    ipa_file_dst =dir_ipa + "/" + common.GetOutPutIPAName()
    print ("ipa_file_src= "+ipa_file_src)
    print ("ipa_file_dst= "+ipa_file_dst)

    if os.path.isfile(ipa_file_src):
        shutil.copyfile(ipa_file_src,ipa_file_dst)

def CopyXcodeProject(isDel):
#copy共享目录
    if not common.IsVMWare():
        return

    ZipProject()

    dirsrc = common.GetRootDirXcodeNormal()+ ".zip" 
    dirdst = common.GetRootDirXcodeUser()+ ".zip" 
    flag = os.path.exists(dirsrc)
    if flag:  
        shutil.copyfile(dirsrc,dirdst)
    
    UnZipProject()

#压缩
def ZipProject():
    dirproject = common.GetRootDirXcodeNormal()
    file_zip = dirproject+ ".zip" 

    if not os.path.exists(dirproject):
        return

    if os.path.exists(file_zip):
        # os.remove(file_zip) 
        return
        
    DeleteMetaFiles(dirproject+"/Frameworks/Plugins")
    DeleteMetaFiles(dirproject+"/Libraries/Plugins")
    # DeleteMetaFiles(dirproject+"/Frameworks/Plugins/iOS/ThirdParty/umeng/thirdparties/thirdparties_ios_1.0.5/SecurityEnvSDK.framework")

    # 压缩目录
    ziputils.zipDir(dirproject,file_zip)


def ChmodSh(): 
    project = common.GetRootDirXcodeUser() 
    # MapFileParser.sh: Permission denied
    # https://www.cnblogs.com/jukaiit/p/6860871.html
    # chmod a+x /Users/imac-1/Desktop/iosbuild-1/MapFileParser.sh
    file_sh = project+ "/MapFileParser.sh"
    print("file_sh ="+file_sh)
    if os.path.exists(file_sh):
        os.system("chmod a+x "+file_sh)

def UnZipProject():
    diroutput = common.GetRootProjectIosUser()
    project = common.GetRootDirXcodeUser()
    file_zip = project+ ".zip" 

    if os.path.exists(project):
        shutil.rmtree(project)

    if os.path.exists(file_zip):
        #解压
        ziputils.un_zip(file_zip,diroutput)

    ChmodSh()



def IsXcode10():
    ret = False
    if os.path.exists("/Applications/Xcode.app/Contents/Applications/Application\ Loader.app"):
        ret = True
    
    return ret

# xcode 证书 清空
def DeleteProvisioningProfiles(sourceDir):
    if not os.path.exists(sourceDir): 
        return
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
            #cover the files
        if os.path.isfile(sourceFile):
            # print sourceFile
            # 分割文件名与后缀
            temp_list = os.path.splitext(file)
            # name without extension
            src_apk_name = temp_list[0]
            # 后缀名，包含.   例如: ".apk "
            src_apk_extension = temp_list[1]
            apk_ext='.mobileprovision';
            if apk_ext==src_apk_extension:
                 print (sourceFile)
                 os.remove(sourceFile)
                
        #目录嵌套
        if os.path.isdir(sourceFile):
            # print sourceFile
            deleteFiles(sourceFile)
  


def DeleteMetaFiles(sourceDir):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
            #cover the files
        if os.path.isfile(sourceFile):
            # print sourceFile
            # 分割文件名与后缀
            temp_list = os.path.splitext(file)
            # name without extension
            src_apk_name = temp_list[0]
            # 后缀名，包含.   例如: ".apk "
            ext = common.getFileExt(file) 
            # print "file="+file+" ext="+ext 
            apk_ext='meta'
            if apk_ext==ext:
                 print (sourceFile)
                 os.remove(sourceFile)
                
        #目录嵌套
        if os.path.isdir(sourceFile):
            # print sourceFile
            DeleteMetaFiles(sourceFile)

# http://help.apple.com/itc/appsspec/#/itc6e4198248
# 主函数的实现
if __name__ == "__main__":

    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1, count):
        print ("参数", i, sys.argv[i])
        if i == 1:
            cmdPath = sys.argv[i]
   
    print ("cmdPath="+cmdPath+" count="+str(count))
    common.SetCmdPath(cmdPath)
    gameName = common.getGameName()
    gameType = common.getGameType()
    print ("gameName="+gameName)
    print ("gameType="+gameType)

    RootDir = common.GetRootProjectIos()
    target = "Unity-iPhone"  
    ipa_file = RootDir + "/app/" + target

    isUploadIPA = False
    isExportIPA = False

    # 清空频道文件
    channel_dir = common.GetRootDirXcode() + "/Data/Raw/channel"
    flag = os.path.exists(channel_dir)
    if flag:
        shutil.rmtree(channel_dir)

    if count > 1:
        argv1 = sys.argv[2]
        if argv1 == "upload_ipa":
            isUploadIPA = True
            # ipa_file = RootDir + "/app_export_ipa/" + target
            UploadOneIPA(ipa_file + "/" + target + ".ipa")

        if argv1 == "export_ipa":
            isExportIPA = True
            if count > 2:
                channel = sys.argv[2] 
                ipa_file = RootDir + "/app_" + channel + "/" + target

            # 生成频道文件
            os.makedirs(channel_dir)
            fp = open(channel_dir + "/" + channel, "w")
            if fp:
                fp.close()

            
            ExportIPA(ipa_file)

        if argv1 == "build":
            # CopyXcodeProject(False)
            BuildIPA(ipa_file)
            ExportIPA(ipa_file)
            
                
        if argv1 == "upload_allipa":
            UploadAllIPA(common.GetProjectOutPut()+"/IPA")
           
        if argv1 == "copy_project":
            CopyXcodeProject(True)

        if argv1 == "zip_project":
            ZipProject()

    print ("ipa_build sucess")
