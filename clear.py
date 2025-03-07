#!/usr/bin/env python3
import os
import shutil
import sys

def remove_pycache(directory="."):
    """
    Recursively removes all __pycache__ directories and .pyc files
    starting from the specified directory.
    """
    count_dirs = 0
    count_files = 0
    
    print(f"Searching for Python cache files in: {os.path.abspath(directory)}")
    
    # Walk through all directories
    for root, dirs, files in os.walk(directory):
        # Remove __pycache__ directories
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            print(f"Removing directory: {pycache_path}")
            shutil.rmtree(pycache_path)
            count_dirs += 1
            dirs.remove("__pycache__")  # Prevent os.walk from going into the deleted directory
        
        # Remove .pyc files
        for file in files:
            if file.endswith(".pyc") or file.endswith(".pyo"):
                pyc_file = os.path.join(root, file)
                print(f"Removing file: {pyc_file}")
                os.remove(pyc_file)
                count_files += 1
    
    print(f"\nCleanup complete!")
    print(f"Removed {count_dirs} __pycache__ directories and {count_files} .pyc/.pyo files.")

if __name__ == "__main__":
    # Use command line argument as directory if provided, otherwise use current directory
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    remove_pycache(directory)
