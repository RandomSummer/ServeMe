import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib
import matplotlib.pyplot as plt

# Load the data
print("Loading data...")
data = pd.read_csv('../simulated_waste_bins.csv')

# Extract relevant features: Fill level trends over time
print("Processing fill level trends...")
trend_data = data.groupby('bin_id')['fill_level'].apply(list).reset_index()

# Pad fill levels to the same length (if necessary) for K-Means
print("Padding fill levels to equal length...")
max_length = trend_data['fill_level'].apply(len).max()
trend_data['fill_level'] = trend_data['fill_level'].apply(
    lambda x: x + [0] * (max_length - len(x))
)

# Convert fill level trends to a numpy array
X = np.array(trend_data['fill_level'].tolist())
print(f"Data shape after processing: {X.shape}")

# Standardize the data (important for clustering algorithms)
print("Standardizing data...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save the scaler
joblib.dump(scaler, '../models/scaler.pkl')
print("Scaler saved successfully.")

# Determine optimal number of clusters using the Elbow Method
print("Determining the optimal number of clusters...")
inertia = []
for k in range(1, 11):
    print(f"Training KMeans for k={k}...")
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
    print(f"Inertia for k={k}: {kmeans.inertia_}")

# Plot the Elbow Method graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal Clusters (Fill Level Trends)')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.grid(True)
plt.show()

# Based on the Elbow Method, choose an optimal k (e.g., k=3)
optimal_k = 3
print(f"Training final KMeans model with k={optimal_k}...")
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(X_scaled)
print("Final KMeans model trained successfully.")

# Save the K-Means model
joblib.dump(kmeans, '../models/kmeans_fill_level_model.pkl')
print("KMeans model saved successfully.")

# Add cluster labels to the original data
trend_data['cluster'] = kmeans.labels_

# Save clustered data for further use
trend_data.to_csv('../data/clustered_fill_level_data.csv', index=False)
print("Clustered data saved successfully.")

# Visualize the clustered data
print("Visualizing clustered data...")
plt.figure(figsize=(8, 5))
for cluster in range(optimal_k):
    cluster_data = X_scaled[kmeans.labels_ == cluster]
    plt.scatter(cluster_data[:, 0], np.zeros_like(cluster_data[:, 0]), label=f'Cluster {cluster}')
plt.title('Clustered Data Visualization')
plt.xlabel('Feature 1')
plt.ylabel('Cluster')
plt.legend()
plt.grid(True)
plt.show()

print(f'K-Means clustering on fill level trends completed. Data saved with cluster labels.')
