import requests
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def fetch_and_store_songs():
    api_url = "https://api.sampleapis.com/songs/music"  # Replace with a real API
    response = requests.get(api_url)
    if response.status_code == 200:
        songs = response.json()
        for song in songs:
            es.index(index="songs", document=song)
    else:
        print("Failed to fetch data")

fetch_and_store_songs()
