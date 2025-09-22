import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "text_summarization"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/constant.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "pyproject.toml",
    "research/trials.ipynb"
]

for file_path_str in list_of_files:
    file_path = Path(file_path_str)
    dir_path = file_path.parent

    try:
        if dir_path and not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {dir_path}")

        if not file_path.exists() or file_path.stat().st_size == 0:
            file_path.touch(exist_ok=True)
            logging.info(f"Created file: {file_path}")
        else:
            logging.info(f"{file_path.name} already exists and is not empty, skipping creation.")
    except Exception as e:
        logging.error(f"Error creating {file_path}: {e}")