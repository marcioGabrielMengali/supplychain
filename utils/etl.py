#Function to perform ETL
from colorama import Fore
import pandas as pd

def make_table(table_name:str, files:list, columns:list) -> pd.DataFrame:
    """Function to return table based on selected columns"""
    print(Fore.YELLOW + f'>> Making Table: {table_name}')
    table = pd.DataFrame()
    for file in files:
        aux_table = file[columns]
        table = pd.concat(
            [table, aux_table],
            axis=0
        )
    print(Fore.CYAN + f'\t >>>Table Informations (Shape): {table.shape}')
    print(Fore.CYAN + f'\t >>>Table Informations (Columns): {table.columns}')
    return table