from user_utils import UserUtils
from data_manager import DataManager
from spotify_module import SpotifyModule
from envr import CLIENT_SECRET, CLIENT_ID, URI
import pprint

pp = pprint.PrettyPrinter(indent=4)

URL = 'https://www.billboard.com/charts/hot-100'
date_from_user = UserUtils.get_date_from_user()

website_access = DataManager.scrape_website(URL, date_from_user)
soup = DataManager.get_content_from_website(website_access)


songs_titles = [title.getText() for title in soup.find_all(name='span', class_='chart-element__information__song'
                                                                               ' text--truncate color--primary')]
songs_authors = [title.getText() for title in soup.find_all(name='span', class_='chart-element__information__artist'
                                                                                ' text--truncate color--secondary')]

spotify = SpotifyModule(CLIENT_ID, CLIENT_SECRET, URI)
spotify_auth = spotify.authenticate_spotify()
user_id = spotify_auth.current_user()['id']

song_uris = []
for song in songs_titles:
    result = spotify_auth.search(q='track:' + song, type='track')
    try:
        uri = result['tracks']['items'][0]['album']['uri']
        print(uri)
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)

