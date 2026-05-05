import pandas as pd
import numpy as np 

df = pd.read_csv(r'C:\Users\spoor\Downloads\archive (1).zip') #read data

df = df.drop_duplicates()#remove duplicate
print(f"after removing duplicates", df.shape)

df = df.dropna(subset=['artists', 'album_name', 'track_name'])#drop missing values

df = df.drop(columns=['Unnamed: 0'])#drop unneccesary columns 

df['duration_min'] = (df['duration_ms'] / 6000).round(2) #conversion to min
df = df.drop(columns = ['duration_ms'])

df = df[df['popularity']>0] #Filter out tracks with 0 popularity
print("After filtering 0 popularity:", df.shape)

df = df.reset_index(drop=True)

df.to_csv('spotify_clean.csv', index = False)
print("\n clean dataset saved!")
print("Final Shape:", df.shape)
print("\ncolumns:", df.columns.tolist())



