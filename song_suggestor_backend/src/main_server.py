from flask import Flask, request, jsonify
from flask_cors import CORS

import sys
import os
current_directory = os.getcwd()
sys.path.append(current_directory)

from config.application_factory import get_embeddings_instance
from dto.suggestion_result_dto import SuggestionResultDto
from service.suggestion_service import get_suggestion_for_lyrics
from service.song_embedding_service import embed_keyword_table_to_vector_store


app = Flask(__name__)
CORS(app)

# load embedding instance directly when starting
get_embeddings_instance()

@app.route('/api/suggest', methods=['POST'])
def handle_post():
    if not request.is_json:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    data = request.get_json()
    input_lyrics = data['inputLyrics']
    print("lyrics: " + input_lyrics)
    result: SuggestionResultDto = get_suggestion_for_lyrics(input_lyrics)
    response = result.to_dict()
    
    return jsonify(response), 200

@app.route('/api/setup', methods=['POST'])
def handle_post_setup():
    embed_keyword_table_to_vector_store()
    response = "Setup successful"
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
