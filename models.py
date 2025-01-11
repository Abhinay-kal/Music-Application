from pydantic import BaseModel

class Song(BaseModel):
    title: str
    artist: str
    genre: str
    language: str
    region: str
    country: str
    release_year: int
