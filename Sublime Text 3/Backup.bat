@echo off
echo 确认将当前系统的Sublime Text 3配置备份到当前文件夹？
pause
set destination=%cd%\Packages
set source=%APPDATA%\Sublime Text 3\Packages
xcopy "%source%\Default" "%destination%\Default\" /s/q/y
xcopy "%source%\Guangshan" "%destination%\Guangshan\" /s/q/y
xcopy "%source%\User" "%destination%\User\" /s/q/y /exclude:Backup.ignore
xcopy "%source%\Color Highlighter" "%destination%\Color Highlighter\" /s/q/y
rem echo 备份sublimeCodeIntel的配置
rem xcopy "%USERPROFILE%\.codeintel\config" "%destination%\.codeintel\" /s/q/y

pause
exit
