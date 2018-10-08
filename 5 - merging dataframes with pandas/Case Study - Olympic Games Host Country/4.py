'''
Counting medals by country/edition in a pivot table

Here, you'll start with the concatenated DataFrame medals from the previous exercise.

You can construct a pivot table to see the number of medals each country won in each year. The result is a new DataFrame with the Olympic edition on the Index and with 138 country NOC codes as columns. If you want a refresher on pivot tables, it may be useful to refer back to the relevant exercises in Manipulating DataFrames with pandas.
'''
# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(aggfunc='count', index='Edition', values='Athlete', columns='NOC')

# Print the first & last 5 rows of medal_counts
print(medal_counts.head())
print(medal_counts.tail())