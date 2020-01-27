
  
@set filepath = %~dp0 

cd ../../../script

c:/Python27/python save_resource.py %~dp0 
c:/Python27/python appcode.py %~dp0 "save"


@Pause

 


 
 
 