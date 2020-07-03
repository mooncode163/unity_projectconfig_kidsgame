@echo  apk_build_gp
@set filepath = %~dp0 

cd ../../../script

python copy_config.py %~dp0 icon
python clean_screenshot.py %~dp0
python apk_build_clean.py 
python apk_build_xiaomi.py %~dp0


python copy_config.py %~dp0 iconhd
python clean_screenshot.py %~dp0
python apk_build_clean.py
python apk_build_xiaomi.py %~dp0


@Pause
