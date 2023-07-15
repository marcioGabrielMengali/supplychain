import os
import pandas as pd

def read_csv_file_chunk(path, file):
    """Funtion to read csv into chunksizes"""
    print(f'\t>> Reading file {file}')
    full_path = os.path.join(path,file)
    try:
        return pd.read_csv(full_path, encoding='latin1', chunksize=10000)
    except Exception as e:
        print(f'Error to read file: {str(e)}')

def read_csv_file(path, file):
    """Funtion to read csv into chunksizes"""
    print(f'\t>> Reading file {file}')
    full_path = os.path.join(path,file)
    try:
        return pd.read_csv(full_path, encoding='latin1')
    except Exception as e:
        print(f'Error to read file: {str(e)}')


def save_file_as_json(path, df, file_name):
    """Function to Save dataframe as json"""
    print(f'\t>> Saving File {file_name}')
    full_path = os.path.join(path,file_name)
    try:
        df.to_json(full_path, orient='records')
    except Exception as e:
        print(f'Error to save file: {str(e)}')