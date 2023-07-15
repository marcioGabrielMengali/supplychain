from dotenv import load_dotenv
import os

#My libraries
from utils import csv
from utils import columns
from utils import tables


def pipeline(read_path, file, desc_file, save_path):
    """Function to start the pipeline"""
    print('> Starting Pipeline')
    files = csv.read_csv_file_chunk(path=read_path, file=file)
    description_file = csv.read_csv_file(
        path=os.getcwd(),
        file=desc_file
    )
    table_columns = columns.extract_columns(file=description_file)
    print('>> Starting Tb Dim Customers')
    tables.customers(files=files, columns=table_columns['customer'], save_path=save_path)
    print('>> Tb_dim_customers Compelted')







if __name__ == '__main__':
    load_dotenv()
    read_path = os.getenv('READ_PATH')
    file = os.getenv('FILE_NAME')
    desc_file = os.getenv('DESCRIPTION_FILE')
    save_path = os.getenv('SAVE_PATH')
    pipeline(
        read_path=read_path,
        file=file,
        desc_file=desc_file,
        save_path=save_path
    )