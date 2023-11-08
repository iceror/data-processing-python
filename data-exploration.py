import pandas as pd
import json

df = pd.read_csv('./spotify_songs.csv')

mask_genre = df['playlist_genre'] == 'pop'

filtered_genre = df[mask_genre]

unique_genre = df['playlist_genre'].unique()

for genre in unique_genre:
  print(genre)

# get most popular song
# get most danceable songs
# get most energy songs
# get songs with higher and lower tempos
# get shorter and longer songs
# get num of songs by x artist
# get num of songs from x year
# percentage of playlists genre from all playlists genres
# most popular key (values from 0-11 C-B )