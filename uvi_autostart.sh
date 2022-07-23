#!/bin/bash
source /home/pi/Elden-Ring/venv/bin/activate
/home/pi/Elden-Ring/venv/bin/python -m uvicorn testringer:app --app-dir /home/pi/Elden-Ring --reload --host 0.0.0.0
