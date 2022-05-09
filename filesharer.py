from filestack import Client

file_stack_key = "ASGikRXqSuSaYhmmCl5B5z"


class FileSharer:

    def __init__(self, filepath, api_key="ASGikRXqSuSaYhmmCl5B5z"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
