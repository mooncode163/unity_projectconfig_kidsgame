@echo  unity_build
@set filepath = %~dp0 

cd ../../../script

python unity_build.py %~dp0 ios
  
@Pause
