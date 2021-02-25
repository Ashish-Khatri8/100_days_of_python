# Day 46 project - Musical Time Machine.

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Create your own app at https://developer.spotify.com/dashboard/applications.
# And add "http://example.com" as Redirect URI to your app.
SPOTIFY_CLIENT_ID = "your own client id"
SPOTIFY_CLIENT_SECRET = "your own client secret"


# Scraping Billboard 100 and getting the names of top 100 songs.
date = input("Which year do you want to travel to?\nType the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.find_all(name="span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]


# Spotify Authentication.
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]


# Searching Spotify for songs by title/name.
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    # If song found in spotify, add its uri to song_uris.
    # Else tell the user that the song was not found.
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# Creating a new private playlist in Spotify.
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding the songs that were found to the new playlist.
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
