# Function to perform ETL
from colorama import Fore
import pandas as pd


def make_table(table_name: str, files, columns: list, flag: str, subset: list, rename_columns: dict) -> pd.DataFrame:
    """Function to return table based on selected columns"""
    print(Fore.YELLOW + f'>> Making Table: {table_name}')
    table = pd.DataFrame()
    if flag == 'fact':
        for file in files:
            aux_table = file[columns]
            table = pd.concat(
                [table, aux_table],
                axis=0
            )
    elif flag == 'dim':
        for file in files:
            aux_table = file[columns]
            table = pd.concat(
                [table, aux_table],
                axis=0
            )
            table.drop_duplicates(subset=subset, inplace=True)
    table.rename(columns=rename_columns, inplace=True)
    print(Fore.CYAN + f'\t >>>Table Informations (Shape): {table.shape}')
    print(Fore.CYAN + f'\t >>>Table Informations (Columns): {table.columns}')
    return table
