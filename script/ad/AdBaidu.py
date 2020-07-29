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

import pyperclip
from AppStore.WebDriverCmd import CmdType
from AppStore.WebDriverCmd import WebDriverCmd 
from AppStore.WebDriverCmd import CmdInfo 
from AppVersionHuawei import mainAppVersionHuawei

from AdBase import AdBase

# 要想调用键盘按键操作需要引入keys包

# 导入chrome选项


# pip3 install pywin32

# sys.path.append('../common')


class AdBaidu(AdBase):
    driver: None
    dirRoot: None
    urlCreatePlaceId: None
    osApp: None

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
        print("dir = ", dir)

    def GoHome(self):
        # 加载百度页面 
        # self.driver.get("https://union.baidu.com/")
        self.driver.get("https://union.baidu.com/bqt#/")
        
        time.sleep(2)



        

    def Login(self, user, password):
        self.urlold = self.driver.current_url
        print("Login urlold=", self.urlold)

        webcmd = WebDriverCmd(self.driver)
        webcmd.AddCmdWait(CmdType.CLICK_Action,"//div[@class='btn-login']")
        webcmd.Run(True) 


        webcmd.AddCmd(CmdType.INPUT,"//input[@id='uc-common-account']",user)
        webcmd.AddCmd(CmdType.INPUT,"//input[@id='ucsl-password-edit']",password)

        # 登录
        # <div class="login-action">
        # webcmd.AddCmd(CmdType.CLICK_Action,"//input[@id='submit-formt']")
        # webcmd.AddCmd(CmdType.CLICK_Action,"//div[@class='login-action']")

        webcmd.Run(True) 

        # self.LoginQQ(user, password)
        # self.SaveCookie()
        # 等待登录成功
        while True:
            time.sleep(1)
            self.urlnew = self.driver.current_url
            print("Login urlnew=", self.urlnew)
            if self.urlnew != self.urlold:
                print("Login Finish =", self.urlnew)
                break
 
 
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


    def SetText(self, key,title): 
        webcmd = WebDriverCmd(self.driver)
        pyperclip.copy(title) 
        pyperclip.paste()
        webcmd.AddCmd2(CmdType.CLICK, key)
        webcmd.AddCmd2(CmdType.CTR_V, key) 
        webcmd.Run(True)



    def DeleteAllDownloadApk(self,sourceDir):
        for file in os.listdir(sourceDir):
            sourceFile = os.path.join(sourceDir,  file)
                #cover the files
            if os.path.isfile(sourceFile):
                # print sourceFile
                # 分割文件名与后缀
                temp_list = os.path.splitext(file)
                # name without extension
                src_apk_name = temp_list[0]
                # 后缀名，包含.   例如: ".apk "
                ext = temp_list[1]
                apk_ext='.apk';
                if apk_ext==ext:
                    print(sourceFile)
                    os.remove(sourceFile)

    def GetDownloadApk(self,sourceDir):
        for file in os.listdir(sourceDir):
            sourceFile = os.path.join(sourceDir,  file)
                #cover the files
            if os.path.isfile(sourceFile):
                # print sourceFile
                # 分割文件名与后缀
                temp_list = os.path.splitext(file)
                # name without extension
                src_apk_name = temp_list[0]
                # 后缀名，包含.   例如: ".apk "
                ext = temp_list[1]
                apk_ext='.apk';
                if apk_ext==ext:
                    print(sourceFile)
                    return sourceFile

        return ""
            
                    
 

# 3452644866 qq31415926
    def CreateApp(self, isHD):
        self.driver.get("http://union.baidu.com/bqt/appco.html#/promotion/application/create")
        time.sleep(1)

        webcmd = WebDriverCmd(self.driver)
        appChannel = source.TAPTAP
        appid = AppInfo.GetAppId(isHD, source.TAPTAP)
        if appid=="0":
            appid = AppInfo.GetAppId(isHD, source.HUAWEI)
            appChannel = source.HUAWEI

 
        key = "//input[@type='text' and @name='name']"
        title = self.GetAppName(isHD)
        self.SetText(key,title)

# 行业
        key = "//div[@class='veui-select veui-select-empty']"
        div = webcmd.Find(key)
        key = ".//button[@aria-haspopup='listbox']"
        item = webcmd.FindChild(div,key)
        item.click()

        time.sleep(1)
        key = "//span[@class='veui-option-label' and text()='教育']"
        webcmd.AddCmd(CmdType.CLICK, key)
        webcmd.Run(True)

        time.sleep(1)
        key = "//span[@class='veui-option-label' and text()='儿童']"
        webcmd.AddCmd(CmdType.CLICK, key)
        webcmd.Run(True)
        


        

        key = "//input[@type='text' and @name='keyword']"
        title = self.GetAppName(isHD)
        self.SetText(key,title)

        key = "//textarea[@class='veui-textarea-input']"
        title = AppInfo.GetAppDetail(isHD,source.LANGUAGE_CN)
        self.SetText(key,title)

        # <button type="button" class="veui-button">  Android </button>
        if self.osApp== source.ANDROID:
            key = "//button[@class='veui-button' and contains(text(),'Android')]"
            webcmd.AddCmd(CmdType.CLICK, key)
            webcmd.Run(True)

        


        key = "//input[@type='text' and @name='packageName']"
        title = AppInfo.GetAppPackage(self.osApp,isHD)
        self.SetText(key,title)

        #应用市场 http://app.mi.com/details?id=com.kibey.prophecy
        if self.osApp== source.ANDROID:
            key = "//button[@class='veui-button veui-dropdown-button']"
            webcmd.AddCmd(CmdType.CLICK, key)
            webcmd.Run(True)

            time.sleep(1)
            key = "//span[@class='veui-option-label' and text()='华为应用市场']"
            webcmd.AddCmd(CmdType.CLICK, key)
            webcmd.Run(True) 

        key = "//input[@type='text' and @name='appUrl']"
        # http(s)://appdl-drcn.dbankcdn.com/xxx或者http(s)://appdlc-drcn.hispace.hicloud.com/xxx
        # http://appdlc-drcn.hispace.hicloud.com/dl/appdl/application/apk/7c/7c1e552794ec43d488e9149e6c4644a7/com.ss.android.ugc.aweme.lite.2007201350.apk
        apk_url = mainAppVersionHuawei.GetApkUrl(AppInfo.GetAppId(isHD, source.HUAWEI)) 
        self.SetText(key,apk_url)

        old_window = self.driver.current_window_handle
        # 下一步
        # <button ui="primary" type="submit" class="veui-button">下一步</button>
        key = "//button[@ui='primary' and @type='submit']"
        webcmd.AddCmd(CmdType.CLICK, key)
        webcmd.Run(True)

                # 跳转到新的页面
        print("self.driver.current_url=", self.driver.current_url)
        # self.driver.switch_to.window(self.driver.window_handles[0])
        for win in self.driver.window_handles:
            if win != old_window:
                self.driver.switch_to.window(win)
        time.sleep(2)
        print("self.driver.current_url 2=", self.driver.current_url)



        if self.osApp== source.ANDROID:

            # E:\Users\moon\Downloads
            downloadDir = "C:\\Users\\moon\\Downloads"
            self.DeleteAllDownloadApk(downloadDir)

            # 下载空包 E:\Users\moon\Downloads\mssp-verify-b8920a35.apk
            key = "//button[@class='veui-button bottom20']"
            webcmd.AddCmd(CmdType.CLICK, key)
            webcmd.Run(True)

            time.sleep(3)
            apk_unsign = self.GetDownloadApk(downloadDir) 
            apk_sign = "F:\\sourcecode\\mssp_baidu\\signed.apk"
            jks = "F:\\sourcecode\\unity\\product\\kidsgame\\ProjectConfig\\Ad\\moonma.jks"
            # sign apk:
            # jarsigner -verbose -keystore ~/sourcecode/mssp_baidu/moonma.jks -signedjar ~/sourcecode/mssp_baidu/signed.apk ~/sourcecode/mssp_baidu/empty.apk moonma -storepass qianlizhiwai
            cmd = "jarsigner -verbose -keystore "+jks+" -signedjar "+apk_sign+" "+apk_unsign+" moonma -storepass qianlizhiwai"
            print(cmd)
            os.system(cmd)
            time.sleep(1)

            # sign end

            # 滚动到浏览器顶部
            js_top = "var q=document.documentElement.scrollTop=0"
            # 滚动到浏览器底部
            js_bottom = "var q=document.documentElement.scrollTop=document.documentElement.scrollHeight"
            self.driver.execute_script(js_bottom)
            time.sleep(2)

            # 上传签名包
            # key = "//input[@accept='.apk' and @name='file']"
            key = "//label[@class='veui-button veui-uploader-input-label']"
            item = webcmd.AddCmd(CmdType.CLICK_Action, key)
            # webcmd.SetItemVisible(item)
            webcmd.Run(True)

            self.OpenFileBrowser(apk_sign) 

        if self.osApp== source.IOS:
            time.sleep(3)

        # 完成
        key = "//button[@ui='primary' and @type='submit']"
        webcmd.AddCmd(CmdType.CLICK_Action, key)
        webcmd.Run(True)
        
         

    def GetAppName(self, ishd):
        name = AppInfo.GetAppName(self.osApp, ishd,source.LANGUAGE_CN) 
        return name
 
  #获取cookies保存到文件
    def SaveCookie(self):
        cookies=self.driver.get_cookies()
        json_cookies=json.dumps(cookies)
        with open('e:/cookies/cookies_gdt.json','w') as f:
            f.write(json_cookies)
    #读取文件中的cookie
    def AddCookie(self):
        self.driver.delete_all_cookies()
        dict_cookies={}
        with open('e:/cookies/cookies_gdt.json','r',encoding='utf-8') as f:
            list_cookies=json.loads(f.read())
            for i in list_cookies:
                self.driver.add_cookie(i)


    def SearchApp(self, ishd):
        name = self.GetAppName(ishd)
        self.driver.get("https://adnet.qq.com/medium/list")
        time.sleep(3)
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
        # <span class="media-heading" title="天天开心拼图">天天开心拼图</span>
        # key = "//span[@class='media-heading' and title ='"+name+"']"
        key = "//span[@class='media-heading']"
        list = self.driver.find_elements(By.XPATH, key)
        for span in list:
            if span.get_attribute('title') == name:
                span.click()
                time.sleep(1)


    def SearchAppAddPlace(self, ishd):

        self.SearchApp(ishd)

        # 新建广告
        list = self.driver.find_elements(
            By.XPATH, "//a[@class='btn btn-default btn-120']")
        a = list[1]
        url = a.get_attribute('href')
        print(url)
        self.urlCreatePlaceId = url
        # a.click()
        # time.sleep(1)

    def SearchAppGetAdInfo(self, ishd):
        self.SearchApp(ishd)
        # 关联广告位
        # <a style="cursor: pointer;">关联广告位</a>
        list = self.driver.find_elements(
            By.XPATH, "//a[@style='cursor: pointer;']")
        a = list[1]
        a.click()
        time.sleep(1)

        # table media-table js-media-details
        # table = self.driver.find_element(By.XPATH, "//table[@class='table media-table js-media-details']")
        # list = table.find_elements_by_xpath('//tbody/tr')
        # print("tr len =",len(list))
        # print(table.get_attribute('innerHTML'))
        # for tr in list:
        #     span_list = tr.find_elements_by_xpath("//span")
        #     # [@class='field-value']
        #     # print(span_list[1].text)

        parse = ParseAdGdt()
        parse.ParseAdData(self.driver.page_source, ishd, self.osApp)

    def GetAdInfo(self, isHD):
        self.SearchAppGetAdInfo(isHD)

    def CreatePlaceId(self, isHD):
        self.SearchAppAddPlace(isHD)
        self.CreateAdBanner(isHD)
        self.CreateAdInsert(isHD)
        self.CreateAdVideo(isHD)
        time.sleep(1)
        self.GetAdInfo(isHD)

    def OpenFileBrowser(self,filepath):
        # win32gui
        dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None,
                             filepath)
        # win32gui.SendMessage(Edit,win32con.WM_SETTEXT,None,'F:\sourcecode\unity\product\kidsgame\ProjectOutPut\xiehanzi\hanziyuan\screenshot\shu\cn\480p\1.jpg')  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

        time.sleep(3)

    def CreateAdBanner(self, isHD):
        # self.driver.get("https://adnet.qq.com/placement/add")
        # https://adnet.qq.com/placement/60503466885129/add
        self.driver.get(self.urlCreatePlaceId)
        time.sleep(1)
        webcmd = WebDriverCmd(self.driver)

        time.sleep(3)

        # div class="card-inner"
        # list = self.driver.find_elements(
        #     By.XPATH, "//div[@class='card-inner']")
        # list[4].click()
        # time.sleep(2)
        key = "//div[@class='card-inner']"
        webcmd.AddCmdList(CmdType.CLICK_Action, key,4,2)
        webcmd.Run(True) 

        # <ul class="union-card-list card-list-banner list-contain-1"
        ul = self.driver.find_element(
            By.XPATH, "//ul[@class='union-card-list card-list-banner list-contain-1']")

        # bug
        # list = ul.find_elements(By.XPATH, "//li[@class='union-card-item']")
        # ok 查找子元素li
        list = ul.find_elements_by_xpath('li')
        li = list[0]
        li.click()
        time.sleep(1)

        # item = self.driver.find_element(By.XPATH, "//input[@class='spaui-input has-normal spaui-component']")
        list = self.driver.find_elements(By.XPATH, "//input[@type='text']")
        # self.driver.execute_script("arguments[0].scrollIntoView();", item)
        # self.driver.execute_script('window.scrollTo(0,1000000)')
        time.sleep(1)
        list[1].send_keys("b")

        # upload image
        item = self.driver.find_element(
            By.XPATH, "//button[@id='spaui-uploader_2-empty']")
        item.click()
        time.sleep(1)
        self.OpenFileBrowser()
        time.sleep(1)

        # finish
        item = self.driver.find_element(
            By.XPATH, "//button[@class='union-complete-btn spaui-button spaui-button-primary spaui-component']")
        item.click()
        time.sleep(1)

    def CreateAdInsert(self, isHD):
        webcmd = WebDriverCmd(self.driver)
        # self.driver.get("https://adnet.qq.com/placement/add")
        # https://adnet.qq.com/placement/60503466885129/add
        self.driver.get(self.urlCreatePlaceId)
        time.sleep(1)

        time.sleep(3)

        # div class="card-inner"
        key = "//div[@class='card-inner']"
        webcmd.AddCmdList(CmdType.CLICK_Action, key,5,2)
        webcmd.Run(True) 


        # <ul class="union-card-list card-list-banner list-contain-1"
        ul = self.driver.find_element(
            By.XPATH, "//ul[@class='union-card-list card-list-cp list-contain-2']")

        # bug
        # list = ul.find_elements By.XPATH, "//li[@class='union-card-item']")
        # ok 查找子元素li
        list = ul.find_elements_by_xpath('li')

        list[1].click()
        time.sleep(1)

        # item = self.driver.find_element(By.XPATH, "//input[@class='spaui-input has-normal spaui-component']")
        list = self.driver.find_elements(By.XPATH, "//input[@type='text']")
        # self.driver.execute_script("arguments[0].scrollIntoView();", item)
        # self.driver.execute_script('window.scrollTo(0,1000000)')
        time.sleep(1)
        list[1].send_keys("i")

        # upload image
        item = self.driver.find_element(
            By.XPATH, "//button[@id='spaui-uploader_2-empty']")
        item.click()
        time.sleep(1)
        self.OpenFileBrowser()
        time.sleep(1)

        # finish
        item = self.driver.find_element(
            By.XPATH, "//button[@class='union-complete-btn spaui-button spaui-button-primary spaui-component']")
        item.click()
        time.sleep(1)

    def CreateAdVideo(self, isHD):
        webcmd = WebDriverCmd(self.driver)
        # self.driver.get("https://adnet.qq.com/placement/add")
        # https://adnet.qq.com/placement/60503466885129/add
        self.driver.get(self.urlCreatePlaceId)
        time.sleep(1)

        time.sleep(3)

        # div class="card-inner" 
        key = "//div[@class='card-inner']"
        webcmd.AddCmdList(CmdType.CLICK_Action, key,2,2)
        webcmd.Run(True) 

        # item = self.driver.find_element(By.XPATH, "//input[@class='spaui-input has-normal spaui-component']")
        list = self.driver.find_elements(By.XPATH, "//input[@type='text']")
        # self.driver.execute_script("arguments[0].scrollIntoView();", item)
        # self.driver.execute_script('window.scrollTo(0,1000000)')
        time.sleep(1)
        list[1].send_keys("v")

        # upload image
        item = self.driver.find_element(
            By.XPATH, "//button[@id='spaui-uploader_2-empty']")
        item.click()
        time.sleep(1)
        self.OpenFileBrowser()
        time.sleep(1)

        # finish
        item = self.driver.find_element(
            By.XPATH, "//button[@class='union-complete-btn spaui-button spaui-button-primary spaui-component']")
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
    for i in range(1, count):
        print("参数", i, sys.argv[i])
        if i == 1:
            cmdPath = sys.argv[i]

    # cmdPath = cmdPath.replace("ad\\", "")

    dir = common.getLastDirofDir(cmdPath)
    # dir = common.getLastDirofDir(dir)
    common.SetCmdPath(dir)
    print(cmdPath) 
    ad = AdBaidu()
    ad.SetCmdPath(cmdPath)
    ad.Init()
    ad.GoHome()
    ad.Login("moonmaapp","Qianlizhiwai1")

    argv1 = sys.argv[2]
    ad.osApp = sys.argv[3]
    if argv1 == "createapp":
        ad.CreateApp(False)
        time.sleep(3)
        # ad.CreateApp(True)

    if argv1 == "createplaceid":
        ad.CreatePlaceId(False)
        time.sleep(3)
        ad.CreatePlaceId(True)

    if argv1 == "adinfo":
        ad.GetAdInfo(False)
        time.sleep(3)
        ad.GetAdInfo(True)

    print("AdGdt sucess")
