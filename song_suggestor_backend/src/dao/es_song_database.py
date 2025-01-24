
from typing import List, Tuple

from config.application_factory import get_vector_store
from dto.song_keywords_dto_neu import SongKeywordsDtoNeu
from langchain_core.documents import Document

class ElasticsearchSongDatabase():

    def __init__(self) -> None:
        self.db = get_vector_store()
    
    def similarity_search(self, query: str, k: int = 4) -> List[Tuple[Document, float]]:
        return self.db.similarity_search_with_relevance_scores(query=query, k=k)

    def similarity_search_filter(self, query: str, keyword_id: int, k: int = 4) -> List[Tuple[Document, float]]:
        return self.db.similarity_search_with_relevance_scores(query=query, k=k, 
            filter={"bool": {
                "filter": [{
                    "term": {"metadata.keyword_id": keyword_id}
                }]}
        })

    def add_song_keywords(self, song_keywords_dto: SongKeywordsDtoNeu):
        song_documents = []
        for keyword in song_keywords_dto.keywords:
            metadata = {
                "song_id": song_keywords_dto.song_id,
                "keyword_id": keyword.keyword_id
            }
            document = Document(
                page_content=keyword.keyword,
                metadata=metadata
            )
            song_documents.append(document)
        self.db.add_documents(song_documents)

    def close(self):        
        self.db.close()

