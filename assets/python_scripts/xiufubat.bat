@echo off
echo ============================================
echo.
echo U�������ļ��лָ�
echo.
echo ============================================
pause
rem echo �г�Ŀ¼
dir /a:d /b >yxkmp4dir.txt
rem echo �г�Ŀ¼��������ļ�
rem dir /a:s /a:-d /b
for /f "tokens=* delims= " %%i in (yxkmp4dir.txt) do call :ss "%%i"
del yxkmp4dir.txt
echo.
echo ȫ���޸����,лл���ʹ��!
echo.
pause
goto :eof
:ss
set var=%1
echo �����޸��ļ��� %var% ...
attrib -s -h -r %var%
goto :eof