#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time
import datetime
import sys
# include common.py
sys.path.append('./common')
import common


# 主函数的实现
if __name__ == "__main__":

    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1, count):
        print("参数", i, sys.argv[i])
        if i == 1:
            cmdPath = sys.argv[i]

    common.SetCmdPath(cmdPath)

    targetDir = common.GetRootDirAndroidStudio()

    # build
    dir2 = targetDir + "/build"
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)

    print("apk_build_clean sucess")
