@echo off
echo 确认将当前目录下的的Sublime Text 3配置还原到当前系统下？

pause

set source=%cd%\Packages\

set destination=C:\Users\Guangshan\AppData\Roaming\Sublime Text 3\Packages\

xcopy "%source%Default" "%destination%Default\" /s/q/y

xcopy "%source%Guangshan" "%destination%Guangshan\" /s/q/y

xcopy "%source%User" "%destination%User\" /s/q/y

pause

exit
