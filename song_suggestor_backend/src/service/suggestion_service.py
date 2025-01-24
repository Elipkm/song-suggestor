
from typing import List
from config.application_factory import get_db_connection
from dao.sql_song_dao import get_suggestion_dto_by_song_id
from dto.suggestion_result_dto import SongAnalysisDto, SuggestionDto, SuggestionResultDto
from src.service.elasticsearch_similarity_service import find_similar_song_ids
from src.dao.es_song_database import ElasticsearchSongDatabase 
from src.config.properties import get_properties
from src.dto.song_keywords_dto import SongKeywordsDto
from src.service.llm_service import get_keywords_for_lyrics

def get_suggestion_for_lyrics(input_lyrics: str) -> SuggestionResultDto:
    properties = get_properties()
    vector_store = ElasticsearchSongDatabase()

    input_lyrics_keywords: List[str] = get_keywords_for_lyrics(input_lyrics)
    keywords_dto = SongKeywordsDto(-1, input_lyrics_keywords)
    input_analysis_dto: SongAnalysisDto = SongAnalysisDto(input_lyrics_keywords)

    similar_song_ids = find_similar_song_ids(keywords_dto, vector_store)

    print("Found Similar Songs:")
    suggestion_list: List[SuggestionDto] = []
    
    if similar_song_ids is None or len(similar_song_ids) == 0:
        print("No song suggestions found")
    else:
        for suggestion in similar_song_ids[:properties.number_of_suggestions]:
            print("Suggestion found")
            print("song id: " + str(suggestion))
            suggestion_dto: SuggestionDto = get_suggestion_dto_by_song_id(suggestion)
            suggestion_list.append(suggestion_dto)

    result: SuggestionResultDto = SuggestionResultDto(suggestion_list, input_analysis_dto)

    #close ES und SQl
    vector_store.close()
    get_db_connection().close()

    return result