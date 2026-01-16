#!/bin/bash
# Safe Git workflow for PhD research

echo "=== SAFE GIT WORKFLOW ==="
echo ""

# Check status
echo "1. Current status:"
git status --short

echo ""
echo "2. Files that WILL be ignored (from .gitignore):"
grep -v "^#" .gitignore | grep -v "^$" | head -10

echo ""
echo "3. Recommended action:"
echo "   To add specific file: git add path/to/file"
echo "   To add all tracked changes: git add -u"
echo "   NEVER use: git add ."
echo ""

echo "4. Current branch:"
git branch --show-current

echo ""
read -p "Do you want to add files? (y/n): " add_choice

if [ "$add_choice" = "y" ]; then
    echo ""
    read -p "Enter file/directory to add (or press Enter to skip): " files_to_add
    
    if [ -n "$files_to_add" ]; then
        git add "$files_to_add"
        echo "✅ Added: $files_to_add"
        
        echo ""
        read -p "Enter commit message: " commit_msg
        if [ -n "$commit_msg" ]; then
            git commit -m "$commit_msg"
            echo "✅ Committed"
            
            read -p "Push to GitHub? (y/n): " push_choice
            if [ "$push_choice" = "y" ]; then
                git push origin $(git branch --show-current)
                echo "✅ Pushed"
            fi
        fi
    fi
fi

echo ""
echo "=== DONE ==="
