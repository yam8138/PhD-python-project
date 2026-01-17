# PhD Research: Thermophysical & Structural Properties

## 📋 Project Overview
This repository contains code and analysis for my PhD research on thermophysical and structural properties of materials.

## 🏗️ Project Structure
.
├── data/               # Experimental data (raw & processed)
│   ├── raw/           # Raw experimental data (NOT in Git)
│   └── processed/     # Processed data for analysis
├── notebooks/         # Jupyter notebooks for analysis
├── scripts/           # Python modules and utility functions
├── figures/           # Generated plots and visualizations
├── literature/        # Research papers and references
├── requirements.txt   # Python package dependencies
├── environment.yml    # Conda environment (optional)
├── setup.sh           # Setup script for environment
├── .gitignore         # Files to exclude from Git
└── README.md          # This file

## 🚀 Quick Start

### Setup Environment:
\`\`\`bash
# 1. Create virtual environment
python3 -m venv phd_env
source phd_env/bin/activate

# 2. Install packages
pip install -r requirements.txt

# 3. Setup Jupyter kernel
python -m ipykernel install --user --name=phd_env --display-name="Python (PhD Research)"
\`\`\`

### Start Working:
\`\`\`bash
# Use the alias (if set up)
start-phd
# Or manually:
cd ~/Documents/PhD/python
source phd_env/bin/activate
jupyter lab
\`\`\`

## 📊 Research Areas
- XRD pattern analysis for structural properties
- Thermal conductivity measurements
- Specific heat capacity calculations
- Diffusion coefficient analysis
- Material characterization

## 📝 License
This work is part of my PhD research at [Your University].
# phd-research
