import configparser

properties_instance = None
CONFIG_FILE_PATH = 'src/config/config.ini'

class Properties:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE_PATH)

        self.es_url = config.get('elasticsearch', 'es_url')
        self.es_index = config.get('elasticsearch', 'es_index')

        self.number_of_keyword_search_results = config.getint('search', 'number_of_keyword_search_results')

        self.number_of_suggestions = config.getint('suggestor', 'number_of_suggestions')

        self.song_data_table = config.get('database', 'song_data_table')
        self.song_keyword_table = config.get('database', 'song_keyword_table')
    
    
def get_properties() -> Properties:
    global properties_instance
    if(properties_instance is None):
        properties_instance = Properties()
    return properties_instance
