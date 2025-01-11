import streamlit as st
import requests

st.title("Music Search App")

query = st.text_input("Search songs by title or artist")
genre = st.selectbox("Select Genre", ["Pop", "Rock", "Jazz"])
language = st.selectbox("Select Language", ["English", "Spanish"])
release_year = st.number_input("Release Year", min_value=1900, max_value=2025)

if st.button("Search"):
    params = {"query": query, "genre": genre, "language": language, "release_year": release_year}
    response = requests.get("http://localhost:8000/search", params=params)
    results = response.json()["songs"]
    for song in results:
        st.write(f"**{song['title']}** by {song['artist']} ({song['release_year']})")
