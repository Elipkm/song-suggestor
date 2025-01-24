
- Prerequisites
   - Set the following environment variables for OpenAi LLM 
      - OPENAI_API_KEY
      - OPENAI_ORGANIZATION
   - Run a local Elasticsearch (on port 9200)
1. Run Backend
   - cd song_suggestor_backend 
   - py src/main_server.py 
2. Run Setup to embed the demo song data - keywords into local elasticsearch
   - curl -X POST http://localhost:5000/api/setup
3. Run Frontend with ng serve
   - cd song_suggestor_ui
   - ng serve

 Technologies and Versions used:
   - Python: 3.10.7
   - ElasticSearch: 8.12.1
   - Angular: 19
   - PrimeNG
   - node: v22.12.0
   - npm: 11.0.0
