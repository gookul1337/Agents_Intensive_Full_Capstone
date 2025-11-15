#!/usr/bin/env bash
set -e
python3 -m venv venv || true
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Setup complete. Activate with: source venv/bin/activate"
