@echo off
echo 创建链接的目的是提供给SublimeCodeIntel使用，因为这个插件只支持使用~用户目录变量，而不支持$系统变量，所以创建一个python到user目录的链接，也可以通过修改插件做到该功能
set destination=%USERPROFILE%\Python
set source=%PYTHON_HOME%
set destination3=%USERPROFILE%\Python3
set source3=%PYTHON3_HOME%
if exist "%source%" (
   if exist "%destination%" (
      echo 原链接已存在，删除
      rmdir "%destination%"
   )
   echo 创建到PYTHON_HOME的链接
   mklink /J "%destination%" "%source%"
) else (
   echo PYTHON_HOME不存在
)
pause
if exist "%source3%" (
   if exist "%destination3%" (
      echo 原链接已存在，删除
      rmdir "%destination3%"
   )
   echo 创建到PYTHON3_HOME的链接
   mklink /J "%destination3%" "%source3%"
) else (
   echo PYTHON3_HOME不存在
)
pause