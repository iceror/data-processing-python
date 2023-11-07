import pandas as pd
import json

df = pd.read_csv('./spotify_songs.csv')

mask = df['track_artist'] == 'Maroon 5'
mask_genre = df['playlist_genre'] == 'rock'

filtered_df = df[mask]
filtered_genre = df[mask_genre]
print(filtered_genre)
#print(df['playlist_genre'])
