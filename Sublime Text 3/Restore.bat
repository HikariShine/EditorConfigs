@echo off
echo ȷ�Ͻ���ǰĿ¼�µĵ�Sublime Text 3���û�ԭ����ǰϵͳ�£�

pause

set source=%cd%\Packages\

set destination=C:\Users\Guangshan\AppData\Roaming\Sublime Text 3\Packages\

xcopy "%source%Default" "%destination%Default\" /s/q/y

xcopy "%source%Guangshan" "%destination%Guangshan\" /s/q/y

xcopy "%source%User" "%destination%User\" /s/q/y

pause

exit
