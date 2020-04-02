@echo  apk_build_huawei
@set filepath = %~dp0 

cd ../../../script

c:/Python27/python copy_android_output_asset.py %~dp0 

c:/Python27/python copy_config.py %~dp0 icon
c:/Python27/python clean_screenshot.py %~dp0
c:/Python27/python apk_build_clean.py 
c:/Python27/python apk_build_huawei.py %~dp0


c:/Python27/python copy_config.py %~dp0 iconhd
c:/Python27/python clean_screenshot.py %~dp0
c:/Python27/python apk_build_clean.py 
c:/Python27/python apk_build_huawei.py %~dp0 hd


@Pause
