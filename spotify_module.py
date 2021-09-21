import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyModule:

    def __init__(self, client_id, client_secret, uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.uri = uri
        self.authenticate_spotify()

    def authenticate_spotify(self):
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://example.com",
                client_id=self.client_id,
                client_secret=self.client_secret,
                show_dialog=True,
                cache_path="token.txt"
            )
        )
        return sp