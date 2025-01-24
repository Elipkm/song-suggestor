from typing import List
from config.application_factory import get_db_connection
from dto.suggestion_result_dto import SongAnalysisDto, SuggestionDto
from src.config.properties import get_properties
from src.dto.song_dto import SongDto

SONG_DATA_TABLE_NAME = get_properties().song_data_table
SONG_KEYWORD_TABLE_NAME = get_properties().song_keyword_table

def get_suggestion_dto_by_song_id(song_id) -> SuggestionDto:
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    # read song
    print("start reading songs from: " + SONG_DATA_TABLE_NAME)
    cursor.execute("select title, artist, lyrics from " + SONG_DATA_TABLE_NAME + " where id = :id", (song_id,))
    row = cursor.fetchone()
    print(row)
    title = row[0]
    artist = row[1]
    lyrics = row[2]

    song = SongDto(title, artist, lyrics)
    song.set_id(song_id)

    # read keywords
    keywords: List[str] = []
    print("start reading keywords from: " + SONG_KEYWORD_TABLE_NAME)
    cursor.execute("select keyword from " + SONG_KEYWORD_TABLE_NAME + " where song_id = :id order by keyword_id", (song_id,))
    for row in cursor:
        keywords.append(row[0])

    song_analysis = SongAnalysisDto(keywords)
    suggestion = SuggestionDto(title, artist, lyrics, song_analysis)

    return suggestion