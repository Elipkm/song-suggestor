import datetime
from typing import List
from config.application_factory import get_db_connection
from dao.es_song_database import ElasticsearchSongDatabase
from src.config.logger import create_logger
from src.config.properties import get_properties
from src.dto.song_keywords_dto_neu import SongKeywordsDtoNeu, KeywordDto


""" this service is used for setting up and filling the vector store """
def embed_keyword_table_to_vector_store():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    logger = create_logger("main_song_embedding_")
    logger.info("start: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    song_id_list = get_target_song_ids(cursor)
    logger.info("number of target songs: " + str(len(song_id_list)))

    song_keywords_dto_list = get_song_keywords_dto_list_by_id(song_id_list, cursor)

    cursor.close()
    db_connection.close()

    vector_store = ElasticsearchSongDatabase()
    logger.info("get vector store for index name: " + get_properties().es_index)

    logger.info("song_keywords_dto list length: " + str(len(song_keywords_dto_list)))
    for song_keywords_dto in song_keywords_dto_list:
        vector_store.add_song_keywords(song_keywords_dto)
        logger.info("added song with id: " + str(song_keywords_dto.song_id))

    vector_store.close()
    logger.info("end: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def get_target_song_ids(cursor) -> List[int]:
    SONG_TABLE_NAME = get_properties().song_data_table

    cursor.execute("select distinct id from " + SONG_TABLE_NAME)
    rows = cursor.fetchall()
    song_id_list = []
    for row in rows:
        song_id_list.append(row[0])

    return song_id_list

def get_song_keywords_dto_list_by_id(song_id_list: List[int], cursor: any) -> List[SongKeywordsDtoNeu]:
    song_keywords_dto_list: List[SongKeywordsDtoNeu] = []
    KEYWORD_TABLE_NAME = get_properties().song_keyword_table
    for song_id in song_id_list:
        cursor.execute("select keyword, keyword_id from " + KEYWORD_TABLE_NAME + " where song_id = " + str(song_id))
        keywords = []
        for row in cursor:
            keyword = row[0]
            keyword_id = row[1]
            keyword_dto: KeywordDto = KeywordDto(keyword, keyword_id)
            keywords.append(keyword_dto)

        song_keywords_dto = SongKeywordsDtoNeu(song_id, keywords)
        song_keywords_dto_list.append(song_keywords_dto)

    return song_keywords_dto_list