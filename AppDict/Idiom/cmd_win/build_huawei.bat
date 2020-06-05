@echo  build_huawei
@set filepath = %~dp0 
@echo off
echo.| call copy_resource.bat
echo.| call unity_build_android.bat
echo. | call update_appname_auto.bat
echo.| call apk_build_huawei.bat
@Pause
