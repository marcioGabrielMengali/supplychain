#Functions to hadle files inside folders
import os
from colorama import Fore
from utils.path import make_path

def get_file(path:str) -> list:
    """Funtion to return files inside a path"""
    print(Fore.YELLOW + '>> Getting File')
    try:
        file = os.listdir(path)
    except Exception as e:
        print(Fore.RED + f'\t >>>Error to find files: {str(e)}')
    print(Fore.GREEN + f'\t>>> {file}')
    return file