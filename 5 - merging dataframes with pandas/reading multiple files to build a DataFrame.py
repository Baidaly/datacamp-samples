'''
It is often convenient to build a large DataFrame by parsing many files as DataFrames and concatenating them all at once. You'll do this here with three files, but, in principle, this approach can be used to combine data from dozens or hundreds of files.

Here, you'll work with DataFrames compiled from The Guardian's Olympic medal dataset.

pandas has been imported as pd and two lists have been pre-loaded: An empty list called medals, and medal_types, which contains the strings 'bronze', 'silver', and 'gold'.
'''
medals = []
medal_types = ['bronze', 'silver', 'gold']

for medal in medal_types:

    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal
    
    # Create list of column names: columns
    columns = ['Country', medal]
    
    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv(file_name, header=0, index_col='Country', names=columns)

    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals
medals = pd.concat(medals, axis='columns')

# Print medals
print(medals)