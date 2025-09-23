import os
from box.exceptions import BoxValueError
import yaml
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from typing import Any, Dict
from text_summarization.logging import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> configbox:
    """Reads a yaml file and returns the contents as a dictionary

    Args:
        path_to_yaml (Path): Path to the yaml file

    Raises:
        BoxValueError: If the yaml file is empty

    Returns:
        Dict[str, Any]: Contents of the yaml file as a dictionary
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise BoxValueError("YAML file is empty")
            return content
    except BoxValueError:
        raise BoxValueError("YAML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates list of directories

    Args:
        path_to_directories (list): List of paths to directories
        verbose (bool, optional): Whether to log the created directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of the file in KB

    Args:
        path (Path): Path to the file

    Returns:
        str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"~ {size_in_kb} KB"


