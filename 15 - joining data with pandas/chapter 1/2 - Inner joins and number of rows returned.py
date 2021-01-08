'''
All of the merges you have studied to this point are called inner joins. It is necessary to understand that inner joins only return the rows with matching values in both tables. You will explore this further by reviewing the merge shown in the video lesson between the wards and census tables. You will alter the tables and examine how this affects the merge between them. The wards and census tables have been loaded for you.

For this exercise, it is important to know that both tables start with 50 rows, and are reset back to their original values after each Step.
'''
# Change '1' to None in `ward` col
census.loc[census['ward'] == '1', 'ward'] = None

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print(wards_census.shape)