echo off

pyinstaller --clean --onefile --noconsole --i DiscDisable.ico discdisable.py

del /s /q /f build.spec
rmdir /s /q __pycache__
rmdir /s /q build

