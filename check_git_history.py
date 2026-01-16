#!/usr/bin/env python3
"""
Check Git history for phd_env and recommend actions
"""

import subprocess
import os

def run_cmd(cmd):
    """Run command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return None, str(e)

print("=== GIT HISTORY ANALYSIS ===")
print()

# Check if phd_env exists in history
print("1. Checking if phd_env was committed...")
out, err = run_cmd("git log --oneline -- phd_env 2>/dev/null | head -1")

if out:
    print("   ❌ phd_env WAS committed")
    print()
    print("   Commits that touched phd_env:")
    out, _ = run_cmd("git log --oneline -- phd_env 2>/dev/null | head -10")
    for line in out.split('\n'):
        print(f"     {line}")
    print()
    
    # Check repository size
    out, _ = run_cmd("git count-objects -vH | grep size-pack")
    if out:
        print(f"   Current repository size: {out}")
    
    print()
    print("   ⚠️  RECOMMENDED ACTION:")
    print("   Since phd_env contains 100+ MB of files, you should:")
    print("   1. Backup your work: git stash")
    print("   2. Clean history (if working alone):")
    print("      git filter-branch --force --index-filter")
    print("      \"git rm --cached --ignore-unmatch -r phd_env\"")
    print("      --prune-empty --tag-name-filter cat -- --all")
    print("   3. Force push: git push origin --force --all")
    print("   WARNING: This rewrites Git history!")
    
else:
    print("   ✅ phd_env was NEVER committed")
    print()
    print("   🎉 Your repository is clean!")
    print("   Just push your changes:")
    print("   git push origin main")

print()
print("2. Checking current .gitignore...")
out, _ = run_cmd("grep -c 'phd_env' .gitignore")
if int(out or 0) > 0:
    print("   ✅ .gitignore properly excludes phd_env")
else:
    print("   ❌ .gitignore missing phd_env")

print()
print("3. Current untracked files (should NOT include phd_env):")
out, _ = run_cmd("git status --porcelain | grep '^??' | head -5")
if out:
    for line in out.split('\n'):
        print(f"   {line[3:]}")
else:
    print("   No untracked files")

print()
print("=== SUMMARY ===")
if not out:  # If phd_env not in history
    print("✅ Your Git setup is correct!")
    print("   Use ./git_safe.sh for safe operations")
else:
    print("❌ Need to clean Git history")
