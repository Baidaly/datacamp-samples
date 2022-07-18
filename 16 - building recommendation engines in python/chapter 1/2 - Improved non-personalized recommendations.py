'''
Just because a movie has been watched by a lot of people doesn't necessarily mean viewers enjoyed it. To understand how a viewer actually felt about a movie, more explicit data is useful. Thankfully, you also have ratings from each of the viewers in the Movie Lens dataset.

In this exercise, you will find the average rating of each movie in the dataset, and then find the movie with the highest average rating.

You will use the same user_ratings_df as you used in the previous exercise, which has been loaded for you.
'''
# Find the mean of the ratings given to each title
average_rating_df = user_ratings_df[["title", "rating"]].groupby('title').mean()

# Order the entries by highest average rating to lowest
sorted_average_ratings = average_rating_df.sort_values(ascending=False, by="rating")

# Inspect the top movies
print(sorted_average_ratings.head())