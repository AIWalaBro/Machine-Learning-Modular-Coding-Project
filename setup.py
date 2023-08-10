from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Machine Learning Project"
VERSION = "0.0.1"
DESCRIPTION = "this is the machine learning project in the modular coding"
AUTHOR_NAME = "Bharatbhushan Dwarkewasi"
AUTHOR_EMAIL = "aiwalabro@gmail.com"


REQUIREMENT_FILE_NAME = "requirements.txt"
HYPEN_E_DOT = "-e ."


# requirement.txt file open 
# read that file
# remove the \n from the file

def get_requirements_list()-> List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        
        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)
            
        return requirement_list

# 

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages = find_packages(),
      install_requries = get_requirements_list() 
     )