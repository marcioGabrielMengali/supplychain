from colorama import Fore
from utils.get_file import get_file
from utils.csv import CSV
from utils.tables import dict_tables
from utils import etl


def pipeline(read_path:str, save_path:str) -> None:
    """Function to start run the pipeline"""
    print(Fore.BLUE + '> Starting Pipeline')
    file = get_file(path=read_path)
    csv = CSV(
        read_path=read_path,
        save_path=save_path
    )
    
    for key, value in dict_tables.items():
        dataframes = csv.read_csv_chunks(filename=file, enconding='latin1')
        table = etl.make_table(
            table_name=key,
            files = dataframes,
            columns=value['columns'],
            flag=value['flag'],
            subset=value['subset']
        )
        csv.csv_to_json(
            filename=key,
            dataframe=table
        )
        
