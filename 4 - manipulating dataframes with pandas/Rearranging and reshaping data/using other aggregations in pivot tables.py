'''
You can also use aggregation functions within a pivot table by specifying the aggfunc parameter. 
In this exercise, you will practice using the 'count' and len aggregation functions - which produce the same result - on the users DataFrame.
'''
# Use a pivot table to display the count of each column: count_by_weekday1
count_by_weekday1 = users.pivot_table(index='weekday',
                                      values=['city','visitors', 'signups'],
                                      aggfunc='count')

# Print count_by_weekday
print(count_by_weekday1)

# Replace 'aggfunc='count'' with 'aggfunc=len': count_by_weekday2
count_by_weekday2 = users.pivot_table(index='weekday',
                                      values=['city','visitors', 'signups'],
                                      aggfunc=len)


# Verify that the same result is obtained
print('==========================================')
print(count_by_weekday1.equals(count_by_weekday2))
