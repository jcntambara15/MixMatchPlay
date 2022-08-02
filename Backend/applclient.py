from os import spawnlpe
from Spotify import spotifyPlaylist as sp
from Apple import AppleMusicClient as amc

client = amc(
    "",
    "",
    "developer_token",
    access_token= ""
)

class Apple_music_client(sp):
    def __init__(self):
        self.playlist_url = None
        self.playlist_name = sp.playlist_name
        self.playlist_image = sp.playlist_image
        self.number_of_songs = sp.number_of_songs
        self.song_list = sp.song_list
        self.artists_list = sp.artists_list
        self.album_list = sp.album_list
    
def convert_to_apple_music():
    amc.search()