# 导入selenium的浏览器驱动接口
import sys
import os
import json
o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径
from common import common
import appname
import source

from selenium import webdriver

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 导入chrome选项
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


import sqlite3


# sys.path.append('../common')



class AdGdt():
    driver: None
    dirRoot:None
    def saveString2File(self, str, file):
        f = open(file, 'wb')  # 若是'wb'就表示写二进制文件
        b = str.encode('utf-8', "ignore")
        f.write(b)
        f.close()

    def SetCmdPath(self, str):
        dir = common.getLastDirofDir(str)
        dir = common.getLastDirofDir(dir)
        dir = common.getLastDirofDir(dir)
        self.dirRoot = dir
        print("dir = ",dir)
    
    def GetJsonFile(self,isHd):
        cur_path = self.dirRoot+"/appinfo"
        jsonfile = cur_path+'/appname.json'
        if isHd:
            jsonfile = cur_path+'/appname_hd.json'
        return jsonfile

    def loadJson(self,isHd): 
        jsonfile = self.GetJsonFile(isHd) 
        
        with  open(jsonfile, 'rb') as json_file:
            data = json.load(json_file)
            return data


    def GetPackage(self,osSrc,isHD): 
        jsonData = self,loadJson(isHD) 
        isOld = IsOldVersion(jsonData)
        ret = ""
        if isOld:
            key = "PACKAGE_IOS"
            if osSrc == source.ANDROID:
                key = "PACKAGE_ANDROID" 
            ret = jsonData[key]
        else:      
            if osSrc == source.ANDROID:
                ret = jsonData["apppackage"][source.ANDROID]["default"] 
            if osSrc == source.IOS:
                ret = jsonData["apppackage"][source.IOS]["default"]

        return ret

    def GoHome(self):
        # 加载百度页面
        # driver.get("https://developer.huawei.com/consumer/cn/")
        self.driver.get("https://adnet.qq.com/index")
        # time.sleep(5)

        # self.saveString2File(self.driver.page_source,"1.html")
        #   # 点击登录按钮
        # self.driver.find_element_by_id('switcher_plogin').click()
        # time.sleep(1)

    def Login(self):
        # 3452644866
        print("waiting for login")
        time.sleep(20)
        return
        # driver.add_cookie("[{'domain': '.id1.cloud.huawei.com', 'expiry': 1908869785, 'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': True, 'value': '2049382e3828ef4470bef8b426c4bb3370e7d9e1147f53a18839e47dad7caf10a233e61ee15337b4373e'}, {'domain': '.id1.cloud.huawei.com', 'expiry': 1908869785, 'httpOnly': False, 'name': 'hwid_cas_sid', 'path': '/', 'secure': True, 'value': '2049382e3828ef4470bef8b426c4bb3370e7d9e1147f53a18839e47dad7caf10a233e61ee15337b4373e'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_idts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1593336984125'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_id_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': 'cf787be41ac24d65887dcd20c826ac97'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_idvc_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1593338788, 'httpOnly': False, 'name': 'HW_idn_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': 'ec569450f0ac4cd78fc72965d91ec7e8'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1608888984, 'httpOnly': False, 'name': 'HW_refts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1593336984124'}, {'domain': '.id1.cloud.huawei.com', 'httpOnly': True, 'name': 'CAS_THEME_NAME', 'path': '/', 'secure': True, 'value': 'red'}, {'domain': 'id1.cloud.huawei.com', 'httpOnly': False, 'name': 'cookieBannerOnOff', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.id1.cloud.huawei.com', 'httpOnly': True, 'name': 'VERSION_NO', 'path': '/', 'secure': True, 'value': 'UP_CAS_4.0.4.100'}, {'domain': 'id1.cloud.huawei.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/CAS', 'secure': True, 'value': '144E8B2ED3F5D9C8576742C1DDF4CF3D0DCF6949E13D6943'}]")

        item = self.driver.find_element(
            By.XPATH, "//input[@id='u']")
        item.send_keys("3452644866")

        item = self.driver.find_element(By.XPATH, "//input[@id='p']")
        item.send_keys("qq31415926")

        # item = self.driver.find_element(
        #     By.XPATH, "//div[@ht='click_pwdlogin_submitLogin']")
        # item.click()

        # cookie = self.driver.get_cookies()
        # print(cookie)
        # [{'domain': '.id1.cloud.huawei.com', 'expiry': 1908869785, 'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': True, 'value': '2049382e3828ef4470bef8b426c4bb3370e7d9e1147f53a18839e47dad7caf10a233e61ee15337b4373e'}, {'domain': '.id1.cloud.huawei.com', 'expiry': 1908869785, 'httpOnly': False, 'name': 'hwid_cas_sid', 'path': '/', 'secure': True, 'value': '2049382e3828ef4470bef8b426c4bb3370e7d9e1147f53a18839e47dad7caf10a233e61ee15337b4373e'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_idts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1593336984125'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_id_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': 'cf787be41ac24d65887dcd20c826ac97'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_idvc_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1593338788, 'httpOnly': False, 'name': 'HW_idn_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': 'ec569450f0ac4cd78fc72965d91ec7e8'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1608888984, 'httpOnly': False, 'name': 'HW_refts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1593336984124'}, {'domain': '.id1.cloud.huawei.com', 'httpOnly': True, 'name': 'CAS_THEME_NAME', 'path': '/', 'secure': True, 'value': 'red'}, {'domain': 'id1.cloud.huawei.com', 'httpOnly': False, 'name': 'cookieBannerOnOff', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.id1.cloud.huawei.com', 'httpOnly': True, 'name': 'VERSION_NO', 'path': '/', 'secure': True, 'value': 'UP_CAS_4.0.4.100'}, {'domain': 'id1.cloud.huawei.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/CAS', 'secure': True, 'value': '144E8B2ED3F5D9C8576742C1DDF4CF3D0DCF6949E13D6943'}]

    def Init(self):
        # 创建chrome浏览器驱动，无头模式（超爽）
        chrome_options = Options()
        # chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # 全屏
        self.driver.maximize_window()
        # 具体大小
        # driver.set_window_size(width, height)

        # self.GoHome()
        # self.Login()
        # time.sleep(2)
        # GoAppgallery(driver)

        #     # 快照显示已经成功登录
        # print(driver.save_screenshot('jietu.png'))
        # driver.quit()

    def Quit(self):
        self.driver.quit()

# 3452644866 qq31415926
    def CreateApp(self,isHD):
        self.driver.get("https://adnet.qq.com/medium/add")
        time.sleep(1)

        # Android平台
        item = self.driver.find_element(
            By.XPATH, "//button[@data-id='mediumTypeSelector']")
        item.click()

        time.sleep(1)

        list = self.driver.find_elements(
            By.XPATH, "//a[@role='option']")
        list[0].click()

        # 应用商店

        item = self.driver.find_element(
            By.XPATH, "//button[@data-id='appStoreSelector']")
        item.click()

        time.sleep(1)

        ul_list = self.driver.find_elements(
            By.XPATH, "//ul[@class='dropdown-menu inner']")

        list = ul_list[1].find_elements(
            By.XPATH, "//a[@role='option']")
        list[7].click()



    # 应用分类
        item = self.driver.find_element(
            By.XPATH, "//button[@data-id='industryOneSelector']")
        item.click()
        time.sleep(1)
        ul_list = self.driver.find_elements(
        By.XPATH, "//ul[@class='dropdown-menu inner']")
        list = ul_list[2].find_elements(
            By.XPATH, "//a[@role='option']")
        list[12].click()


        item = self.driver.find_element(
            By.XPATH, "//button[@data-id='industrySecondSelector']")
        item.click()
        time.sleep(1)
        ul_list = self.driver.find_elements(
        By.XPATH, "//ul[@class='dropdown-menu inner']")
        list = ul_list[3].find_elements(
            By.XPATH, "//a[@role='option']")
        list[3].click()
        



        # url
        item = self.driver.find_element(
            By.XPATH, "//input[@class='form-control size-410 form-control']")
        item.send_keys("http://appstore.huawei.com/c1000")
        
        # name
        list = self.driver.find_elements(
            By.XPATH, "//input[@id='placementName']")
        list[0].send_keys("appname")

        list = self.driver.find_elements(
            By.XPATH, "//input[@id='placementName']")
        list[1].send_keys("keyname")
        

        item = self.driver.find_element_by_id('formControlsTextarea')
        item.send_keys("detail")


        item = self.driver.find_element(
            By.XPATH, "//input[@id='packageName']")
        # package = appname.GetPackage(source.ANDROID,isHD)
        # item.send_keys(package)
        


        # 创建
        
        item = self.driver.find_element(
            By.XPATH, "//a[@class='btn btn-primary btn-160']")
        item.click()


# 主函数的实现
if __name__ == "__main__":
    # 设置为utf8编码
    # reload(sys)
    # sys.setdefaultencoding("utf-8")

    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1, count):
        print("参数", i, sys.argv[i])
        if i == 1:
            cmdPath = sys.argv[i]

     
    # cmdPath = cmdPath.replace("ad\\", "")

    dir = common.getLastDirofDir(cmdPath)
    dir = common.getLastDirofDir(dir)
    common.SetCmdPath(dir)
    print(cmdPath)
    ad = AdGdt()
    ad.SetCmdPath(cmdPath)
    ad.Init()
    ad.GoHome()
    ad.Login()
    ad.CreateApp(False)
    ad.CreateApp(True)
    print("AdGdt sucess")
