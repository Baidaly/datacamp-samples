'''
To better understand DataFrame objects, it's useful to know that they consist of three components, stored as attributes:

    .values: A two-dimensional NumPy array of values.
    .columns: An index of columns: the column names.
    .index: An index for the rows: either row numbers or row names.

You can usually think of indexes as being like a list of strings or numbers, though the pandas Index data type allows for more sophisticated options. (These will be covered later in the course.)
'''
# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)