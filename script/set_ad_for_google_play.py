#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path
import time
import datetime

# include common.py
sys.path.append('./common')
import common
import source
import AppInfo
import config_adsdk_android


# 主函数的实现
if __name__ == "__main__":

      # 设置为utf8编码
    reload(sys)
    sys.setdefaultencoding("utf-8")

    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1, count):
        print ("参数", i, sys.argv[i])
        if i == 1:
            cmdPath = sys.argv[i]

    common.SetCmdPath(cmdPath)

    config_adsdk_android.SetAdSdk(source.ADVIEW, False)
    config_adsdk_android.SetAdSdk(source.GDT, False)
    config_adsdk_android.SetAdSdk(source.XIAOMI, False)
    config_adsdk_android.SetAdSdk(source.UNITY, True)
    config_adsdk_android.SetAdSdk(source.MOBVISTA, False)    
    
    print "set_ad_for_google_play sucess"
