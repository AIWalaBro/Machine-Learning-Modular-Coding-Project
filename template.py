import sys
import os
from pathlib import Path
import logging

while True:
    project_name = input('enter your project name:')
    if project_name != "":
            break

#src/__init__.py 
#src/Components/__init__.py      
list_of_files = [
    f"{project_name}/__init__.py ",
    f"{project_name}/Components/__init__.py",
    f"{project_name}/Config/__init__.py",
    f"{project_name}/Constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
    
]

# for loop defined to split the files and folders

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        logging.info(f"file already exits at:{filepath}")
    
        