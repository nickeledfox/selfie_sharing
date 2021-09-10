class Sharing:
    def __init__(self, file_path, api_key=''):
        self.file_path = file_path
        self.api_key = api_key

def share(self):
    client = Client(self.api_key)
    new_file_link = client.upload(file_path=self.file_path)
    return new_file_link.url
