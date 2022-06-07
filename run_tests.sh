#!/bin/bash

source ./venv/bin/activate
flake8 .
pytest app/tests/tests.py
