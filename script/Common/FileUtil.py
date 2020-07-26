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
# sys.path.append('./common')

o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径
from Common import common 

from xml.dom.minidom import parse
 
 
class FileUtil():  
   
    @staticmethod   
    def CopyDir(src,dst): 
        flag = os.path.exists(dst)
        if flag:
            shutil.rmtree(dst)
        shutil.copytree(src,dst)
  