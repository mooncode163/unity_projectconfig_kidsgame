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
    INPUT_CLEAR = "input_clear" 
    ENTER = "enter"
    # 粘贴
    CTR_V = "control_v"
    

class CmdInfo(object):  
    type:None
    cmd:None
    value:None
    delay:None
    isWaiting:None



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
        info.isWaiting = False

        self.listCmd.append(info)
    def AddCmd2(self,type,cmd):
        info = CmdInfo()
        info.type = type
        info.cmd = cmd
        info.value = ""
        info.delay = 1
        info.isWaiting = False

        self.listCmd.append(info)

    def AddCmdInfo(self,info): 
        self.listCmd.append(info)    
    
    def Clear(self):
        self.listCmd.clear()

    def IsElementExist(self,element):
        flag=True
        browser=self.driver
        try:
            # browser.find_element_by_css_selector(element)
            browser.find_element(By.XPATH, element)
            return flag 
        except:
            flag=False
            return flag

# 组合查找 https://blog.csdn.net/qq_32189701/article/details/100176577
# find_element_by_xpath("//input[@class=‘s_ipt’ and @name=‘wd’]")
    def Run(self,isClear):
        for info in self.listCmd:
            if info.isWaiting:
                if self.IsElementExist(info.cmd):
                    item = self.driver.find_element(By.XPATH, info.cmd)
                else:
                    # waiting
                    while True:
                        time.sleep(1) 
                        print("waiting info.cmd=", info.cmd)
                        if self.IsElementExist(info.cmd): 
                            item = self.driver.find_element(By.XPATH, info.cmd)
                            break

            else:
                item = self.driver.find_element(By.XPATH, info.cmd)
            # item.click()
            if info.type == CmdType.CLICK:
                self.driver.execute_script("arguments[0].click();", item)
            if info.type == CmdType.INPUT:
                item.clear()
                item.send_keys(info.value)
                # item.clear()
                # item.send_keys(info.value)
                # item.text = info.value

            if info.type == CmdType.INPUT_CLEAR:
                item.clear()

            if info.type == CmdType.ENTER:
                item.send_keys(Keys.ENTER)
            if info.type == CmdType.CTR_V:
                item.send_keys(Keys.CONTROL,"v")
                 

            time.sleep(info.delay)

        if isClear:
            self.Clear()

  

 
 