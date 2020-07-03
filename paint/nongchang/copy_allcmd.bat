@echo  apk_build_gp
@set filepath = %~dp0 

cd ../script
python copy_allcmd.py %~dp0
  
@Pause
