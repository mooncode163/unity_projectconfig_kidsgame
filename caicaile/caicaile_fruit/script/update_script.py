#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path
import time
import datetime
import json

#include common.py
sys.path.append('./common')
import common

 
 
# 主函数的实现
if __name__ == "__main__":
    # 设置为utf8编码
    reload(sys)
    sys.setdefaultencoding("utf-8")

    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    print "脚本名：", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "参数", i, sys.argv[i]
    
    dir_default = "../../../default/script"
    dir_to = "../script"

#先从default 拷贝 工程文件模版
    # ios project file
    dir1 = dir_default
    dir2 = dir_to
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)
 

    print "update_script sucess"
