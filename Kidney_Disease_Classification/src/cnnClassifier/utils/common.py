import os
from box import ConfigBox
import yaml
import json
import base64
import joblib
from typing import Any
from pathlib import Path
from cnnClassifier import logger
from ensure import ensure_annotations
from box.exceptions import BoxValueError

# hERE WE ARE DEFINING SOME COMMON UTILITIES, CODES USED IN THE ENTIRED PROJECT LIKE READING AND WRITING YAML/JSON FILES, SAVING/LOADING OBJECTS USING JOBLIB, ETC.
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Raises:
        e (BoxValueError): If there is an error in reading the YAML file.
        valueError: If the file is empty or not properly formatted.
    
    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox object.
    """
    
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError(f"The file at {path_to_yaml} is empty or not properly formatted.")
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error reading the YAML file at {path_to_yaml}: {e}")
        raise e
    except ValueError as ve:
        logger.error(f"Value error: {ve}")
        raise ve
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they do not exist.

    Args:
        path_to_directories (list[Path]): List of directory paths to create.
        verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved.
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"JSON file saved at: {path}")
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns its contents as a dictionary.

    Args:
        path (Path): Path to the JSON file.
        
    Returns:
        ConfigBox: Contents of the JSON file as a ConfigBox object.
    """
    with open(path, 'r') as json_file:
        content = json.load(json_file)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves an object to a binary file using joblib.

    Args:
        data (Any): Data to be saved.
        path (Path): Path to the binary file.
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads an object from a binary file using joblib.

    Args:
        path (Path): Path to the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded successfully from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of a file in kilobytes (KB).

    Args:
        path (Path): Path to the file. 
        
    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    logger.info(f"File size for {path} is {size_in_kb} KB")
    return f"{size_in_kb} KB"

@ensure_annotations
def decodeImage(imgString, filemame):
    """Decodes a base64 encoded image string and saves it as an image file.

    Args:
        imgString (str): Base64 encoded image string.
        filemame (Path): Path where the decoded image will be saved.
    """
    imgdata = base64.b64decode(imgString)
    with open(filemame, 'wb') as f:
        f.write(imgdata)
        f.close()
    logger.info(f"Image decoded and saved at: {filemame}")
    
@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    """Encodes an image file into a base64 string.

    Args:
        croppedImagePath (Path): Path to the image file.
        
    Returns:
        str: Base64 encoded string of the image.
    """
    with open(croppedImagePath, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    logger.info(f"Image at {croppedImagePath} encoded into base64 string")
    return my_string.decode('utf-8')