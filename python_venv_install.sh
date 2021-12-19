#!/bin/bash
python3 -m venv obsidian_cloud
cp -r requirements.txt obsidian_cloud/
cp -r run.py obsidian_cloud/
source obsidian_cloud/bin/activate
wait
pip3 install -r requirements.txt 