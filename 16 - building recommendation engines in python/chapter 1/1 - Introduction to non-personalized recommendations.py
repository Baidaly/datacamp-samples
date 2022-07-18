'''
One of the most basic ways to make recommendations is to go with the knowledge of the crowd and recommend what is already the most popular. In this exercise, you will calculate how often each movie in the dataset has been watched and find the most frequently watched movies.

The DataFrame user_ratings_df, which is a subset of the Movie Lens dataset, has been loaded for you. This table contains identifiers for each movie and the user who watched it, along with the rating they gave it.
'''
movie_watch_counts = user_ratings_df["title"].value_counts()

print(movie_watch_counts.head())