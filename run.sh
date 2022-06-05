#!/bin/bash

source ./venv/bin/activate
uvicorn app.main:fastapi_app --host 127.0.0.1 --port 8080
