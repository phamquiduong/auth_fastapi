@echo off
cd src
set /p host="Enter host (default: 127.0.0.1): "
set /p port="Enter port (default: 8000): "

if "%host%"=="" set host=127.0.0.1
if "%port%"=="" set port=8000

uvicorn main:app --host %host% --port %port% --reload
