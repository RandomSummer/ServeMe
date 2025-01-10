import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the simulated data
data = pd.read_csv('simulated_waste_bins.csv')

# Display basic statistics
print(data.describe())

# Visualize the distribution of fill levels
sns.histplot(data['fill_level'], bins=20, kde=True)
plt.title('Distribution of Bin Fill Levels')
plt.xlabel('Fill Level (%)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of bin locations colored by fill level
plt.scatter(data['location_lat'], data['location_lon'], c=data['fill_level'], cmap='viridis', s=50)
plt.colorbar(label='Fill Level (%)')
plt.title('Bin Locations with Fill Levels')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()
