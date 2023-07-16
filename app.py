from dotenv import load_dotenv
import os

#My libraries
from utils import csv
from utils import columns
from utils import tables


def pipeline(read_path, file, save_path):
    """Function to start the pipeline"""
    print('> Starting Pipeline')
    files = csv.read_csv_file_chunk(path=read_path, file=file)
    print('>> Starting Tb Fact Sales')
    tables.customers(files=files, columns=columns.dict_columns['sales'], save_path=save_path)
    print('\t>> Tb Fact sales Compelted')




if __name__ == '__main__':
    load_dotenv()
    read_path = os.getenv('READ_PATH')
    file = os.getenv('FILE_NAME')
    save_path = os.getenv('SAVE_PATH')
    pipeline(
        read_path=read_path,
        file=file,
        save_path=save_path
    )