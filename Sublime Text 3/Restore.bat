@echo off
echo 确认将当前目录下的Sublime Text 3配置还原到当前系统下？
pause

set source=%cd%\Packages

set destination=%APPDATA%\Sublime Text 3\Packages

echo 先备份原Packages下所有文件到E盘的Backup中，以防万一
xcopy "%destination%" "E:\Backup\" /s/q/y
echo 备份完成
xcopy "%source%\Default" "%destination%\Default\" /s/q/y

xcopy "%source%\Guangshan" "%destination%\Guangshan\" /s/q/y

xcopy "%source%\User" "%destination%\User\" /s/q/y

pause

exit
