#class to handle csv

import pandas as pd

from utils.path import make_path
from utils.path import make_save_path
from colorama import Fore

class CSV:
    def __init__(self, read_path, save_path) -> None:
        self.read_path = read_path
        self.save_path = save_path
    

    def read_csv_chunks(self, filename:str, enconding:str) -> list:
        """Function to read file in chunks"""
        print(Fore.YELLOW + f'>> Reaading file: {filename}')
        path = make_path(path=self.read_path, file=filename)
        try:
            return pd.read_csv(path, encoding=enconding, chunksize=10000)
        except Exception as e:
            print(Fore.RED + f'>>> Error Read File: {str(e)}')
    

    def csv_to_json(self, filename:str, dataframe:pd.DataFrame) -> None:
        """Funtion to convert csv to json"""
        print(Fore.YELLOW + f'>> saving file: {filename}')
        path = make_save_path(path=self.save_path, file=filename)
        try:
            dataframe.to_json(
                path,
                orient='records'
            )
        except Exception as e:
            print(Fore.RED + f'>>> Error write File {str(e)}')

