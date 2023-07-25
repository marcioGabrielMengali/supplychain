import pandas as pd
from colorama import Fore
from utils.path import make_path

def read_json(path:str, file:str) -> list:
    """Function to read json into chunks"""
    print(Fore.YELLOW + f"Reading File: {file}")
    path = make_path(path=path, file=file)
    try:
        return pd.read_json(
            path,
            orient='records',
            chunksize=10000,
            lines=True
        )
    except Exception as e:
        print(Fore.RED + f"Error to read json file: {str(e)}")