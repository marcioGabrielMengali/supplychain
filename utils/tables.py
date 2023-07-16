# Codes to create the fact table and dimensional tables
import pandas as pd
from utils import csv


def customers(files, columns, save_path):
    """Funtion to create the customers dimensional table"""
    tb_dim_customers = pd.DataFrame()
    for file in files:
        df = file[columns]
        tb_dim_customers = pd.concat(
            [tb_dim_customers, df],
            ignore_index=True,
            axis=0
        )
        del df
        tb_dim_customers.drop_duplicates(subset='Customer Id', inplace=True)
    print(f'\t>>> tb_dim_customers COMPLETED: informations: {tb_dim_customers.shape}')
    csv.save_file_as_json(path=save_path, df=tb_dim_customers, file_name='tb_dim_customers.json')

def customers(files, columns, save_path):
    """Funtion to create the customers dimensional table"""
    tb_fact_sales = pd.DataFrame()
    for file in files:
        df = file[columns]
        tb_fact_sales = pd.concat(
            [tb_fact_sales, df],
            ignore_index=True,
            axis=0
        )
        del df
    print(f'\t>>> tb_dim_customers COMPLETED: informations: {tb_fact_sales.shape}')
    csv.save_file_as_json(path=save_path, df=tb_fact_sales, file_name='tb_fact_sales.json')
