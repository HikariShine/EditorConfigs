@echo off
echo ȷ�Ͻ���ǰĿ¼�µ�Sublime Text 3���û�ԭ����ǰϵͳ�£�
pause

set source=%cd%\Packages

set destination=%APPDATA%\Sublime Text 3\Packages

echo �ȱ���ԭPackages�������ļ���E�̵�Backup�У��Է���һ
xcopy "%destination%" "E:\Backup\" /s/q/y
echo �������
xcopy "%source%\Default" "%destination%\Default\" /s/q/y

xcopy "%source%\Guangshan" "%destination%\Guangshan\" /s/q/y

xcopy "%source%\User" "%destination%\User\" /s/q/y

pause

exit
