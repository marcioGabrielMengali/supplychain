import pandas as pd

def extract_columns(file):
    print('>> Getting Columns')
    columns = file['FIELDS'].tolist()
    dict_of_columns = {}
    dict_of_columns['customer'] = [x for x in columns if 'Customer' in x and 'Order Customer Id' not in x]
    print(f'\t>>> {dict_of_columns}')
    return dict_of_columns
