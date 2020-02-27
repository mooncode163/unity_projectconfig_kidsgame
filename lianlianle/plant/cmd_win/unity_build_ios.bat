@echo  unity_build
@set filepath = %~dp0 

cd ../../../script

c:/Python27/python unity_build.py %~dp0 ios
  
@Pause
