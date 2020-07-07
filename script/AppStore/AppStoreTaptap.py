# 导入selenium的浏览器驱动接口
import sys
import os
import json
o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径

from WebDriverCmd import CmdType
from WebDriverCmd import WebDriverCmd 
from AppStoreBase import AppStoreBase
from common import common
from common import source
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sqlite3
import win32gui
import win32con
import AppInfo



# 要想调用键盘按键操作需要引入keys包

# 导入chrome选项


# pip3 install pywin32

# sys.path.append('../common')


class AppStoreTaptap(AppStoreBase):

    def GoHome(self, isHD, login):
        # self.driver.get("https://www.taptap.com/developer")
        # self.driver.get("https://www.taptap.com/developer/dashboard/14628/apps")
        # app
        # https://www.taptap.com/developer/dashboard/14628?app_id=56016
        # https://www.taptap.com/developer/dashboard/14628/apps
        appid = AppInfo.GetAppId(isHD, source.TAPTAP)
        print("GoHome appid=", appid, " isHD="+str(isHD))
        # url = "https://www.taptap.com/developer/dashboard/14628?app_id="+appid
        url = "https://www.taptap.com/developer/dashboard/14628/apps"
        #
        print(url)
        self.driver.get(url)
        time.sleep(1)

        if login == True:
            # <div class="icon-font ic_qq"></div>
            # 跳转qq登录
            item = self.driver.find_element(
                By.XPATH, "//div[@class='icon-font ic_qq']")
            item.click()
            time.sleep(1)

    def Login(self, user, password):
        self.urlold = self.driver.current_url
        print("Login urlold=", self.urlold)
        self.LoginQQ(user, password)

        # 等待登录成功
        while True:
            time.sleep(1)
            self.urlnew = self.driver.current_url
            print("Login urlnew=", self.urlnew)
            if self.urlnew != self.urlold:
                print("Login Finish =", self.urlnew)
                break


# 3452644866 qq31415926
    def SelectLanguage(self,webcmd, lan):  
        if lan == 0:
            # 填写中文资料
                # webcmd.AddCmd(  CmdType.CLICK, "//li[@class='nav-item js-chs-contents-li js-spec-lang-li']", "", 1)
                # <a class="nav-link" data-toggle="tab" href="#chs-contents" role="tab" aria-controls="chs" aria-selected="true" aria-expanded="true">简体中文</a>
            webcmd.AddCmd(  CmdType.CLICK, "//a[@aria-controls='chs']", "", 2) 
            webcmd.Run(True)
        if lan == 1:
                # 填写英文资料
                # webcmd.AddCmd(  CmdType.CLICK, "//li[@class='nav-item js-en-contents-li js-spec-lang-li active']", "", 1)
            webcmd.AddCmd(  CmdType.CLICK, "//a[@aria-controls='en']", "", 2)
            webcmd.Run(True)  
                
    def CreateApp(self, isHD):
        url = "https://www.taptap.com/developer/app-create/14628"
        self.driver.get(url)
        time.sleep(1)
        self.UpLoadApk(isHD)
 
        # url = "https://www.taptap.com/developer/fill-form/14628"
        # self.driver.get(url)
        # time.sleep(1)


        webcmd = WebDriverCmd(self.driver)
        


        #
        webcmd.AddCmd(CmdType.CLICK, "//select[@id='developer_type']", "", 1)
        webcmd.Run(True)

        list = self.driver.find_elements(
            By.XPATH, "//select[@id='developer_type']/option")
        list[3].click()
        time.sleep(1)

        webcmd.AddCmd(CmdType.CLICK, "//select[@id='category']", "", 1)
        webcmd.Run(True)

        list = self.driver.find_elements(
            By.XPATH, "//select[@id='category']/option")
        list[1].click()
        time.sleep(1)

        webcmd.AddCmd(
            CmdType.CLICK, "//input[@type='checkbox' and @value='zh_CN']", "", 1)
        webcmd.AddCmd(
            CmdType.CLICK, "//input[@type='checkbox' and @value='en_US']", "", 1)

        webcmd.AddCmd(CmdType.CLICK, "//input[@id='area_available_cn']", "", 1)
        webcmd.AddCmd(CmdType.CLICK, "//input[@id='area_available_tw']", "", 1)

        # 管理多语言
        webcmd.AddCmd(CmdType.CLICK, "//a[@id='manage-trans-btn']", "", 1)
        webcmd.AddCmd(CmdType.CLICK, "//input[@id='trans-select-chs']", "", 1)
        webcmd.AddCmd(CmdType.CLICK, "//input[@id='trans-select-en']", "", 1)
        webcmd.AddCmd(CmdType.CLICK, "//button[@id='manage-trans-submit']", "", 1)

        webcmd.Run(True)


        # webcmd.AddCmd(  CmdType.CLICK, "//a[@aria-controls='chs']", "", 1)
        # webcmd.Run(True)
        # key = "//input[@type='file' and @data-target='#banner_1_android-"+"cn"+"']"
        # key = "//input[@data-target='#banner_1_android']"
        # key = "//input[@data-target='#icon']"
        # key = "//input[@type='file' and @data-target='#icon']"
        # key = "//input[@type='file' and @data-target='#icon-zh_CN']" 

        # #icon
        # # key ="//input[@id='banner_1_android-input']"
        # # key ="//span[@class='fileinput-button fixed-size banner']"
        

        # # 
        # #banner_1_android
        # # webcmd.AddCmd(CmdType.CLICK, key, "", 1)
        # # webcmd.Run(True)
        # item = self.driver.find_element(By.XPATH, key)
        # item.click() 
        # # item.send_keys(Keys.ENTER)
        # time.sleep(1)
        # pic = common.GetOutPutAdPathWin32(self.rootDirProjectOutPut, source.TAPTAP, isHD) + "\\"+"cn"+"\\"+"ad_home_1024x500.png"
        # self.OpenFileBrowser(pic, True)
        # time.sleep(3)
        # return



        # zh_CN en_US
        lanKeys =("zh_CN", "en_US")
        applans = (source.LANGUAGE_CN, source.LANGUAGE_EN)
        for lan in range(0, len(lanKeys)):
            # if lan == 0:
            #     # 填写中文资料
            #     # webcmd.AddCmd(  CmdType.CLICK, "//li[@class='nav-item js-chs-contents-li js-spec-lang-li']", "", 1)
            #     # <a class="nav-link" data-toggle="tab" href="#chs-contents" role="tab" aria-controls="chs" aria-selected="true" aria-expanded="true">简体中文</a>
            #     webcmd.AddCmd(  CmdType.CLICK, "//a[@aria-controls='chs']", "", 2) 
            #     webcmd.Run(True)
            # if lan == 1:
            #     # 填写英文资料
            #     # webcmd.AddCmd(  CmdType.CLICK, "//li[@class='nav-item js-en-contents-li js-spec-lang-li active']", "", 1)
            #     webcmd.AddCmd(  CmdType.CLICK, "//a[@aria-controls='en']", "", 2)
            #     webcmd.Run(True)
            self.SelectLanguage(webcmd,lan)

            # title "//input[@type='text' and @name='translations[zh_CN][title]']"
            print(lanKeys[lan])
            key = "//input[@type='text' and @name='translations[" + lanKeys[lan]+"][title]']"

            print(key)
            title = self.GetAppName(isHD, applans[lan])
            webcmd.AddCmd(CmdType.INPUT, key, title, 1)
            # detail "//textarea[@name='translations[zh_CN][description]']"
            key = "//textarea[@name='translations[" +  lanKeys[lan]+"][description]']"
            title = self.GetAppDetail(isHD, applans[lan])
            webcmd.AddCmd(CmdType.INPUT, key, title, 1)
            webcmd.Run(True)

       

            # title = self.GetAppName(isHD, applans[lan])
            # webcmd.AddCmd(CmdType.INPUT, key, title, 1)
            # webcmd.Run(True)


            # icon
            # <input type="file" name="image" data-valid-width="512" data-valid-height="512" data-taptap-ajax="upload" data-target="#icon-zh_CN" data-target-input="#icon-input-zh_CN" data-url="https://www.taptap.com/ajax/image">
            # "//input[@type='file' and @data-target='#icon-zh_CN']"
            key = "//input[@type='file' and @data-target='#icon-" +   lanKeys[lan]+"']"
            # key = "//input[@type='file' and @data-target='#icon']"
            print(key)
            # self.driver.switch_to.window(self.driver.window_handles[0])
            webcmd.AddCmd(CmdType.CLICK, key, "", 2)
            icon = common.GetOutPutIconPathWin32(
                self.rootDirProjectOutPut, source.TAPTAP, isHD)+"\\icon_android_512.png"
            print(icon)
            webcmd.Run(True)
            self.OpenFileBrowser(icon, True)
            time.sleep(2)

            # adhome
            # self.SelectLanguage(webcmd,lan)
            # self.driver.switch_to.window(self.driver.window_handles[0])
            key = "//input[@type='file' and @data-target='#banner_1_android-"+lanKeys[lan]+"']"
            webcmd.AddCmd(CmdType.CLICK, key, "", 3)
            webcmd.Run(True)
            pic = common.GetOutPutAdPathWin32(self.rootDirProjectOutPut, source.TAPTAP, isHD) + "\\"+applans[lan]+"\\"+"ad_home_1024x500.png"
            print(pic)
            self.OpenFileBrowser(pic, True)
            time.sleep(3)
            
            # self.SelectLanguage(webcmd,lan)
            # self.driver.switch_to.window(self.driver.window_handles[0])
            key = "//input[@type='file' and @data-target='#banner_1_ios-"+lanKeys[lan]+"']"
            webcmd.AddCmd(CmdType.CLICK, key, "", 3)
            webcmd.Run(True)
            print(pic)
            self.OpenFileBrowser(pic, True)
            time.sleep(3)






            # screenshot
            for i in range(0, 5):
                # <input type="file" name="image" data-taptap-ajax="upload" data-target="#screenshots" data-url="https://www.taptap.com/ajax/image">
                # add-screenshot-li
                # self.driver.switch_to.window(self.driver.window_handles[0])
                webcmd.AddCmd(CmdType.CLICK, "//input[@type='file' and @data-target='#screenshots']", "", 3)
                # webcmd.AddCmd(CmdType.CLICK, "//li[@class='add-screenshot-li]", "", 1)
                webcmd.Run(True)
                pic = common.GetOutPutScreenshotPathWin32(self.rootDirProjectOutPut, source.TAPTAP, isHD) + "\\"+applans[lan]+"\\1080p\\"+str(i+1)+".jpg"
                
                flag = os.path.exists(pic)
                if flag:
                    print(pic)
                    self.OpenFileBrowser(pic, True)
                    time.sleep(5)


        # 发布状态
        webcmd.AddCmd( CmdType.CLICK, "//input[@type='radio' and @name='flag_android' and @value='4']", "", 1) 
        webcmd.Run(True)

        self.SubmitApp(False)

    def GoToAPPPage(self, isHD):
        appid = AppInfo.GetAppId(isHD, source.TAPTAP)
        url = "https://www.taptap.com/developer/dashboard/14628?app_id="+appid
        print(url)
        self.driver.get(url)
        time.sleep(1)

    def UpLoadApk(self, isHD):
        # <a data-toggle="modal" data-target=".confirm-upload-apk" class="btn btn-primary">上传APK</a>
        item = self.driver.find_element(
            By.XPATH, "//a[@data-target='.confirm-upload-apk']")
        # item = self.driver.find_element(By.XPATH, "//a[@data-toggle='modal']")
        item.click()
        time.sleep(2)

        # <a id="selectfiles" href="javascript:void(0);" class="btn btn-primary" style="position: relative; z-index: 1;">开始上传APK</a>
        item = self.driver.find_element(By.XPATH, "//a[@id='selectfiles']")
        item.click()
        time.sleep(2)

        self.urlold = self.driver.current_url
        old_window = self.driver.current_window_handle
        print("urlold=", self.urlold)
        # 手动点击上传
 
        apk = common.GetOutPutApkPathWin32(self.rootDirProjectOutPut, source.TAPTAP, isHD)
        # F:\\sourcecode\\unity\\product\\kidsgame\\ProjectOutPut\\xiehanzi\\hanziyuan\\screenshot\\shu\\cn\\480p\\1.jpg
        self.OpenFileBrowser(apk, True)
        time.sleep(1)

        # 檢查是否文件長傳結束
        while True:
            time.sleep(2)
            # for win in self.driver.window_handles:
            #     if win!=old_window:
            #         self.driver.switch_to.window(win)
            #         self.urlold = self.driver.current_url
            #         old_window = win
            #         print("urlold 2=",self.urlold)

            # self.driver.switch_to.window(self.driver.windowop_handles[0])
            self.urlnew = self.driver.current_url
            print("urlnew=", self.urlnew)
            if self.urlnew != self.urlold:
                print("new page =", self.urlnew)
                print("apk upload finish")
                break

        # <div class="progress"><div class="progress-bar" style="width: 82%;" aria-valuenow="82"></div></div>
        # while True:
        #     item = self.driver.find_element(By.XPATH, "//div[@class='progress']")
        #     if item is not None:
        #         value = item.get_attribute('aria-valuenow')
        #         int_v = int(value)
        #         if int_v>=100:
        #             break

        # time.sleep(1)

        # 手动等待上传
        # time.sleep(60*2)

    def SubmitApp(self,isYes):
        # 未成年人防沉迷
        # <input required="" type="radio" name="anti_addiction_read" value="1">
        item = self.driver.find_element(
            By.XPATH, "//input[@name='anti_addiction_read']")
        item.click()
        time.sleep(1)
        # <input required="required" type="radio" name="anti_addiction_status" value="1">
        item = self.driver.find_element(
            By.XPATH, "//input[@name='anti_addiction_status']")
        item.click()
        time.sleep(1)

        # 等待后台apk解析
        time.sleep(10)

        if isYes:
            # 提交审核
            # <button id="postAppSubmitV2" type="submit" value="submit" class="leave_current_page btn btn-primary btn-lg">保存并提交审核</button>
            item = self.driver.find_element(
                By.XPATH, "//button[@id='postAppSubmitV2']")
            item.click()
            time.sleep(1)

            # 确定

            # section = self.driver.find_element(By.XPATH, "//section[@class='modal fade taptap-modal global-tip-modal in']")
            # # <button class="btn btn-primary" data-default-text="确定">确定</button>
            # # item = self.driver.find_element(By.XPATH, "//button[@data-default-text='确定']")
            # item = section.find_element(By.XPATH, "//button[@data-default-text='确定']")
            list = self.driver.find_elements(
                By.XPATH, "//button[@data-default-text='确定']")
            item = list[1]
            print("确定")
            self.driver.execute_script("arguments[0].click();", item)
            time.sleep(1)

    def UpdateApp(self, isHD):
        appid = AppInfo.GetAppId(isHD, source.TAPTAP)
        # dir = self.rootDirProjectOutPut

        if appid == "0":
            self.SearchApp(isHD)
            time.sleep(1)

        self.GoToAPPPage(isHD)
        # print("UpdateApp appid=",appid," isHD="+isHD)
        # https://www.taptap.com/developer/app-update/56016/14628
        time.sleep(2)
        old_window = self.driver.current_window_handle
        key = "//a[@data-taptap-btn='updateAppData']"
        if self.IsElementExist(key):
            item = self.driver.find_element(By.XPATH, key)
            item.click()
            time.sleep(2)
        else:
            print("updateAppData button not find ")
            print("updateAppData current_url=", self.driver.current_url)
            self.UpdateApp(isHD)

        # 跳转到新的页面
        print("self.driver.current_url=", self.driver.current_url)
        # self.driver.switch_to.window(self.driver.window_handles[0])
        for win in self.driver.window_handles:
            if win != old_window:
                self.driver.switch_to.window(win)
        time.sleep(1)
        print("self.driver.current_url 2=", self.driver.current_url)

        self.UpLoadApk(isHD)

        # https://www.taptap.com/developer/fill-form/14628?apk_id=496448&app_id=56016

        self.SubmitApp(True)

    def SearchApp(self, ishd):
        name = self.GetAppName(ishd, source.LANGUAGE_CN)

        self.driver.get(
            "https://www.taptap.com/developer/dashboard/14628/apps")
        time.sleep(2)

        div = self.driver.find_element(
            By.XPATH, "//div[@class='developer-search-app']")
        time.sleep(1)

        item = div.find_element_by_xpath("input")
        item.send_keys(name)
        # item.send_keys("儿童写汉字")

        time.sleep(1)

        div = self.driver.find_element(
            By.XPATH, "//div[@class='dropdown search-app-dropdown']")
        list = div.find_elements_by_xpath("ul/li/a")
        for a in list:
            title = a.text
            print(title)
            if title.find(name) == 0:
                # app_id=56016
                url = a.get_attribute('href')
                strfind = "app_id="
                idx = url.find(strfind)+len(strfind)
                print(url)
                appid = url[idx:]
                print(appid)
                AppInfo.SetAppId(ishd, source.ANDROID, source.TAPTAP, appid)
                break


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
            print("check hd", i, sys.argv[i])
            if sys.argv[i] == "hd":
                print("isHD true")
                isHD = True

    # cmdPath = cmdPath.replace("ad\\", "")

    dir = common.getLastDirofDir(cmdPath)
    # dir = common.getLastDirofDir(dir)
    common.SetCmdPath(dir)

    ad = AppStoreTaptap()
    ad.SetCmdPath(cmdPath)
    ad.Init()
    ad.GoHome(isHD, True)
    ad.Login("651577315", "qq31415926")

    argv1 = sys.argv[2]
    # ad.osApp = sys.argv[3]
    if argv1 == "createapp":
        ad.CreateApp(False)
        time.sleep(3)
        ad.CreateApp(True)

    if argv1 == "update":
        if isHD == True:
            ad.UpdateApp(True)
        else:
            ad.UpdateApp(False)
            time.sleep(3)
            ad.UpdateApp(True)

    if argv1 == "getappid":
        ad.SearchApp(False)
        time.sleep(3)
        ad.SearchApp(True)

    # ad.Quit(30)

    print("AppStoreTaptap sucess")
