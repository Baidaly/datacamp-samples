'''
Now that you have found the most commonly paired movies, you can make your first recommendations!

While you are not taking in any information about the person watching, and do not even know any details about the movie, valuable recommendations can still be made by examining what groups of movies are watched by the same people. In this exercise, you will examine the movies often watched by the same people that watched Thor, and then use this data to give a recommendation to someone who just watched the movie. The DataFrame you generated in the last lesson, combination_counts_df, that contains counts of how often movies are watched together has been loaded for you.
'''
import matplotlib.pyplot as plt

# Sort the counts from highest to lowest
combination_counts_df.sort_values('size', ascending=False, inplace=True)

# Find the movies most frequently watched by people who watched Thor
thor_df = combination_counts_df[combination_counts_df['movie_a'] == 'Thor']

# Plot the results
thor_df.plot.bar(x="movie_b")
plt.show()