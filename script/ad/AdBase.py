# 导入selenium的浏览器驱动接口
from ParseAdGdt import ParseAdGdt
import AppInfo
import win32con
import win32gui
import sqlite3
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from Common import source
from Common import common
import sys
import os
import json
o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径


from AppStore.WebDriverCmd import CmdType
from AppStore.WebDriverCmd import WebDriverCmd 
from AppStore.WebDriverCmd import CmdInfo 
 

# 要想调用键盘按键操作需要引入keys包

# 导入chrome选项


# pip3 install pywin32

# sys.path.append('../common')


class AdBase():
    driver: None 

 



         