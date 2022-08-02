import requests
import os
import json

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# os.environ.get('SPOTIFY_CLIENT_ID')
# os.environ.get('SPOTIFY_CLIENT_SECRET')

SPOTIPY_CLIENT_ID = '0156ece3cac04e1799360e844a97d7c3'
SPOTIPY_CLIENT_SECRET = '6580b204f28d46a8b58e6e4644141fd7'

auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)



# AUTH_URL = 'https://accounts.spotify.com/api/token'

# auth_response = requests.post(AUTH_URL, {
#     'grant_type': 'client_credentials',
#     'client_id': CLIENT_ID,
#     'client_secret': CLIENT_SECRET,
# })

# auth_response_data = auth_response.json()

# access_token = auth_response_data['access_token']

# headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

# BASE_URL = 'https://api.spotify.com/v1/'

album_list = []
song_list = []
artists_list = []
release_date_list = []
    
def get_playlist(playlist_url):
    playlist_dict = sp.playlist(playlist_url)
    playlist_image = sp.playlist_cover_image(playlist_url)
    no_of_songs = playlist_dict["tracks"]["total"]
    # album_list = []
    # song_list = []
    # artists_list = []
    # release_date_list = []
    tracks = playlist_dict["tracks"]
    items = tracks["items"]
    offset=0
    i=0
    while i<no_of_songs:
        song = items[i-offset]["track"]["name"]
        album = items[i-offset]["track"]["album"]["name"]
        release_date = items[i-offset]["track"]["album"]["release_date"]
        artists = [k["name"] for k in items[i-offset]["track"]["artists"]]
        artists = ','.join(artists)
        album_list.append(album)
        song_list.append(song)
        release_date_list.append(release_date)
        artists_list.append(artists)
        if (i+1)%100 == 0:
            tracks = sp.next(tracks)
            items = tracks["items"]
            offset = i+1
        i+=1

def main():
    get_playlist('https://open.spotify.com/playlist/37i9dQZF1DX4SrOBCjlfVi')
    print(album_list)

if __name__ == "__main__":
    main()