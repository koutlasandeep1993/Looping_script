@echo off
setLocal EnableDelayedExpansion
::Basic configuration

For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-3 delims=/:/ " %%a in ('time /t') do (set mytime=%%a-%%b-%%c)
::set mytime=%mytime: =% 

::Basic configuration end

::Script execution steps 

echo  informatica call started

::Call informatica 
c:
cd C:\Program Files\Informatica Cloud Secure Agent\apps\runAJobCli\
::set filename=D:\Script_Logs\%1_%mydate%_%mytime.txt%
::set val1=D:\Script_Logs\%1_%mydate%_%mytime%_%
::set filename=%val1%.txt%
set filename=D:\Script_Logs\%1_%mydate%_%mytime%.txt%
call cli.bat runAJobCli -n %1 -t %2 true >>%filename%
echo %errorlevel%
if %errorlevel% equ 0 (
	echo Job completed successfully with return code %errorlevel% >>%filename%
    exit  %errorlevel%
   
) else (
	echo Failure Reason Given is %errorlevel% >>%filename%
	exit %errorlevel%
)

@echo off

echo informatica process finished




