@echo off
cmd /k "cd /d backEnd\venv\Scripts & activate & cd /d    C:\xampp\htdocs\quru\backEnd & python main.py 0 & cd /d venv\Scripts & deactivate"