@echo  apk_build_gp
@set filepath = %~dp0 

cd ../../../script

c:/Python27/python copy_config.py %~dp0 icon
c:/Python27/python clean_screenshot.py %~dp0
c:/Python27/python apk_build_clean.py 
c:/Python27/python apk_build_gp.py %~dp0


c:/Python27/python copy_config.py %~dp0 iconhd
c:/Python27/python clean_screenshot.py %~dp0
c:/Python27/python apk_build_clean.py 
c:/Python27/python apk_build_huawei.py %~dp0


@Pause
