# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot the histogram
# There are extremely large differences between the min and max values, so we need to use logx and logy
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()
