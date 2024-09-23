#In this module we create project structure and logging those structure into logs file!!!
import os,sys
from pathlib import Path
from datetime import datetime
import logging

project_name = "Mask"

timestamp = datetime.now().strftime(format = "%d_%m_%Y_%H_%M_%S")

FORMAT = "[%(asctime)s]-%(lineno)d-%(message)s"

#creating an object of basicConfig class of logging module
logging.basicConfig(
    filename = f"log_{project_name}.log",
    filemode="w",
    level=logging.INFO,
    format=FORMAT,
)

#now creating list of files that contains project structure
files = [
    ".github/workflows/.gitkeep",
    "research/trials.ipynb",
    "config/config.yaml",
    "param.yaml",
    "Dockerfile",
    "requirements.txt",
    "main.py",
    "templates/index.html",
    "test.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/loggers.py",
    f"src/{project_name}/exceptions.py",
    f"src/{project_name}/Components/__init__.py",
    f"src/{project_name}/Constants/__init__.py",
    f"src/{project_name}/Config/__init__.py",
    f"src/{project_name}/Config/configuration.py",
    f"src/{project_name}/Utils/__init__.py",
    f"src/{project_name}/Utils/common.py",
    f"src/{project_name}/Entity/__init__.py",
    f"src/{project_name}/Entity/config_entity.py",
    f"src/{project_name}/Pipelines/__init__.py",
    f"src/{project_name}/Pipelines/training.py",
    f"src/{project_name}/Pipelines/prediction.py"
]

#iterating each filepath from list
for filepath in files:
    #using path class changing filepath to  window path
    filepath = Path(filepath)

    #splitting the filepath into directory and filename
    dirpath, filename = os.path.split(filepath)

    #checking if directory exist in project structure or not
    if dirpath!= "":
        os.makedirs(dirpath,exist_ok=True)
        logging.info(f"Directory {dirpath} created for files {filename} ")

    #now creating files or (filepath) in those directory and also checking the size of filepath
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "wb") as f:
            pass #this line created empty files in those directory
            logging.info(f"Empty file cretaed for {filepath}")
    else:
        logging.info(f"File {filepath} already exists")

