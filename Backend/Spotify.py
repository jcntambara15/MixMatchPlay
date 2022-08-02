import requests
import os
import json
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from Database import *

# TODO make sure to hide later using bash method 
# os.environ.get('SPOTIFY_CLIENT_ID')
# os.environ.get('SPOTIFY_CLIENT_SECRET')



SPOTIPY_CLIENT_ID = '9e12f520e41e4f1c8e2c201dd31d6cc5'
SPOTIPY_CLIENT_SECRET = 'e19db685409940e68d894ed1b8fee1eb'


auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)


class spotifyPlaylist:
    def __init__(self):
        self.playlist_url = None
        self.playlist_name = None
        self.playlist_image = None
        self.number_of_songs = 0
        self.song_list = []
        self.artists_list = []
        self.album_list = []
        

    def get_playlist(self, url):
        self.playlist_url = url
        playlist_dict = sp.playlist(self.playlist_url)
        self.playlist_name = playlist_dict['name']
        self.playlist_image = sp.playlist_cover_image(self.playlist_url)
        self.number_of_songs = playlist_dict["tracks"]["total"]

        tracks = playlist_dict["tracks"]
        items = tracks["items"]
        offset=0
        i=0

        while i<self.number_of_songs:
            song = items[i-offset]["track"]["name"]
            album = items[i-offset]["track"]["album"]["name"]
            artists = [k["name"] for k in items[i-offset]["track"]["artists"]]
            artists = ','.join(artists)
            self.album_list.append(album)
            self.song_list.append(song)
            self.artists_list.append(artists)
            if (i+1)%100 == 0:
                tracks = sp.next(tracks)
                items = tracks["items"]
                offset = i+1
            i+=1


def main():
    x = spotifyPlaylist()
    x.get_playlist('https://open.spotify.com/playlist/1n4hHMWVTtXLTNiDC09JXg?si=b78a86aa7fce47d2')
    print(x.playlist_name)

    
if __name__ == "__main__":
    main()