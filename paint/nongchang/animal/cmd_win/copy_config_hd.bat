 
@set filepath = %~dp0 

cd ../../../script

python copy_config.py %~dp0 iconhd
python clean_screenshot.py %~dp0
python config_xcode_project.py %~dp0
@Pause

 

 
 