@echo off
echo ȷ�Ͻ���ǰϵͳ��Sublime Text 3���ñ��ݵ���ǰ�ļ��У�
pause
set destination=%cd%\Packages
set source=%APPDATA%\Sublime Text 3\Packages
xcopy "%source%\Default" "%destination%\Default\" /s/q/y
xcopy "%source%\Guangshan" "%destination%\Guangshan\" /s/q/y
xcopy "%source%\User" "%destination%\User\" /s/q/y /exclude:Backup.ignore
pause
exit
