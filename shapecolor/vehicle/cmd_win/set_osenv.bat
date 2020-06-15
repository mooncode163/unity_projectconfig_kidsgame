@echo  unity_build
@set filepath = %~dp0 

cd ../../../script

python set_osenv.py %~dp0
  
@Pause
