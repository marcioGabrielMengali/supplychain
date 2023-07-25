from multiprocessing import Pool
from colorama import Fore
from utils.json import read_json
from utils.database import create_connection_string
import pandas as pd

def upload_file(args) ->None:
    """Function to upload file to database"""
    print(Fore.CYAN + f"\t>> Upload File to Table {args[2]}" )
    engine = create_connection_string()
    dataframes = read_json(
        path=args[1],
        file=args[0]
    )
    for dataframe in dataframes:
        try:
            verify = dataframe.to_sql(
                args[2],
                con=engine,
                if_exists='append',
                index=False,
                method='multi',
                schema=args[3]
            )
            print(Fore.GREEN + f"\t\t>>> Upload Completd {args[2]}, {verify}")
        except Exception as e:
            print(Fore.RED + f"Error to upload table: {args[2]}", {str(e)})
            exit()


def start(files:list, path:str, schema:str) -> None:
    """Function to star upload files"""
    print(Fore.YELLOW + f">> Starting Upload Files")
    args = []
    for file in files:
        tablename = file.split('.')[0]
        arg = [file, path, tablename, schema]
        args.append(arg)
    with Pool(30) as p:
        p.map(upload_file, args)
    
        
    