#!/bin/bash
echo "Setting up PhD research environment..."

# Create virtual environment
python3 -m venv phd_env

# Activate and install packages
source phd_env/bin/activate
pip install -r requirements.txt

# Setup Jupyter kernel
python -m ipykernel install --user --name=phd_env --display-name="Python (PhD Research)"

echo "✅ Setup complete! Activate with: source phd_env/bin/activate"
