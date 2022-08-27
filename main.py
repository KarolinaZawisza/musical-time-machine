import spotipy
from spotipy import SpotifyOAuth
from user_utils import UserUtils
from data_manager import DataManager
from spotify_module import SpotifyModule
# from envr import CLIENT_SECRET, CLIENT_ID
CLIENT_SECRET = ""
CLIENT_ID = ""

URL = 'https://www.billboard.com/charts/hot-100'
date = UserUtils.get_date_from_user()

website_access = DataManager.scrape_website(URL, date)
soup = DataManager.get_content_from_website(website_access)

song_names = [title.getText() for title in soup.find_all(name='span',
                                                         class_='chart-element__information__song'
                                                                ' text--truncate '
                                                                'color--primary')]
spotify_module = SpotifyModule(CLIENT_ID, CLIENT_SECRET, URL)
sp = spotify_module.authenticate_spotify()
user_id = sp.current_user()['id']

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"Musical Time Travel: top 100 from {date}", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
