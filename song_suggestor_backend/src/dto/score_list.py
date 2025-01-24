from src.dto.song_dto import SongDto


class ScoreList:
    def __init__(self):
        # Initialize with an empty list of scores
        self.scores = []

    def add_entry(self, song_id):
        """Adds a new entry with the given ID and an initial score."""
        self.scores.append({'song_id': song_id, 'score': 0, 'weighted_score': 0})

    def add_score(self, song_id, score_to_add):
        """Adds a score to the entry with the given ID."""
        if not self.is_entry_present(song_id):
            self.add_entry(song_id)
        # Find the entry by id and add the score
        for entry in self.scores:
            if entry['song_id'] == song_id:
                entry['score'] += score_to_add
                return
        # If the entry doesn't exist, print an error message
        print(f"Entry with id {song_id} not found!")

    def add_weighted_score(self, song_id, score_to_add):
        """Adds a score to the entry with the given ID."""
        if not self.is_entry_present(song_id):
            self.add_entry(song_id)
        
        # Find the entry by id and add the score
        for entry in self.scores:
            if entry['song_id'] == song_id:
                entry['weighted_score'] += score_to_add
                return
        # If the entry doesn't exist, print an error message

    def is_entry_present(self, song_id):
        """Returns True if the entry with the given ID is present in the list."""   
        for entry in self.scores:
            if entry['song_id'] == song_id:
                return True
            
        return False
    def get_scores(self):
        """Returns the current list of entries with their scores."""
        return self.scores

    def get_ordered_scores(self):
        """Returns the list of entries ordered by the highest score first."""
        # Sort by score in descending order
        return sorted(self.scores, key=lambda x: x['score'], reverse=True)

    def get_ordered_weighted_scores(self):
        """Returns the list of entries ordered by the highest weighted score first."""
        # Sort by score in descending order
        return sorted(self.scores, key=lambda x: x['weighted_score'], reverse=True)
