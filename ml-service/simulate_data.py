import pandas as pd
import numpy as np
import random

def simulate_waste_bin_data(num_bins=100):
    data = {
        'bin_id': range(1, num_bins + 1),
        'location_lat': np.random.uniform(40.0, 41.0, num_bins),
        'location_lon': np.random.uniform(-74.0, -73.0, num_bins),
        'fill_level': np.random.randint(0, 101, num_bins),  # 0 to 100% fill level
        'temperature': np.random.uniform(15, 35, num_bins), # in Celsius
        'last_collected': pd.date_range(start='2023-01-01', periods=num_bins).tolist()
    }
    df = pd.DataFrame(data)
    return df

if __name__ == '__main__':
    num_bins = 100  # Number of bins to simulate
    df = simulate_waste_bin_data(num_bins)
    # Save to a CSV file
    df.to_csv('simulated_waste_bins.csv', index=False)
    print(f"Simulated data for {num_bins} bins saved to 'simulated_waste_bins.csv'.")
