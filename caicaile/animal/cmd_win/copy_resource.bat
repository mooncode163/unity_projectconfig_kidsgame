
  
@set filepath = %~dp0 

cd ../../../script

c:/Python27/python copy_resource.py %~dp0
c:/Python27/python copy_gamedata.py %~dp0
c:/Python27/python appcode.py %~dp0 "copy"


@Pause

 


 
 