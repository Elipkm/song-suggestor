import sqlite3
from sqlite3 import Connection
from langchain_elasticsearch import ElasticsearchStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_community.chat_models import ChatOpenAI
from config.properties import get_properties

def get_db_connection() -> Connection:
    return sqlite3.connect("database/song_suggestor_demo.db")

def get_llm() -> BaseChatModel:
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=2048,
        timeout=None,
        max_retries=2        
    )
    return llm

def get_vector_store():
    properties = get_properties()
    db = ElasticsearchStore(
        embedding=get_embeddings_instance(),
        es_url=properties.es_url,
        index_name=properties.es_index,
    )
    return db

embeddings = None
def get_embeddings_instance():
    global embeddings
    if embeddings is None:
        embeddings = HuggingFaceEmbeddings()
    return embeddings