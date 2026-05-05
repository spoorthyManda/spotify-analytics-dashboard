import pandas as pd
import sqlite3

# Load clean data
df = pd.read_csv('spotify_clean.csv')

# Create SQLite database
conn = sqlite3.connect('spotify.db')

# Save dataframe to SQL table
df.to_sql('spotify_tracks', conn, if_exists='replace', index=False)
print("Data loaded into SQLite!")

# Query 1 — Top 10 most popular tracks
print("\nTop 10 Most Popular Tracks:")
query1 = pd.read_sql_query("""
    SELECT track_name, artists, track_genre, popularity
    FROM spotify_tracks
    ORDER BY popularity DESC
    LIMIT 10
""", conn)
print(query1)

# Query 2 — Top 10 genres by average popularity
print("\nTop 10 Genres by Avg Popularity:")
query2 = pd.read_sql_query("""
    SELECT track_genre,
           ROUND(AVG(popularity), 2) AS avg_popularity,
           COUNT(*) AS total_tracks
    FROM spotify_tracks
    GROUP BY track_genre
    ORDER BY avg_popularity DESC
    LIMIT 10
""", conn)
print(query2)

# Query 3 — Top 10 artists by track count
print("\nTop 10 Artists by Track Count:")
query3 = pd.read_sql_query("""
    SELECT artists,
           COUNT(*) AS total_tracks,
           ROUND(AVG(popularity), 2) AS avg_popularity
    FROM spotify_tracks
    GROUP BY artists
    ORDER BY total_tracks DESC
    LIMIT 10
""", conn)
print(query3)

# Query 4 — Average audio features
print("\nAverage Audio Features:")
query4 = pd.read_sql_query("""
    SELECT
        ROUND(AVG(danceability), 3) AS avg_danceability,
        ROUND(AVG(energy), 3) AS avg_energy,
        ROUND(AVG(valence), 3) AS avg_valence,
        ROUND(AVG(tempo), 2) AS avg_tempo,
        ROUND(AVG(popularity), 2) AS avg_popularity
    FROM spotify_tracks
""", conn)
print(query4)

conn.close()
print("\nAll SQL queries complete!")

exit()
