import json

class ArtistFileService:
    def __init__(self, filename):
        self.filename = filename

    def get_artists(self):
        with open(self.filename) as data_file:    
            data = json.load(data_file)

        return data
