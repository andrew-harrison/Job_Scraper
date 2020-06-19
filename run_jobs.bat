@echo off
DEL msgbox.vbs
pipenv run python jobs.py %1
if errorlevel 1 echo x=msgbox("Python code failed to run" ,0, "Message from your computer  ") >> msgbox.vbs
start msgbox.vbs