import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_module import SpotifyModule

class TrackModule:

    def __int__(self, track_id: int, track_name: str, track_author: str, track_album: str):
        self.track_id = track_id
        self.track_name = track_name
        self.track_author = track_author
        self.track_album = track_album

    def get_track(self, sp):
        sp.search()