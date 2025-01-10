from flask import Flask, request, jsonify
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib

app = Flask(__name__)

# Load the pre-trained K-Means model and the scaler
kmeans_model_path = 'models/kmeans_fill_level_model.pkl'
scaler_path = 'models/scaler.pkl'
kmeans = joblib.load(kmeans_model_path)
scaler = joblib.load(scaler_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Example input: {'features': [[0.1, 0.2, 0.3, ..., 0.0], [0.4, 0.5, 0.6, ..., 0.0]]}
    features = np.array(data['features'])
    
    # Standardize the input features
    features_scaled = scaler.transform(features)
    
    # Make predictions
    prediction = kmeans.predict(features_scaled)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)