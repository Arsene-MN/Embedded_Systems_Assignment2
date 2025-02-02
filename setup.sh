#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required dependencies from requirements.txt
pip install -r requirements.txt

# Confirm successful installation
echo "Dependencies installed successfully."
