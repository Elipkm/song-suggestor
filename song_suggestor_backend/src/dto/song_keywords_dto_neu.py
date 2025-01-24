from typing import List

class KeywordDto:
    def __init__(self, keyword, keyword_id):
        self.keyword = keyword
        self.keyword_id = keyword_id
class SongKeywordsDtoNeu:

    def __init__(self, song_id: int, keywords: List[KeywordDto]):
        self.keywords = keywords
        self.song_id = song_id

    def __str__(self):
        return f"{self.song.title} keywords: {self.keywords}"
        
