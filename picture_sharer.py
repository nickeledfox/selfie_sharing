from filestack import Client
from dotenv import load_dotenv
from pathlib import Path
import os

# Take environment variables from .env
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv('FILESTACK')

class FileSharer:
    def __init__(self, filepath, api_key=API_KEY):
        self.file_path = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file_link =\
            client.upload(filepath=self.file_path)
        return new_file_link.url
