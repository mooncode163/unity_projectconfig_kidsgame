@set filepath = %~dp0 


cd ../../../script


c:/Python27/python copy_config.py %~dp0 icon
c:/Python27/python clean_screenshot.py %~dp0
c:/Python27/python config_xcode_project.py %~dp0 

@Pause

 

 
 