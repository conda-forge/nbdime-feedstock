@echo off

"%PREFIX%\Scripts\jupyter-nbextension.exe" disable --py nbdime --sys-prefix > NUL 2>&1 && if errorlevel 1 exit 1
"%PREFIX%\Scripts\jupyter-serverextension.exe" disable nbdime --sys-prefix > NUL 2>&1 && if errorlevel 1 exit 1
