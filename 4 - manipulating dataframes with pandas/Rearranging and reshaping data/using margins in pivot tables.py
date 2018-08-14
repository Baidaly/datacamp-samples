'''
Sometimes it's useful to add totals in the margins of a pivot table. You can do this with the argument margins=True. 
In this exercise, you will practice using margins in a pivot table along with a new aggregation function: sum.

The users DataFrame, which you are now probably very familiar with, has been pre-loaded for you.
'''
# Create the DataFrame with the appropriate pivot table: signups_and_visitors
signups_and_visitors = users.pivot_table(index='weekday',
                                         values=['signups', 'visitors'],
                                         aggfunc=sum)

# Print signups_and_visitors
print(signups_and_visitors)

# Add in the margins: signups_and_visitors_total 
signups_and_visitors_total = users.pivot_table(index='weekday',
                                               values=['signups', 'visitors'],
                                               aggfunc=sum,
                                               margins=True)

# Print signups_and_visitors_total
print(signups_and_visitors_total)
