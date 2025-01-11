from elasticsearch import Elasticsearch

# Initialize Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Create an index for songs
def create_index():
    index_body = {
        "mappings": {
            "properties": {
                "title": {"type": "text"},
                "artist": {"type": "text"},
                "genre": {"type": "keyword"},
                "language": {"type": "keyword"},
                "region": {"type": "keyword"},
                "release_year": {"type": "integer"}
            }
        }
    }
    es.indices.create(index="songs", body=index_body, ignore=400)

create_index()
