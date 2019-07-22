@echo off
ECHO Build tProjectTimer
pyinstaller --onefile --noconsole controllerCsvWriter.py
pyinstaller --onefile --noconsole controllerProjectSelector.py
pyinstaller --onefile --noconsole rememberingToolStarter.py