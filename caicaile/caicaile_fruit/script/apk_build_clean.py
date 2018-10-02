#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time,  datetime
import sys
#include common.py
sys.path.append('./common')
import common



#主函数的实现
if  __name__ =="__main__":
    
#            javaLibDir ="/Users/jaykie/sourcecode/cocos2d_appstore/ertong/cocos2d/cocos/2d/platform/android/java/gen/org/cocos2dx/lib"
             
            
             
            targetDir = "../../../../project_android/kidsgame"
            
  
            #build
            dir2 = targetDir+"/build";
            flag = os.path.exists(dir2)
            if flag:
                shutil.rmtree(dir2)
 


            print "apk_build_clean sucess"



