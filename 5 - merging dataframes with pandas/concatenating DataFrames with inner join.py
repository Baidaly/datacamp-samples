'''
Here, you'll continue working with DataFrames compiled from The Guardian's Olympic medal dataset.

The DataFrames bronze, silver, and gold have been pre-loaded for you.

Your task is to compute an inner join.
'''
# Create the list of DataFrames: medal_list
medal_list = [bronze, silver, gold]

# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list, keys=['bronze', 'silver', 'gold'], axis=1, join='inner')

# Print medals
print(medals)
