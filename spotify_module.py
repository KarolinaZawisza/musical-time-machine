import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyModule:

    def __init__(self, client_id, client_secret, uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.uri = uri

    def authenticate_spotify(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                       client_secret=self.client_secret,
                                                       redirect_uri=self.uri,
                                                       scope="playlist-modify-private",
                                                       show_dialog=True,
                                                       cache_path="token.txt"
                                                       ))
        return sp

    @staticmethod
    def create_playlist(user_id, spotify, date):
        spotify.user_playlist_create(user=user_id, name=f'Musical Time Machine {date}')

    @staticmethod
    def add_tracks_to_playlist(spotify, user_id, playlist_id, tracks):
        spotify.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=tracks, position=None)