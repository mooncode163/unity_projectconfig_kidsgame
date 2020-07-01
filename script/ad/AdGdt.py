# 导入selenium的浏览器驱动接口
import sys
import os
import json
o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径
from common import common
from common import source

import appname 

from selenium import webdriver

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 导入chrome选项
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


import sqlite3

# pip3 install pywin32
import win32gui
import win32con

# sys.path.append('../common') 
from ParseAdGdt import ParseAdGdt 

class AdGdt():
    driver: None
    dirRoot:None
    urlCreatePlaceId:None
    osApp:None

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
        time.sleep(2)
        # return
        # driver.add_cookie("[{'domain': '.id1.cloud.huawei.com', 'expiry': 1908869785, 'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': True, 'value': '2049382e3828ef4470bef8b426c4bb3370e7d9e1147f53a18839e47dad7caf10a233e61ee15337b4373e'}, {'domain': '.id1.cloud.huawei.com', 'expiry': 1908869785, 'httpOnly': False, 'name': 'hwid_cas_sid', 'path': '/', 'secure': True, 'value': '2049382e3828ef4470bef8b426c4bb3370e7d9e1147f53a18839e47dad7caf10a233e61ee15337b4373e'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_idts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1593336984125'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_id_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': 'cf787be41ac24d65887dcd20c826ac97'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1624872984, 'httpOnly': False, 'name': 'HW_idvc_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1593338788, 'httpOnly': False, 'name': 'HW_idn_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': 'ec569450f0ac4cd78fc72965d91ec7e8'}, {'domain': 'id1.cloud.huawei.com', 'expiry': 1608888984, 'httpOnly': False, 'name': 'HW_refts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'path': '/', 'secure': False, 'value': '1593336984124'}, {'domain': '.id1.cloud.huawei.com', 'httpOnly': True, 'name': 'CAS_THEME_NAME', 'path': '/', 'secure': True, 'value': 'red'}, {'domain': 'id1.cloud.huawei.com', 'httpOnly': False, 'name': 'cookieBannerOnOff', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.id1.cloud.huawei.com', 'httpOnly': True, 'name': 'VERSION_NO', 'path': '/', 'secure': True, 'value': 'UP_CAS_4.0.4.100'}, {'domain': 'id1.cloud.huawei.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/CAS', 'secure': True, 'value': '144E8B2ED3F5D9C8576742C1DDF4CF3D0DCF6949E13D6943'}]")
        self.driver.switch_to.frame("ptlogin_iframe")
        time.sleep(2)

        self.driver.find_element_by_id('switcher_plogin').click()
        time.sleep(1) 

        item = self.driver.find_element(
            By.XPATH, "//input[@id='u']")
        item.send_keys("3452644866")

        item = self.driver.find_element(By.XPATH, "//input[@id='p']")
        item.send_keys("qq31415926")

 
        item = self.driver.find_element(
            By.XPATH, "//input[@id='login_button']")
        item.click()
        time.sleep(3) 

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
        appid  = appname.GetAppId(isHD,source.HUAWEI)
        item.send_keys("http://appstore.huawei.com/C"+appid)
        
        # name
        name = self.GetAppName(isHD)
        list = self.driver.find_elements(
            By.XPATH, "//input[@id='placementName']")
        list[0].send_keys(name)

        list = self.driver.find_elements(
            By.XPATH, "//input[@id='placementName']")
        list[1].send_keys(name)
        

        item = self.driver.find_element_by_id('formControlsTextarea')
        name+=name
        name+=name
        name+=name
        name+=name 
        item.send_keys(name)


        item = self.driver.find_element(
            By.XPATH, "//input[@id='packageName']")
        package = appname.GetPackage(source.ANDROID,isHD)
        item.send_keys(package)
        


        # 创建
        
        item = self.driver.find_element(
            By.XPATH, "//a[@class='btn btn-primary btn-160']")
        item.click()

    def GetAppName(self,ishd):
        return appname.GetAppName(self.osApp,ishd)+self.osApp

    def SearchAppAddPlace(self,ishd):
        name = self.GetAppName(ishd)
        self.driver.get("https://adnet.qq.com/medium/list")
        time.sleep(2)  
        item = self.driver.find_element(By.XPATH, "//input[@class='form-control']") 
        time.sleep(1)

        item.send_keys(name)
        # item.send_keys("儿童写汉字")
        
        time.sleep(1)

        self.driver.find_element_by_id('search_medium_id').click()
        time.sleep(2)

        item = self.driver.find_element(By.XPATH, "//div[@class='media']") 
        item.click()
        time.sleep(1)
        
        # 新建广告
        list = self.driver.find_elements(By.XPATH, "//a[@class='btn btn-default btn-120']") 
        a = list[1]
        url = a.get_attribute('href')
        print(url)
        self.urlCreatePlaceId = url
        # a.click()
        # time.sleep(1) 
        
        
    def SearchAppGetAdInfo(self,ishd):
        name = self.GetAppName(ishd)
        self.driver.get("https://adnet.qq.com/medium/list")
        time.sleep(2)  
        item = self.driver.find_element(By.XPATH, "//input[@class='form-control']") 
        time.sleep(1)

        item.send_keys(name)
        # item.send_keys("儿童写汉字")
        
        time.sleep(1)

        self.driver.find_element_by_id('search_medium_id').click()
        time.sleep(2)

        item = self.driver.find_element(By.XPATH, "//div[@class='media']") 
        item.click()
        time.sleep(1)
        
        # 关联广告位
        # <a style="cursor: pointer;">关联广告位</a>
        list = self.driver.find_elements(By.XPATH, "//a[@style='cursor: pointer;']") 
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
        parse.ParseAdData(self.driver.page_source,ishd,self.osApp)

            


    def GetAdInfo(self,isHD):
        self.SearchAppGetAdInfo(isHD) 

    def CreatePlaceId(self,isHD): 
        self.SearchAppAddPlace(isHD)
        self.CreateAdBanner(isHD)
        self.CreateAdInsert(isHD)
        self.CreateAdVideo(isHD)
        

    def OpenFileBrowser(self):
        # win32gui
        dialog = win32gui.FindWindow('#32770',u'打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,'ComboBoxEx32',None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32,0,'ComboBox',None)
        Edit = win32gui.FindWindowEx(ComboBox,0,'Edit',None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog,0,'Button',None)  # 确定按钮Button
        win32gui.SendMessage(Edit,win32con.WM_SETTEXT,None,"F:\\sourcecode\\unity\\product\\kidsgame\\ProjectOutPut\\xiehanzi\\hanziyuan\\screenshot\\shu\\cn\\480p\\1.jpg")
        # win32gui.SendMessage(Edit,win32con.WM_SETTEXT,None,'F:\sourcecode\unity\product\kidsgame\ProjectOutPut\xiehanzi\hanziyuan\screenshot\shu\cn\480p\1.jpg')  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)  # 按button


    def CreateAdBanner(self,isHD):
        # self.driver.get("https://adnet.qq.com/placement/add")
        # https://adnet.qq.com/placement/60503466885129/add
        self.driver.get(self.urlCreatePlaceId)
        time.sleep(1)

        # time.sleep(5)

        # div class="card-inner"
        list = self.driver.find_elements(
            By.XPATH, "//div[@class='card-inner']")
        list[4].click()
        time.sleep(2)

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
        

    def CreateAdInsert(self,isHD):
        # self.driver.get("https://adnet.qq.com/placement/add")
        # https://adnet.qq.com/placement/60503466885129/add
        self.driver.get(self.urlCreatePlaceId)
        time.sleep(1)

        # time.sleep(5)

        # div class="card-inner"
        list = self.driver.find_elements(
            By.XPATH, "//div[@class='card-inner']")
        list[5].click()
        time.sleep(2)

        # <ul class="union-card-list card-list-banner list-contain-1"
        ul = self.driver.find_element( By.XPATH, "//ul[@class='union-card-list card-list-cp list-contain-2']")
        
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

    def CreateAdVideo(self,isHD):
        # self.driver.get("https://adnet.qq.com/placement/add")
        # https://adnet.qq.com/placement/60503466885129/add
        self.driver.get(self.urlCreatePlaceId)
        time.sleep(1)

        # time.sleep(5)

        # div class="card-inner"
        list = self.driver.find_elements(
            By.XPATH, "//div[@class='card-inner']")
        list[2].click()
        time.sleep(2)
 
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
    package = appname.GetPackage(source.ANDROID,False)
    print(package) 
    package = appname.GetAppId(False,source.HUAWEI)
    print(package)
    
    
    ad = AdGdt()
    ad.SetCmdPath(cmdPath)
    ad.Init()
    ad.GoHome()
    ad.Login()

    argv1 = sys.argv[2]
    ad.osApp = sys.argv[3]
    if argv1 == "createapp":
        ad.CreateApp(False)
        time.sleep(3)
        ad.CreateApp(True)
        
    if argv1 == "createplaceid":
        ad.CreatePlaceId(False)  
        time.sleep(3)
        ad.CreatePlaceId(True)

    if argv1 == "adinfo":
        ad.GetAdInfo(False)  
        time.sleep(3)
        ad.GetAdInfo(True)
 
    
    

    print("AdGdt sucess")
