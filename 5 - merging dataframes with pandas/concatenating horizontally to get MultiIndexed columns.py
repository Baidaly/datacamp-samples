'''
It is also possible to construct a DataFrame with hierarchically indexed columns. For this exercise, you'll start with pandas imported and a list of three DataFrames called dataframes. All three DataFrames contain 'Company', 'Product', and 'Units' columns with a 'Date' column as the index pertaining to sales transactions during the month of February, 2015. The first DataFrame describes Hardware transactions, the second describes Software transactions, and the third, Service transactions.

Your task is to concatenate the DataFrames horizontally and to create a MultiIndex on the columns. From there, you can summarize the resulting DataFrame and slice some information from it.
'''
# Concatenate dataframes: february
february = pd.concat(dataframes, axis=1, keys=['Hardware', 'Software', 'Service'])

# Print february.info()
print(february.info())

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
slice_2_8 = february.loc['Feb. 2, 2015':'Feb. 8, 2015', idx[:, 'Company']]

# Print slice_2_8
print(slice_2_8)
