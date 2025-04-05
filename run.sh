#!/bin/bash
mysql PPP_data --password <make_table.sql && ./venv/bin/python3 data_pipeline.py
