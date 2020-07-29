# 导入selenium的浏览器驱动接口
import sys
import os
import json
o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径


 
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sqlite3
import win32gui
import win32con 

import json

# 要想调用键盘按键操作需要引入keys包

# 导入chrome选项


# pip3 install pywin32

# sys.path.append('../common')


class AppStoreHuawei:
 

    def GoHome(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(chrome_options=chrome_options)
        # 全屏
        driver.maximize_window()

        driver.get(
            "https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=手机QQ空间&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html&pt_no_auth=0")
        
        button=driver.find_element_by_class_name("face")
        # print(button)
        button.click()
        
        time.sleep(5)
        print(driver.current_url)
        text=driver.page_source
        cookie = driver.get_cookies()
        print(cookie)
        jsonCookies = json.dumps(cookie)
        with open('qqhomepage.json', 'w') as f:
            f.write(jsonCookies)
  

# 主函数的实现
if __name__ == "__main__":
  
    ad = AppStoreHuawei()  
    ad.GoHome()
  
    print("AppStoreHuawei sucess")
