from typing import List


class SongAnalysisDto:
    def __init__(self, analysis: List[str]):
        self.analysis = analysis

    def to_dict(self):
        return {
            'analysis': self.analysis
        }
class SuggestionDto:
    title: str
    artist: str
    lyrics: str
    analysis: SongAnalysisDto

    def __init__(self, title, artist, lyrics, analysis):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics
        self.analysis = analysis

    def to_dict(self):
        return {
            'title': self.title,
            'artist': self.artist,
            'lyrics': self.lyrics,
            'analysis': self.analysis.to_dict()
        }

class SuggestionResultDto:
    suggestionList: List[SuggestionDto]
    inputSongAnalysis: SongAnalysisDto

    def __init__(self, suggestionList: List[SuggestionDto], inputSongAnalysis: SongAnalysisDto):
        self.suggestionList = suggestionList
        self.inputSongAnalysis = inputSongAnalysis

    def to_dict(self):
        return {
            'suggestionList': [suggestion.to_dict() for suggestion in self.suggestionList],
            'inputSongAnalysis': self.inputSongAnalysis.to_dict()
        }
