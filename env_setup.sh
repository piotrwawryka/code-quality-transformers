#!/usr/bin/env bash

# add required modules
module add plgrid/tools/python/3.6.5

# create virtual environment (required only for the first time, uncomment if needed)
# python3.6 -m venv venv
# pip install -r requirements.txt

# activate environment
source venv/bin/activate

# check status
python env_check.py
