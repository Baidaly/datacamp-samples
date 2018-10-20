'''
Load Data from a list into the Table

Using the multiple insert pattern, in this exercise, you will load the data from values_list into the table.
'''
# Import insert
from sqlalchemy import insert

# Build insert statement: stmt
stmt = insert(census)

# Use values_list to insert data: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)
