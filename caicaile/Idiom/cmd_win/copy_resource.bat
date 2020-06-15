
  
@set filepath = %~dp0 

cd ../../../script

python copy_resource.py %~dp0
python copy_gamedata.py %~dp0
python appcode.py %~dp0 "copy"


@Pause

 


 
 