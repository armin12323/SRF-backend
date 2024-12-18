import pandas as pd

ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
movies = pd.read_csv('ml-100k/u.item', sep='|', encoding='latin-1', names=['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_url', 'genres'])

movie_data = pd.merge(ratings, movies[['movie_id', 'title']], on='movie_id')

print(movie_data.head())