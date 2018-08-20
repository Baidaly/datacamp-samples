'''
Sometimes, all you need is some key-value pairs, and the context does not matter. 
If said context is in the index, you can easily obtain what you want. 
For example, in the users DataFrame, the visitors and signups columns lend themselves well to being represented as key-value pairs. 
So if you created a hierarchical index with 'city' and 'weekday' columns as the index, you can easily extract key-value pairs for the 'visitors' and 'signups' columns by melting users and specifying col_level=0.
'''
# Set the new index: users_idx
users_idx = users.set_index(['city', 'weekday'])

# Print the users_idx DataFrame
print(users_idx)

# Obtain the key-value pairs: kv_pairs
kv_pairs = users_idx.melt(col_level=0)

# Print the key-value pairs
print(kv_pairs)