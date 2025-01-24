from typing import List, Tuple
from src.dto.score_list import ScoreList
from src.dao.es_song_database import ElasticsearchSongDatabase
from src.dto.song_keywords_dto import SongKeywordsDto
from src.config.properties import get_properties
from langchain_core.documents import Document 

"""
New Version. 2024-12-07
Keep keyword id == category in mind
Categories:

0: Central Themes
1: Emotional Impact
2: Narrator
3: Perspective
4: Core Message
5: Certainty
6: Language
7: Tone
8: Universal Human Experiences

"""
def find_similar_song_ids(arg_song: SongKeywordsDto, database: ElasticsearchSongDatabase) -> List[int]:   
    properties = get_properties()
    number_of_search_results = properties.number_of_keyword_search_results

    score_list: ScoreList = ScoreList()

    # assuming the index (0-8) is equal to the keyword_id
    keyword_weights = [
        1.0,     #0: Central Themes
        0.7,     #1: Emotional Impact
        0.2,     #2: Narrator
        0.1,     #3: Perspective
        1.5,     #4: Core Message
        0.1,     #5: Certainty
        0.5,     #6: Language
        1.0,     #7: Tone
        1.5      #8: Universal Human Experiences
    ]
    print("keyword weights: " + str(keyword_weights))
    for i, keyword in enumerate(arg_song.keywords):
        keyword_weight = keyword_weights[i]
        keyword_id = i
        similar_results: List[Tuple[Document, float]] = database.similarity_search_filter(keyword, keyword_id=keyword_id, k = number_of_search_results)
        for result in similar_results:
            result_score = result[1]
            result_score_weighted = result_score * keyword_weight
            doc = result[0]
            song_id = doc.metadata["song_id"]
            score_list.add_score(song_id, result_score)
            score_list.add_weighted_score(song_id, result_score_weighted)

    most_similar_songs = []
    for entry in score_list.get_ordered_weighted_scores():
        most_similar_songs.append(entry['song_id'])
        print("add to most similar: " + str(entry['song_id']) + " with score: " + str(entry['score']) + " and weighted score: " + str(entry['weighted_score']))
    return most_similar_songs
    