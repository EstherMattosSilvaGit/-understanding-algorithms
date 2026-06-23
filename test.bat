@echo off
setlocal enabledelayedexpansion
set PYTHONPATH=.
C:/Users/Silva/AppData/Local/Programs/Python/Python312/python.exe -m unittest discover --pattern="*Tests.py"
