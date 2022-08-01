from Spotify import spotifyPlaylist 
from Database import * 


# SPOTIPY_CLIENT_ID = '9e12f520e41e4f1c8e2c201dd31d6cc5'
# SPOTIPY_CLIENT_SECRET = 'e19db685409940e68d894ed1b8fee1eb'


# auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET)
# sp = spotipy.Spotify(auth_manager=auth_manager)


def main():
    x = spotifyPlaylist()
    x.get_playlist('https://open.spotify.com/playlist/1n4hHMWVTtXLTNiDC09JXg?si=b78a86aa7fce47d2')
    print(x.playlist_name)
    add_spotify_playlist(x)



if __name__ == "__main__":
    main()