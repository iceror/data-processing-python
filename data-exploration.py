import pandas as pd
import json

df = pd.read_csv('./spotify_songs.csv')
# print(df)
mask_genre = df['playlist_genre'] == 'pop'
filtered_genre = df[mask_genre]

unique_genres = df['playlist_genre'].unique()

# for genre in unique_genres:
#   print(genre)

# function to get tops 
top_songs = df.sort_values(by='track_popularity', ascending=False)[['track_popularity', 'track_name', 'track_artist']]
most_danceable_songs = df.sort_values(by='danceability', ascending=False)[[ 'danceability', 'track_name', 'track_artist']]
most_energetic_songs = df.sort_values(by='energy', ascending=False)[['energy', 'track_name', 'track_artist']]

def get_top_songs(data):
  tops = data.drop_duplicates(subset='track_name', keep='last')
  tops = tops.head(10)
  # print(tops)
  return tops

top_songs = get_top_songs(top_songs)
most_danceable_songs = get_top_songs(most_danceable_songs)
most_energetic_songs = get_top_songs(most_energetic_songs)

print(most_energetic_songs)

# get songs with higher and lower tempos
# get shorter and longer songs
# get num of songs by x artist
# get num of songs from x year
def get_songs_by_year(data, year):
  # return songs from the given year
  return

# percentage of playlists genre from all playlists genres
# most popular key (values from 0-11 C-B )