

class SongDto:

    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics


    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    def set_id(self, id):
        self.id = id
        
