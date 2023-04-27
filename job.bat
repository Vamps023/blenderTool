@echo off

if exist ".\model\" (
  cd ".\model\"
  for /f %%i in ('dir /b /od *.blend') do set latest_file=%%i
) else (
  for /f %%i in ('dir /b /od *.blend') do set latest_file=%%i
)

start "" "D:\Blender\blender.exe" "%CD%\%latest_file%"
