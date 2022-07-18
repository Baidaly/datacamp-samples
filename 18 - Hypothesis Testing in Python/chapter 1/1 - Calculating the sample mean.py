'''
The late_shipments dataset contains supply chain data on the delivery of medical supplies. Each row represents one delivery of a part. The late columns denotes whether or not the part was delivered late. A value of "Yes" means that the part was delivered late, and a value of "No" means the part was delivered on time.

Let's begin our analysis by calculating a point estimate (or sample statistic), namely the proportion of late shipments.

late_shipments is available, and pandas is loaded as pd.
'''
# Print the late_shipments dataset
print(late_shipments)

# Calculate the proportion of late shipments
late_prop_samp = late_shipments["late"].value_counts()["Yes"] / len(late_shipments)

# Print the results
print(late_prop_samp)