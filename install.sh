#!/usr/bin/bash

docker pull universalrobots/ursim_cb3

# Navigate to the directory containing setup.py
cd old-ds-opt-py

# Install the package globally in editable mode using pip
sudo pip3 install -e .
