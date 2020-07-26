@echo  build_huawei
@set filepath = %~dp0 
@echo off
filepath = %~dp0  
cd ../
echo.| call copy_resource.bat
cd %~dp0
echo.| call unity_build_android.bat
cd ../
echo.| call update_appname_auto.bat
cd %~dp0
echo.| call apk_build_huawei.bat
@Pause
