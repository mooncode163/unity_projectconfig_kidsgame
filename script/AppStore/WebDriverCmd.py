# 导入selenium的浏览器驱动接口 

import sys
import os
import json
o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径
 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 


class CmdType(object): 
    CLICK = "click"
    INPUT = "input" 

class CmdInfo(object):  
    type:None
    cmd:None
    value:None
    delay:None



class WebDriverCmd():  
    listCmd:None
    driver: None

    #构造函数
    def __init__(self,webdv):
        self.listCmd= []
        self.driver = webdv

    def AddCmd(self,type,cmd,value,delay):
        info = CmdInfo()
        info.type = type
        info.cmd = cmd
        info.value = value
        info.delay = delay

        self.listCmd.append(info)
    
    def Clear(self):
        self.listCmd.clear()

# 组合查找 https://blog.csdn.net/qq_32189701/article/details/100176577
# find_element_by_xpath("//input[@class=‘s_ipt’ and @name=‘wd’]")
    def Run(self,isClear):
        for info in self.listCmd:
            item = self.driver.find_element(By.XPATH, info.cmd)
            # item.click()
            if info.type == CmdType.CLICK:
                self.driver.execute_script("arguments[0].click();", item)
            if info.type == CmdType.INPUT:
                item.send_keys(info.value)

            time.sleep(info.delay)

        if isClear:
            self.Clear()

  

 
 