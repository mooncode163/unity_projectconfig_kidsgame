# 导入selenium的浏览器驱动接口


import sys
import os
import json
o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径
 
import AppInfo
import win32con
import win32gui
import sqlite3
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from common import source
from common import common
from AppStoreBase import AppStoreBase

# 要想调用键盘按键操作需要引入keys包

# 导入chrome选项


# pip3 install pywin32

# sys.path.append('../common')


class AppStoreHuawei(AppStoreBase):  

  

    def GoHome(self,isHD):  
        appid = AppInfo.GetAppId(isHD, source.HUAWEI)
        url = "https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myApp"
        print(url)
        self.driver.get(url)
        self.urlold = self.driver.current_url
        time.sleep(1)

     

    def Login(self,user,password):
        # 3452644866 
        print("waiting for login")
        while True:
            time.sleep(1)
            self.urlnew = self.driver.current_url
            if self.urlnew!=self.urlold:
                break
        
        
        return
        # driver.add_cookie("[{'domain': '.id1.cloud.huawei.com', 'expiry': 1908869785, 'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': True, 'value': '2049382e3828ef4470bef8b426c4bb3370e7d9e1147f53a18839e47dad7caf10a233e61ee15337b4373e'}, {'domain': '.id1.cloud.huawei.com', 'expiry': 1908869785, 'httpOnly': False, 'name': 'hwid_cas_sid', 'path': '/', 'secure': True, 'value': '2049382e3828ef4470bef8b426c4bb3370e7d9e1147f53a18839e47dad7caf10a233e61ee15337b4373e'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_idts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1593336984125'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_id_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': 'cf787be41ac24d65887dcd20c826ac97'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_idvc_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1593338788, 'httpOnly': False, 'name': 'HW_idn_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': 'ec569450f0ac4cd78fc72965d91ec7e8'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1608888984, 'httpOnly': False, 'name': 'HW_refts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1593336984124'}, {'domain': '.id1.cloud.huawei.com', 'httpOnly': True, 'name': 'CAS_THEME_NAME', 'path': '/', 'secure': True, 'value': 'red'}, {'domain': 'id1.cloud.huawei.com', 'httpOnly': False, 'name': 'cookieBannerOnOff', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.id1.cloud.huawei.com', 'httpOnly': True, 'name': 'VERSION_NO', 'path': '/', 'secure': True, 'value': 'UP_CAS_4.0.4.100'}, {'domain': 'id1.cloud.huawei.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/CAS', 'secure': True, 'value': '144E8B2ED3F5D9C8576742C1DDF4CF3D0DCF6949E13D6943'}]")
        

        item = self.driver.find_element(
            By.XPATH, "//input[@id='u']")
        item.send_keys(user)

        item = self.driver.find_element(By.XPATH, "//input[@id='p']")
        item.send_keys(password)

        item = self.driver.find_element(
            By.XPATH, "//input[@id='login_button']")
        item.click()
        time.sleep(5)

        # cookie = self.driver.get_cookies()
        # print(cookie)
        # [{'domain': '.id1.cloud.huawei.com', 'expiry': 1908869785, 'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': True, 'value': '2049382e3828ef4470bef8b426c4bb3370e7d9e1147f53a18839e47dad7caf10a233e61ee15337b4373e'}, {'domain': '.id1.cloud.huawei.com', 'expiry': 1908869785, 'httpOnly': False, 'name': 'hwid_cas_sid', 'path': '/', 'secure': True, 'value': '2049382e3828ef4470bef8b426c4bb3370e7d9e1147f53a18839e47dad7caf10a233e61ee15337b4373e'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_idts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1593336984125'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_id_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': 'cf787be41ac24d65887dcd20c826ac97'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_idvc_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1593338788, 'httpOnly': False, 'name': 'HW_idn_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': 'ec569450f0ac4cd78fc72965d91ec7e8'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1608888984, 'httpOnly': False, 'name': 'HW_refts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1593336984124'}, {'domain': '.id1.cloud.huawei.com', 'httpOnly': True, 'name': 'CAS_THEME_NAME', 'path': '/', 'secure': True, 'value': 'red'}, {'domain': 'id1.cloud.huawei.com', 'httpOnly': False, 'name': 'cookieBannerOnOff', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.id1.cloud.huawei.com', 'httpOnly': True, 'name': 'VERSION_NO', 'path': '/', 'secure': True, 'value': 'UP_CAS_4.0.4.100'}, {'domain': 'id1.cloud.huawei.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/CAS', 'secure': True, 'value': '144E8B2ED3F5D9C8576742C1DDF4CF3D0DCF6949E13D6943'}]
 
    
# 3452644866 qq31415926
    def CreateApp(self, isHD):
        # ad.GoHome(isHD)
        time.sleep(1)

        # Android平台
        item = self.driver.find_element(
            By.XPATH, "//button[@data-id='mediumTypeSelector']")
        item.click()

        time.sleep(1)

        list = self.driver.find_elements(
            By.XPATH, "//a[@role='option']")

        if self.osApp == source.ANDROID:
            list[0].click()

        if self.osApp == source.IOS:
            list[1].click()

        # 应用商店

        item = self.driver.find_element(
            By.XPATH, "//button[@data-id='appStoreSelector']")
        item.click()

        time.sleep(1)

        ul_list = self.driver.find_elements(
            By.XPATH, "//ul[@class='dropdown-menu inner']")

        list = ul_list[1].find_elements(
            By.XPATH, "//a[@role='option']")
        
        if self.osApp == source.ANDROID:
            list[7].click()

        if self.osApp == source.IOS:
            list[0].click()


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
        
        
        url = ""
        if self.osApp == source.ANDROID:
            appid = AppInfo.GetAppId(isHD, source.HUAWEI)
            url = "http://appstore.huawei.com/C"+appid

        if self.osApp == source.IOS:
            appid = AppInfo.GetAppId(isHD, source.APPSTORE)
            # https://itunes.apple.com/cn/app/id1303020002
            url = "https://itunes.apple.com/cn/app/id"+appid
        
        item.send_keys(url)

        # name
        name = self.GetAppName(isHD)
        list = self.driver.find_elements(
            By.XPATH, "//input[@id='placementName']")
        list[0].send_keys(name)

        list = self.driver.find_elements(
            By.XPATH, "//input[@id='placementName']")
        list[1].send_keys(name)

        item = self.driver.find_element_by_id('formControlsTextarea')
        name += name
        name += name
        name += name
        name += name
        item.send_keys(name)

        item = self.driver.find_element(
            By.XPATH, "//input[@id='packageName']")
        package = AppInfo.GetPackage(source.ANDROID, isHD)
        item.send_keys(package)

        # 创建

        item = self.driver.find_element(
            By.XPATH, "//a[@class='btn btn-primary btn-160']")
        item.click()


    def GetAppName(self, ishd):
        name = AppInfo.GetAppName(self.osApp, ishd)
        # if self.osApp == source.IOS:
        #     AppInfo.GetAppName(self.osApp, ishd)+self.osApp

        return name

    def SearchApp(self, ishd):
        name = self.GetAppName(ishd) 
        item = self.driver.find_element(
            By.XPATH, "//input[@ng-model='Model.product.query.appName']")
        item.send_keys(name)
        time.sleep(1)
  
        # search
        self.driver.find_element_by_id('search_medium_id').click()
        time.sleep(2)
  

    def UpdateApp(self, isHD):
        # 打开新标签
        # self.driver.find_element_by_xpath('//body').send_keys(Keys.CONTROL,"t")
        # js = "window.open('')"
        # self.driver.execute_script(js)
        # time.sleep(2)

        appid = AppInfo.GetAppId(isHD, source.HUAWEI)
        # https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myApp/101054959 
        url = "https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myApp/"+appid
        self.driver.get(url) 
        time.sleep(3)
        item = self.driver.find_element(By.XPATH, "//span[@class='green-circle']")
        item.click()
        time.sleep(5)


        self.driver.switch_to.frame("mainIframeView")

        item = self.driver.find_element(By.XPATH, "//a[@id='VersionUpgradeButton']")
        # item = self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary button-normal ml-2 ng-binding ng-scope']")
        
        item.click()
        time.sleep(3)

        self.driver.switch_to.frame("mainIframeView")
        time.sleep(1)
        # 软件包管理
        item = self.driver.find_element(By.XPATH, "//a[@id='VerInfoDownloadLink']")
        #  Message: element click intercepted
        self.driver.execute_script("arguments[0].click();", item)
        # item.click()
        time.sleep(1)
        
        item = self.driver.find_element(By.XPATH, "//a[@id='ManageAppUploadPackageButton']")
        item.click()
        time.sleep(1)
        

        # self.driver.switch_to.frame("mainIframeView")
        # item = self.driver.find_element(By.XPATH, "//input[@type='file']")
        # item = self.driver.find_element(By.XPATH, "//div[@class='uploader-pick']")
        item = self.driver.find_element(By.XPATH, "//div[@id='uploaderSelectContainer']")
        item.click()
        time.sleep(2)
        #  Message: element click intercepted
        # self.driver.execute_script("arguments[0].click();", item)
        # time.sleep(10)
        
        rootdir = "F:\\sourcecode\\unity\\product\\kidsgame\\ProjectOutPut"
        apk = common.GetOutPutApkPathWin32(rootdir,source.HUAWEI,isHD)
        print(apk)
        # F:\\sourcecode\\unity\\product\\kidsgame\\ProjectOutPut\\xiehanzi\\hanziyuan\\screenshot\\shu\\cn\\480p\\1.jpg
        self.OpenFileBrowser(apk,True)

        time.sleep(1)
 
     
        # <div class="uploader-progress-bar" ng-style="{width: uploadProgress}"></div>

        # # <div class="progress"><div class="progress-bar" style="width: 82%;" aria-valuenow="82"></div></div>
        isUploading = False
        while True:
            time.sleep(1)
            key = "//div[@class='uploader-progress-bar']"
            if self.IsElementExist(key):
                item = self.driver.find_element(By.XPATH, key)
                if item is not None:
                    style = item.get_attribute('style') 
                    isUploading = True
                    print(style)
                    # if style.find("100") >=0:
                    #     time.sleep(1)
                    #     print("upload apk finish")
                    #     break
            else:
                if isUploading == True:
                    isUploading = False
                    time.sleep(1)
                    print("upload apk finish")
                    break



        
        time.sleep(1)

        # 不申请
        item = self.driver.find_element(By.XPATH, "//span[@id='VerInfoNotApplyButton']")
        item.click()
        time.sleep(1)


        # 提交审核
        item = self.driver.find_element(By.XPATH, "//a[@id='VerInfoSubmitButton']")
        item.click()
        time.sleep(3)

        # 确定
        item = self.driver.find_element(By.XPATH, "//a[@id='AppSubmitConfirmButtonOk']")
        item.click()
        time.sleep(3)


    def GetAppName(self, ishd):
        name = AppInfo.GetAppName(self.osApp, ishd)
        # if self.osApp == source.IOS:
        #     AppInfo.GetAppName(self.osApp, ishd)+self.osApp

        return name
 
    def SearchApp(self, ishd):
        name = self.GetAppName(ishd)
        self.driver.get("https://adnet.qq.com/medium/list")
        time.sleep(2)
        item = self.driver.find_element(
            By.XPATH, "//input[@class='form-control']")
        time.sleep(1)

        item.send_keys(name)
        # item.send_keys("儿童写汉字")

        time.sleep(1)

        # search
        self.driver.find_element_by_id('search_medium_id').click()
        time.sleep(2)
 
        # 筛选
        item = self.driver.find_element(By.XPATH, "//button[@class='btn filter-operate']")
        # item = self.driver.find_element(By.XPATH, "//div[@class='filter-parent-control']")

        # error
        # item.click()  
        self.driver.execute_script("arguments[0].click();", item)
        time.sleep(2)

# <input type="checkbox" class="check" name="" value="IOS"> 
        if self.osApp == source.ANDROID:
            item = self.driver.find_element(By.XPATH, "//input[@value='Android']")
            # item.click()
            self.driver.execute_script("arguments[0].click();", item)
            time.sleep(1)

        if self.osApp == source.IOS:
            item = self.driver.find_element(By.XPATH, "//input[@value='IOS']")
            # item.click()
            self.driver.execute_script("arguments[0].click();", item)
            time.sleep(1)
         
        # 确定
        item = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        # item.click()
        self.driver.execute_script("arguments[0].click();", item)
        time.sleep(2)


        # 点击第一个
        item = self.driver.find_element(By.XPATH, "//div[@class='media']")
        item.click()
        time.sleep(1)
 



    


# 主函数的实现
if __name__ == "__main__":
    # 设置为utf8编码
    # reload(sys)
    # sys.setdefaultencoding("utf-8")

    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)

    isHD = False
    for i in range(1, count):
        print("参数", i, sys.argv[i])
        if i == 1:
            cmdPath = sys.argv[i]

        if i == 3:
            if sys.argv[i] == "hd":
                isHD = True


   

  

    # cmdPath = cmdPath.replace("ad\\", "")

    dir = common.getLastDirofDir(cmdPath)
    # dir = common.getLastDirofDir(dir)
    common.SetCmdPath(dir)
  

    ad = AppStoreHuawei()
    ad.SetCmdPath(cmdPath)
    ad.Init()
    ad.GoHome(False)
    ad.Login("chyfemail163@163.com","Qianlizhiwai1")

    argv1 = sys.argv[2]
    # ad.osApp = sys.argv[3]
    if argv1 == "createapp":
        ad.CreateApp(False)
        time.sleep(3)
        ad.CreateApp(True)
 
    if argv1 == "update":
        # ad.UpdateApp(isHD)
        ad.UpdateApp(False)
        time.sleep(3)
        ad.UpdateApp(True)

 
    ad.Quit(30)


    print("AppStoreHuawei sucess")
