from sqlalchemy import create_engine
import os
from colorama import Fore

def create_connection_string() -> None:
    """Function to create enngine to upload files"""
    print(Fore.YELLOW + f">> Making connection String")
    host = os.getenv('HOST')
    user = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    port = os.getenv('PORT')
    database = os.getenv('DATABASE')
    return create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    )