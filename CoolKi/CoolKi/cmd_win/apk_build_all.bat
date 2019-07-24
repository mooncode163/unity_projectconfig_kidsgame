@echo  apk_build_all
@set filepath = %~dp0 

cd ../../../script

c:/Python27/python copy_config.py %~dp0 icon
c:/Python27/python clean_screenshot.py %~dp0
c:/Python27/python apk_build_clean.py 
c:/Python27/python apk_build_all.py %~dp0


c:/Python27/python copy_config.py %~dp0 iconhd
c:/Python27/python clean_screenshot.py %~dp0
c:/Python27/python apk_build_clean.py 
c:/Python27/python apk_build_all.py %~dp0


@Pause
