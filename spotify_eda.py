import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('spotify_clean.csv')

# Set style
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Chart 1 — Top 10 Genres by Avg Popularity
top_genres = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False).head(10)
plt.figure()
sns.barplot(x=top_genres.values, y=top_genres.index, palette='Greens_r')
plt.title('Top 10 Genres by Average Popularity', fontsize=14)
plt.xlabel('Average Popularity')
plt.tight_layout()
plt.savefig('chart1_top_genres.png')
plt.show()
print("Chart 1 saved!")

# Chart 2 — Energy vs Danceability
plt.figure()
sns.scatterplot(data=df.sample(2000), x='energy', y='danceability',
                hue='popularity', palette='Greens', alpha=0.6)
plt.title('Energy vs Danceability', fontsize=14)
plt.tight_layout()
plt.savefig('chart2_energy_dance.png')
plt.show()
print("Chart 2 saved!")

# Chart 3 — Popularity Distribution
plt.figure()
sns.histplot(df['popularity'], bins=50, color='#1DB954')
plt.title('Popularity Distribution', fontsize=14)
plt.xlabel('Popularity Score')
plt.tight_layout()
plt.savefig('chart3_popularity_dist.png')
plt.show()
print("Chart 3 saved!")

# Chart 4 — Top 10 Artists by Track Count
top_artists = df.groupby('artists')['track_name'].count().sort_values(ascending=False).head(10)
plt.figure()
sns.barplot(x=top_artists.values, y=top_artists.index, palette='Greens_r')
plt.title('Top 10 Artists by Track Count', fontsize=14)
plt.xlabel('Number of Tracks')
plt.tight_layout()
plt.savefig('chart4_top_artists.png')
plt.show()
print("Chart 4 saved!")

print("\nAll charts saved!")