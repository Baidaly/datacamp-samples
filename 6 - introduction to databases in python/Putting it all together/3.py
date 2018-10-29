'''
Reading the Data from the CSV

Leverage the Python CSV module from the standard library and load the data into a list of dictionaries.

It may help to refer back to the Chapter 4 exercise in which you did something similar.
'''
# Create an empty list: values_list
values_list = []

# Iterate over the rows
for row in csv_reader:
    # Create a dictionary with the values
    data = {'state': row[0], 'sex': row[1], 'age':row[2], 'pop2000': row[3],
            'pop2008': row[4]}
    # Append the dictionary to the values list
    values_list.append(data)