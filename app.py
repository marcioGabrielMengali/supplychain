import os

from dotenv import load_dotenv

from utils.pipeline import pipeline


if __name__ == '__main__':
    load_dotenv()
    read_path = os.getenv('READ_PATH')
    save_path = os.getenv('SAVE_PATH')
    pipeline(
        read_path=read_path,
        save_path=save_path
    )