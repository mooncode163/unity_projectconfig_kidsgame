@echo  apk_build_gp
@set filepath = %~dp0 

cd ../script
c:/Python27/python build_all_games.py %~dp0 gp
  
@Pause
