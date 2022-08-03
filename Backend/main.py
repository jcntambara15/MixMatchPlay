from Spotify import spotifyPlaylist 
from Database import * 
from appleclient import *


# SPOTIPY_CLIENT_ID = '9e12f520e41e4f1c8e2c201dd31d6cc5'
# SPOTIPY_CLIENT_SECRET = 'e19db685409940e68d894ed1b8fee1eb'


# auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET)
# sp = spotipy.Spotify(auth_manager=auth_manager)


def main():
    x = spotifyPlaylist()
    x.get_playlist('https://open.spotify.com/playlist/1n4hHMWVTtXLTNiDC09JXg?si=b78a86aa7fce47d2')
    print(x.playlist_name)
    z = Apple_music_client(x)
    for i in x.number_of_songs:
        search_for_song(x.playlist_name+x.)

playlist_name1 = 'Hidden gems'
appl1 = 'https://music.apple.com/us/playlist/hidden-gems/pl.u-GgA5e7RhxYlR1d'
spotify1 = 'https://open.spotify.com/playlist/7x44ySCq6r8VE7JwRzRkzb'

playlist_name2 = 'lofi hip hop music - beats to relax/study to'
playlist_2 ='https://open.spotify.com/playlist/6FDmloGsp24kRk0Kx6nBvE'
apple_2='https://music.apple.com/us/playlist/lofi-hip-hop-music-beats-to-relax-study-to/pl.u-2aoq8mqiGo7J6A0'


if __name__ == "__main__":
    main()