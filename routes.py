from fastapi import FastAPI, Query
from elasticsearch import Elasticsearch

app = FastAPI()
es = Elasticsearch("http://localhost:9200")

@app.get("/search")
def search_songs(
    query: str = Query(None), 
    genre: str = Query(None),
    language: str = Query(None),
    release_year: int = Query(None)
):
    search_body = {"query": {"bool": {"must": []}}}
    
    if query:
        search_body["query"]["bool"]["must"].append({
            "multi_match": {
                "query": query,
                "fields": ["title", "artist"]
            }
        })
    if genre:
        search_body["query"]["bool"]["must"].append({"term": {"genre": genre}})
    if language:
        search_body["query"]["bool"]["must"].append({"term": {"language": language}})
    if release_year:
        search_body["query"]["bool"]["must"].append({"term": {"release_year": release_year}})
    
    results = es.search(index="songs", body=search_body)
    return {"songs": [hit["_source"] for hit in results["hits"]["hits"]]}
