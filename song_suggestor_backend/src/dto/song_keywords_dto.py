from typing import List

class SongKeywordsDto:

    def __init__(self, song_id: int, keywords: List[str]):
        self.keywords = keywords
        self.song_id = song_id

    def __str__(self):
        return f"{self.song.title} keywords: {self.keywords}"
        