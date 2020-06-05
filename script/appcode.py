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

# 删除子目录
def DeleteSubDir(sourceDir):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
        #目录嵌套
        if os.path.isdir(sourceFile):
            if file!="CodeZip":
                shutil.rmtree(sourceFile)
 


def GetDirScriptApps():
    return common.GetRootUnityAssets() + "/Script/Apps/"

def GetDirSourceCode():
    return GetDirScriptApps() + "/" + common.getGameType()


def GetFileSourceCodeZip():
    return common.GetRootUnityAssets() + "/Script/Apps/CodeZip/" + common.getGameType() + ".zip"

# 备份游戏代码到CodeZip  压缩zip
def SaveCode():
    dir_code = GetDirSourceCode()
    file_zip = GetFileSourceCodeZip()
    
    if not os.path.exists(dir_code):
        return

    print(dir_code)
    print(file_zip)
    
    # 压缩目录
    ziputils.zipDir(dir_code,file_zip)



# 从CodeZip的zip文件里解压到assets目录
 
def CopyCode():
    dir_code = GetDirScriptApps()
    if not os.path.exists(dir_code):
        return

    file_zip = GetFileSourceCodeZip()

    print(dir_code)
    print(file_zip)

    DeleteSubDir(dir_code)

    flag = os.path.exists(file_zip)
    if flag:
        ziputils.un_zip(file_zip,dir_code)
    




# 主函数的实现
if __name__ == "__main__":
    # 设置为utf8编码
    # reload(sys)
    # sys.setdefaultencoding("utf-8")

    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    strCmd = ""
    cmdPath = ""
    count = len(sys.argv) 

    for i in range(1, count):
        print("参数", i, sys.argv[i])
        if i == 1:
            cmdPath = sys.argv[i]

        if i == 2:
            strCmd = sys.argv[i]

    common.SetCmdPath(cmdPath)
    gameName = common.getGameName()
    gameType = common.getGameType()
    
    if strCmd == "save":
        SaveCode()

    if strCmd == "copy":
        CopyCode()
