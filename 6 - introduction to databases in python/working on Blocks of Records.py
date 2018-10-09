'''
Fantastic work so far! As Jason discussed in the video, sometimes you may have the need to work on a large ResultProxy, and you may not have the memory to load all the results at once. To work around that issue, you can get blocks of rows from the ResultProxy by using the .fetchmany() method inside a loop. With .fetchmany(), give it an argument of the number of records you want. When you reach an empty list, there are no more rows left to fetch, and you have processed all the results of the query. Then you need to use the .close() method to close out the connection to the database.

You'll now have the chance to practice this on a large ResultProxy called results_proxy that has been pre-loaded for you to work with.
'''
# Start a while loop checking for more results
while more_results:
    # Fetch the first 50 results from the ResultProxy: partial_results
    partial_results = results_proxy.fetchmany(50)

    # if empty list, set more_results to False
    if partial_results == []:
        more_results = False

    # Loop over the fetched records and increment the count for the state
    for row in partial_results:
        if row.state in state_count:
            state_count[row.state] += 1;
        else:
            state_count[row.state] = 1;

# Close the ResultProxy, and thus the connection
results_proxy.close()

# Print the count by state
print(state_count)
