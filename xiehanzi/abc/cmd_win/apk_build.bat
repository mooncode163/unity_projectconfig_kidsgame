
@echo  apk_build  

@set filepath = %~dp0 

cd ../../../script

c:/Python27/python apk_build_clean.py 

c:/Python27/python apk_build.py %~dp0



@Pause
