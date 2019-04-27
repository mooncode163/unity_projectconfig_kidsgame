#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time
import datetime
import sys

# include appinfo.py
# sys.path.append('./common')
import appname
import appchannel
import source
import apk_build

sys.path.append('./common')
import common

listChannel = [source.HUAWEI]




# 主函数的实现
if __name__ == "__main__":

    print "脚本名：", sys.argv[0]
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    isHD = False

    for i in range(1, count):
        print "参数", i, sys.argv[i]
        if i == 1:
            cmdPath = sys.argv[i]

        if i == 2:
            if sys.argv[i] == "hd":
                isHD = True

    common.SetCmdPath(cmdPath)

    android_studio_dir = common.GetRootDirAndroidStudio()
    # python 里无法直接执行cd目录，要用chdir改变当前的工作目录
    os.chdir(android_studio_dir)

    for channel in listChannel:
        print "apk_build_gp:" + channel
        appchannel.updateChannel(channel) 
        apk_build.buildApk()
        apk_build.copyApk(channel)

    print "apk_build_huawei sucess"
