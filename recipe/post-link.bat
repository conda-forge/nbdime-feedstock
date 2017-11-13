@echo off

"%PREFIX%\Scripts\jupyter-nbextension.exe" enable --py nbdime --sys-prefix > NUL 2>&1 && if errorlevel 1 exit 1
"%PREFIX%\Scripts\jupyter-serverextension.exe" enable nbdime --sys-prefix > NUL 2>&1 && if errorlevel 1 exit 1
