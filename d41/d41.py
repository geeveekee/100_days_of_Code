from datetime import time
from bs4.builder import TreeBuilder
from requests.exceptions import ReadTimeout
from requests.models import ReadTimeoutError
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from icecream import ic
import sys
import os
import time
import webbrowser

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="",
        client_secret="",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
display_name = sp.current_user()["display_name"]

def check_if_song_in_album(song, artist_album_list_of_id, artist_album_list, artist_complete_id_list):
    count = -1
    for id in artist_album_list_of_id:
        count += 1 
        try: 
            check_against = [x['name'] for x in sp.album_tracks(id)['items']]
            if song in check_against:
                album_name = artist_album_list[count]
                album_id = artist_album_list_of_id[count]
                song_id = artist_complete_id_list[count]
                return album_name, album_id, song_id
        except ReadTimeoutError:
            print("Wait up!")
        except ReadTimeout:
            pass
        except ConnectionError:
            pass
        
    return False

def search_for_song(artist_complete_song_list, artist_album_list_of_id, artist_album_list, artist_complete_id_list):
    find_album = int(input("Enter the number of the song you wish to find out the album of: "))
    song_name_input = artist_complete_song_list[find_album-1]
    song_in_which_album, song_in_which_album_id, song_id = check_if_song_in_album(song_name_input, artist_album_list_of_id, artist_album_list, artist_complete_id_list)

    try:
        album_cover_img = sp.album(song_in_which_album_id)['images'][0]['url']
    except ReadTimeoutError:
        pass
    except ReadTimeout:
        pass

    webbrowser.open(album_cover_img)
    #song_id = [song_id]
    #sp.start_playback(device_id=user_id, uris=song_id)
    user_continue = input("Would you like to search for another song of the same artist?(y/n): ")
    if user_continue == 'y':
        search_for_song(artist_complete_song_list, artist_album_list_of_id, artist_album_list, artist_complete_id_list)
    else:
        return 



def about_artist(artist_data):
    artist_name = artist_data['name']
    artist_genres = artist_data['genres']
    artist_followers = artist_data['followers']['total']
    artist_image = artist_data['images'][0]['url']
    artist_id = artist_data['id']
    temp_list_albums = sp.artist_albums(artist_id=artist_id)['items']
    artist_album_list = [x['name'] for x in temp_list_albums]
    artist_album_list_of_id = [x['id'] for x in temp_list_albums]
    album_id_list = [x['id'] for x in temp_list_albums]
    print(f"""
Name: {artist_name}\n
Genres: {artist_genres}\n
Followers: {artist_followers}\n
Image: {artist_image}\n
Albums: {artist_album_list}
List of songs: 
    """)
    count = 0

    artist_complete_song_list = []
    artist_complete_id_list = []
    for album in album_id_list:
        try:
            temp_list_songs_in_album = sp.album_tracks(album_id=album)['items']
            for x in temp_list_songs_in_album:
                count +=1
                
                song_name = x['name']
                song_id = x['uri']
                print(f"{count}. {song_name}")
                artist_complete_song_list.append(song_name)
                artist_complete_id_list.append(song_id)
        except ReadTimeoutError:
            print("Hold your horses!")

        except ConnectionError:
            print('blje')

        except ReadTimeout:
            pass

    search_for_song(artist_complete_song_list, artist_album_list_of_id, artist_album_list, artist_complete_id_list)


game_over = False
while not game_over:
    print(f"Hi! {display_name}, welcome to Spotify!")
    user_choice = int(input(f"0-Search for an artist\n1-Exit\n\n"))
    if user_choice == 0:
        artist_name = input("Please enter name of the Artist: ")
        query = f"artist:{artist_name}"
        try:
            artist_data = sp.search(q=query, type='artist')['artists']['items'][0]
        except ReadTimeoutError:
            print("Hold you horses")
        
        about_artist(artist_data)



    elif user_choice ==1:
        game_over = True
        sys.exit()
    else:
        print("Please enter a valid number")
        time.sleep(2)
        os.system('cls||clear')




