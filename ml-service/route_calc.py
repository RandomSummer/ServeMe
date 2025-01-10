import pandas as pd
from geopy.distance import geodesic
import numpy as np

# Load bin data
print("Loading simulated bin data...")
bin_data = pd.read_csv('./simulated_waste_bins.csv')

# Ensure the dataset has the required columns: bin_id, latitude, longitude
# Check and rename columns if necessary
print("Processing bin data for required columns...")
bin_data = bin_data[['bin_id', 'location_lat', 'location_lon']]

# Load clustered fill level data
print("Loading clustered fill level data...")
clustered_data = pd.read_csv('./data/clustered_fill_level_data.csv')

# Merge the two datasets on bin_id
print("Merging bin data with clustered data...")
merged_data = pd.merge(clustered_data, bin_data, on='bin_id')

# Function to calculate distance between two points
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

# Calculate distance matrix
print("Calculating distance matrix...")
distance_matrix = []
for i in range(len(merged_data)):
    distances = []
    for j in range(len(merged_data)):
        coord1 = (merged_data.iloc[i]['location_lat'], merged_data.iloc[i]['location_lon'])
        coord2 = (merged_data.iloc[j]['location_lat'], merged_data.iloc[j]['location_lon'])
        distances.append(calculate_distance(coord1, coord2))
    distance_matrix.append(distances)

print("Distance matrix calculated successfully.")

np.save('./data/distance_matrix.npy', distance_matrix)
print("Distance matrix saved successfully.")
