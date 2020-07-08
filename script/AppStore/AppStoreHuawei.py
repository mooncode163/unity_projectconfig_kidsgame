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
from WebDriverCmd import CmdType
from WebDriverCmd import WebDriverCmd 
from WebDriverCmd import CmdInfo 


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
        self.FillAppInfo(isHD)
        return

        webcmd = WebDriverCmd(self.driver)
        old_window = self.driver.current_window_handle
        url = "https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myApp"
        self.driver.get(url)
        time.sleep(1) 

        # 跳转到新的页面
        print("self.driver.current_url=", self.driver.current_url)
        # self.driver.switch_to.window(self.driver.window_handles[0])
        for win in self.driver.window_handles:
            if win != old_window:
                self.driver.switch_to.window(win)
        time.sleep(1)
        print("self.driver.current_url 2=", self.driver.current_url)

        self.driver.switch_to.frame("mainIframeView")
        
        
        webcmd.AddCmd(CmdType.CLICK, "//a[@id='MyAppListNewApp']", "", 1)
        webcmd.Run(True) 
        
        title = self.GetAppName(isHD, source.LANGUAGE_CN)
        webcmd.AddCmd(CmdType.INPUT, "//input[@ng-model='Model.productAndApp.appName']", title, 1)  
        webcmd.Run(True)
 
        old_window = self.driver.current_window_handle
        # waiting 确定
        while True:
            time.sleep(1)
            if self.IsElementExist("//a[@id='PubProDetermine']")==False:
                break
        
        
        print("self.driver.current_url=", self.driver.current_url)
        # self.driver.switch_to.window(self.driver.window_handles[0])
        for win in self.driver.window_handles:
            if win != old_window:
                self.driver.switch_to.window(win)
        time.sleep(1)

        self.driver.switch_to.frame("mainIframeView")
        
        item = self.driver.find_element(By.XPATH, "//span[@id='AppInfoAppIdContent']") 
        appid = item.text
        print(appid)
        AppInfo.SetAppId(isHD, source.ANDROID, source.HUAWEI, appid)
        
    
    def AddLanguage(self,webcmd, title):
        webcmd.AddCmd2(CmdType.CLICK, "//a[@id='AppInfoManageLanguageButton']") 
        webcmd.AddCmd(CmdType.INPUT, "//input[@ng-model='searchTxt']",title,1)

        key = "//span[@title='"+title+"']"
        print(key)
        if self.IsElementExist(key):
            webcmd.AddCmd2(CmdType.CLICK, key)
            webcmd.AddCmd2(CmdType.CLICK, "//label[@class='checkbox lang-item ng-scope']") 
        else:
            print(key,"is not exit")

        webcmd.AddCmd2(CmdType.CLICK, "//label[@class='checkbox lang-item ng-scope']") 

        webcmd.AddCmd2(CmdType.CLICK, "//a[@class='btn btn-primary btn-small ng-binding']")
        webcmd.Run(True) 
        time.sleep(2) 

    def FillLanguage(self,webcmd, isHD,lanName,lanKey):
  
        # 选择语言 
        # webcmd.AddCmd(CmdType.CLICK, "//input[@type='search' and @aria-owns='ui-select-choices-3']", "", 1)
        webcmd.AddCmd(CmdType.CLICK, "//span[@class='ui-select-match-text pull-left']", "", 2)
        
        # 简体中文-默认
        if lanName =="简体中文":
            lanName = lanName+"-默认"

        key = "//div[@class='ucd-droplist-option ng-binding' and text()='"+lanName+"']" 
        # key = "//div[@class='ucd-droplist-option ng-binding' and text()='"+lanName+"-默认"+"']" 
        # if self.IsElementExist(key)==False:
        #     key = "//div[@class='ucd-droplist-option ng-binding' and text()='"+lanName+"']" 
            
        # 模糊匹配
        # key = "//div[@class='ucd-droplist-option ng-binding' and contains(text(),'"+lanName+"')]"  

        webcmd.AddCmd(CmdType.CLICK, key, "", 1) 
        webcmd.Run(True)


        title = self.GetAppName(isHD,lanKey)
        webcmd.AddCmd(CmdType.INPUT, "//input[@id='AppInfoAppNameInputBox']",title,3) 
        webcmd.Run(True)

        title = self.GetAppDetail(isHD,lanKey)
        webcmd.AddCmd(CmdType.INPUT, "//textarea[@id='AppInfoAppIntroduceInputBox']",title,2) 
        webcmd.Run(True)
        time.sleep(5)

        title = self.GetAppPromotion(isHD,lanKey)
        webcmd.AddCmd(CmdType.INPUT, "//input[@id='AppInfoAppBriefInputBox']",title,3) 
        webcmd.Run(True)
        time.sleep(2)


        # icon 
        key = "//img[@id='AppInfoAppIconAddButton']" 
        webcmd.AddCmd(CmdType.CLICK, key, "", 2)
        icon = common.GetOutPutIconPathWin32(self.rootDirProjectOutPut, source.TAPTAP, isHD)+"\\huawei\\icon_android_216.png"
        print(icon)
        webcmd.Run(True)
        self.OpenFileBrowser(icon, True)
        time.sleep(3)
             
   
#    <span class="text ng-binding">横向截图</span>

        # key = "//img[@id='AppIntroScreenshot1']" 
        # webcmd.AddCmd(CmdType.CLICK, key, "", 2)
        # i = 0
        # pic = common.GetOutPutScreenshotPathWin32(self.rootDirProjectOutPut, source.TAPTAP, isHD) + "\\"+lanKey+"\\1080p\\"+str(i+1)+".jpg"
        # print(pic)
        # webcmd.Run(True)
        # self.OpenFileBrowser(pic, True)
        # time.sleep(2)


    def FillAppInfo(self, isHD):
        webcmd = WebDriverCmd(self.driver) 
        old_window = self.driver.current_window_handle
        appid = AppInfo.GetAppId(isHD, source.HUAWEI) 
        url = "https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myApp/"+appid
        print(url)
        self.driver.get(url) 
        time.sleep(3) 

       # 跳转到新的页面
        print("self.driver.current_url=", self.driver.current_url)
        # self.driver.switch_to.window(self.driver.window_handles[0])
        for win in self.driver.window_handles:
            if win != old_window:
                self.driver.switch_to.window(win)
        time.sleep(1)
        print("self.driver.current_url 2=", self.driver.current_url)
        
        self.driver.switch_to.frame("mainIframeView")

        lanKeys =("简体中文", "英式英语","美式英语")
        applans = (source.LANGUAGE_CN,source.LANGUAGE_EN, source.LANGUAGE_EN)

        # 添加语言
        for lan in range(0, len(lanKeys)): 
            self.AddLanguage(webcmd,lanKeys[lan])
 

        for lan in range(0, len(lanKeys)):
            self.FillLanguage(webcmd,isHD,lanKeys[lan],applans[lan]) 


        return  
        rootdir = "F:\\sourcecode\\unity\\product\\kidsgame\\ProjectOutPut"
        apk = common.GetOutPutApkPathWin32(rootdir,source.HUAWEI,isHD)
        print(apk)
        # F:\\sourcecode\\unity\\product\\kidsgame\\ProjectOutPut\\xiehanzi\\hanziyuan\\screenshot\\shu\\cn\\480p\\1.jpg
        self.OpenFileBrowser(apk,True)

        time.sleep(2)
 
     
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


    def SearchApp(self, ishd):
        name = self.GetAppName(isHD, source.LANGUAGE_CN)
        item = self.driver.find_element(
            By.XPATH, "//input[@ng-model='Model.product.query.appName']")
        item.send_keys(name)
        time.sleep(1)
  
        # search
        self.driver.find_element_by_id('search_medium_id').click()
        time.sleep(2)
  

    def UpdateApp(self, isHD):
        webcmd = WebDriverCmd(self.driver)
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
        # item = self.driver.find_element(By.XPATH, "//a[@id='VerInfoDownloadLink']")
        # #  Message: element click intercepted
        # self.driver.execute_script("arguments[0].click();", item)
        # # item.click()
        # time.sleep(1)
        info = CmdInfo()
        info.type = CmdType.CLICK
        info.cmd = "//a[@id='VerInfoDownloadLink']"
        info.value = ""
        info.delay = 1
        info.isWaiting = True
        webcmd.AddCmdInfo(info)
        webcmd.Run(True)
        
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
 
 
    def SearchApp(self, ishd):
        name = self.GetAppName(isHD, source.LANGUAGE_CN)
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
    ad.GoHome(isHD)
    ad.Login("chyfemail163@163.com","Qianlizhiwai1")

    argv1 = sys.argv[2]
    # ad.osApp = sys.argv[3]
    if argv1 == "createapp":
        # ad.CreateApp(False)
        time.sleep(3)
        ad.CreateApp(True)
 
    if argv1 == "update":
        if isHD:
            ad.UpdateApp(True)
        else:
            ad.UpdateApp(False)
            time.sleep(3)
            # ad.UpdateApp(True)

 
    # ad.Quit(300)


    print("AppStoreHuawei sucess")
