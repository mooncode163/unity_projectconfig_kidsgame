
  
@set filepath = %~dp0 

cd ../../../script

python save_resource.py %~dp0 
python appcode.py %~dp0 "save"


@Pause

 


 
 
 