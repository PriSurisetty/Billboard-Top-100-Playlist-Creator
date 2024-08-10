from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ----------------------- Creates song list ----------------------------#

user_choice = input("Which year do you want to travel to? "
                    "Type the data in this format YYYY-MM-DD: ")


response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_choice}/")
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")


class_name = "c-title"


songs = soup.find_all(name="h3", class_=class_name)
song_titles = []

for song in songs:
    text = song.text.strip()
    if text and not any(keyword in text for keyword in
                        ["Songwriter(s):", "Producer(s):", "Imprint/Promotion Label:",
                         "Gains in Weekly Performance", "Additional Awards"]):
        song_titles.append(text)


song_titles = song_titles[1:101]

# ----------------------- Creates Spotify playlist ----------------------------#

SPOTIFY_ID = os.environ.get("SPOTIFY_ID").strip()
SPOTIFY_SECRET = os.environ.get("SPOTIFY_SECRET").strip()
SPOTIFY_REDIRECT_URI = "http://example.com"
SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME").strip()

scope = "playlist-modify-private playlist-modify-public"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_USERNAME
    )
)

user_id = sp.current_user()["id"]
# print(user_id)
uris = []
for title in song_titles:
    result = sp.search(q=title, type="track")
    if result["tracks"]["items"]:
        uris.append(result["tracks"]["items"][0]["uri"])
    else:
        print(f"Song {title} not found on Spotify")

PLAYLIST_ID = sp.user_playlist_create(user=user_id,
                                      public=False,
                                      name=f"{user_choice} BillBoard-100")['id']

sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=uris)
