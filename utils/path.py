# here is functions to handdle paths
import os

def make_path(path:str, file:str) -> str:
    """Function to make path based on OS"""
    return os.path.join(path, file)

def make_save_path(path:str, file:str) -> str:
    """Function to make path based on OS to save the file etih json extension"""
    return os.path.join(path, f'{file}.json')