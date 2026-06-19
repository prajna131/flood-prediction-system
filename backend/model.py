import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("../dataset/real_time_flood_data.csv")

# Encode categorical columns (Rainfall Range)
label_encoders = {"Rainfall_Range_mm": LabelEncoder()}
df["Rainfall_Range_mm"] = label_encoders["Rainfall_Range_mm"].fit_transform(df["Rainfall_Range_mm"])

# Split features and target
X = df.drop(columns=['Flood_Probability'])
y = df['Flood_Probability']

# Standardize numerical data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model, scaler, and label encoders
joblib.dump(model, "../backend/flood_model.pkl")
joblib.dump(scaler, "../backend/scaler.pkl")
joblib.dump(label_encoders, "../backend/label_encoders.pkl")

print("Model trained for real-time flood prediction!")