@cd /D "%~dp0"
@set pyRuntime=..\..\..\PyRuntime\
@set PY_PIP=%pyRuntime%Scripts
@set PIP=%pyRuntime%Scripts\pip.exe
@set PY_LIBS=%pyRuntime%\Lib;%pyRuntime%\Lib\site-packages
@set path=%pyRuntime%;%PATH%
@%PIP% install -r requirements.txt --target .\lib\
@if not exist .\lib\__init__.py (
    @copy NUL .\lib\__init__.py 
)
