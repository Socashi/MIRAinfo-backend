#!/bin/bash
pip install --no-cache-dir --force-reinstall -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port $PORT
