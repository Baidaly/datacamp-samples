'''
You can move multiple columns into a single column (making the data long and skinny) by "melting" multiple columns. In this exercise, you will practice doing this.

The users DataFrame has been pre-loaded for you. As always, explore it in the IPython Shell and note the index.
'''
# Melt users: skinny
skinny = pd.melt(users, id_vars=['weekday', 'city'], value_vars=['visitors', 'signups'])

# Print skinny
print(skinny)

'''
users

  weekday    city  visitors  signups
0     Sun  Austin       139        7
1     Sun  Dallas       237       12
2     Mon  Austin       326        3
3     Mon  Dallas       456        5
'''