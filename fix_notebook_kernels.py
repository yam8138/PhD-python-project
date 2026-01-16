#!/usr/bin/env python3
"""
Update all notebooks to use the correct kernel
"""

import os
import json
import glob

def update_notebook_kernel(notebook_path, new_kernel_name="phd_env"):
    """Update kernel specification in a notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Update kernel info
        if 'metadata' in notebook:
            if 'kernelspec' in notebook['metadata']:
                notebook['metadata']['kernelspec']['name'] = new_kernel_name
                notebook['metadata']['kernelspec']['display_name'] = "Python (PhD Research)"
            
            # Update language info
            if 'language_info' in notebook['metadata']:
                notebook['metadata']['language_info']['name'] = "python"
        
        # Save back
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1)
        
        return True
    except Exception as e:
        print(f"  Error updating {notebook_path}: {e}")
        return False

def main():
    print("=== FIXING NOTEBOOK KERNELS ===")
    
    # Find all notebooks
    notebooks = glob.glob("notebooks/*.ipynb") + glob.glob("*.ipynb")
    
    if not notebooks:
        print("No notebooks found!")
        return
    
    print(f"Found {len(notebooks)} notebooks")
    print()
    
    updated = 0
    for nb in notebooks:
        print(f"Updating: {nb}")
        if update_notebook_kernel(nb):
            updated += 1
            print(f"  ✅ Updated to use 'phd_env' kernel")
        else:
            print(f"  ❌ Failed")
        print()
    
    print(f"=== SUMMARY ===")
    print(f"Updated {updated}/{len(notebooks)} notebooks")
    print()
    print("Now restart Jupyter Lab and notebooks should use correct kernel")
    
    # Also create kernel.json for reference
    kernel_json = {
        "argv": [
            "/home/yam/Documents/PhD/python/phd_env/bin/python",
            "-m",
            "ipykernel_launcher",
            "-f",
            "{connection_file}"
        ],
        "display_name": "Python (PhD Research)",
        "language": "python",
        "metadata": {
            "debugger": True
        }
    }
    
    os.makedirs("/home/yam/.local/share/jupyter/kernels/phd_env", exist_ok=True)
    with open("/home/yam/.local/share/jupyter/kernels/phd_env/kernel.json", "w") as f:
        json.dump(kernel_json, f, indent=2)
    
    print("Kernel configuration saved")

if __name__ == "__main__":
    main()
