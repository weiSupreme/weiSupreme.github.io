@echo off
echo ============================================
echo.
echo U盘隐藏文件夹恢复
echo.
echo ============================================
pause
rem echo 列出目录
dir /a:d /b >yxkmp4dir.txt
rem echo 列出目录外的所有文件
rem dir /a:s /a:-d /b
for /f "tokens=* delims= " %%i in (yxkmp4dir.txt) do call :ss "%%i"
del yxkmp4dir.txt
echo.
echo 全部修复完成,谢谢你的使用!
echo.
pause
goto :eof
:ss
set var=%1
echo 正在修复文件夹 %var% ...
attrib -s -h -r %var%
goto :eof