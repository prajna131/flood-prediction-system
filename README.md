# Flood Risk Prediction System using Machine Learning

## Project Overview

This project is a Machine Learning-powered Flood Risk Prediction System developed using Python, Scikit-Learn, and Flask. The application predicts flood risk levels based on multiple environmental and geographical factors such as rainfall, river flow, soil moisture, humidity, temperature, drainage capacity, urbanization, and deforestation.

The system provides an interactive web interface where users can enter environmental parameters and receive real-time flood risk predictions.

---

## Why I Built This

Floods are among the most common natural disasters and often result from the interaction of multiple environmental factors. I built this project to understand how Machine Learning can be used to analyze these factors and predict flood risk more effectively than traditional rule-based approaches.

This project helped me gain hands-on experience with the complete Machine Learning lifecycle including data preprocessing, feature engineering, model training, model deployment, and real-time prediction through a web application.

---

## Problem Statement

Flood prediction depends on several interconnected factors:

- Rainfall intensity
- Number of rainy days
- River flow
- Soil moisture
- Humidity
- Temperature
- Drainage capacity
- Urbanization level
- Deforestation level

Analyzing these variables manually can be difficult. This system uses Machine Learning to identify patterns and estimate flood risk levels based on environmental conditions.

---

## Features

- Real-time flood risk prediction
- User-friendly web interface
- Automatic data preprocessing
- Label encoding for categorical features
- Feature scaling using trained scaler
- Machine Learning-based prediction engine
- Risk categorization into:
  - Low Risk
  - Medium Risk
  - High Risk
- Flask-based deployment

---

## Technologies Used

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Joblib

### Backend

- Python
- Flask

### Frontend

- HTML
- CSS

---

## System Workflow

### Step 1

User enters environmental parameters:

- Rainfall Range
- Number of Rainy Days
- River Flow
- Soil Moisture
- Humidity
- Temperature
- Drainage Capacity
- Urbanization Index
- Deforestation Index

### Step 2

Categorical values are converted into numerical format using trained Label Encoders.

### Step 3

Input features are standardized using a saved Scaler.

### Step 4

The trained Machine Learning model processes the transformed input.

### Step 5

The model generates a flood risk score.

### Step 6

The prediction score is classified into:

- Low Risk
- Medium Risk
- High Risk

### Step 7

The result is displayed to the user through the web interface.

---

## Screenshots

Home Page

<img width="1918" height="1087" alt="image" src="https://github.com/user-attachments/assets/2a289895-e4c1-4f52-9ea2-005a1784d53d" />

Prediction Example

<img width="1918" height="1087" alt="image" src="https://github.com/user-attachments/assets/c630023e-49ca-4c4b-bcda-b02bf7df72a1" />

---
## Challenges Faced

### Maintaining Preprocessing Consistency

One of the key challenges was ensuring that the same preprocessing steps used during training were applied during prediction.

To solve this problem:

- Label Encoders were saved and reused
- Scaler was saved and reused
- Prediction pipeline was aligned with training pipeline

### Handling Invalid User Inputs

Users may provide unexpected or invalid values. Additional validation logic was implemented to ensure reliable predictions.

### Model Deployment

Integrating the trained model, scaler, and encoders into a Flask application required careful handling to maintain prediction accuracy and consistency.

---

## What Surprised Me

The most interesting insight from this project was that flood risk is not determined by rainfall alone.

For example:

- High rainfall does not always result in flooding.
- Poor drainage capacity significantly increases risk.
- Soil moisture and river flow strongly influence flood likelihood.

This demonstrated the importance of considering multiple environmental variables simultaneously when building predictive systems.

---

## Project Structure

```text
Flood-Prediction-System/

├── backend/
│   ├── app.py
│   ├── model.py
│   ├── flood_model.pkl
│   ├── scaler.pkl
│   └── label_encoders.pkl
│
├── frontend/
│   ├── index.html
│   ├── result.html
│   └── style.css
│
├── dataset/
│   ├── real_time_flood_data.csv
│   └── real_time_flood_data_updated.csv
│
├── screenshots/
│   ├── homepage.png
│   └── prediction.png
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/prajna131/flood-prediction-system.git
```

### Navigate to Project Directory

```bash
cd flood-prediction-system
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python backend/app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Application Screenshots

### Home Page

(Add homepage screenshot here)

### Prediction Result

(Add prediction screenshot here)

---

## Key Learnings

Through this project, I gained practical experience in:

- Machine Learning model development
- Feature engineering
- Data preprocessing
- Label encoding
- Feature scaling
- Model serialization using Joblib
- Flask web development
- Real-time prediction systems
- End-to-end Machine Learning deployment

---

## Future Enhancements

- Integration with real-time weather APIs
- Satellite and GIS data integration
- Time-series flood forecasting
- Deep Learning-based prediction models
- Cloud deployment using AWS or Azure
- Interactive monitoring dashboard
- Real-time flood alerts and notifications

---

## Dataset

The dataset contains environmental and geographical attributes related to flood prediction including rainfall, river flow, humidity, temperature, drainage capacity, urbanization, and deforestation indicators.

---

## Author

**Prajna Nanipatruni**

B.Tech – Computer Science Engineering

Machine Learning | Deep Learning | AI Engineering | Full Stack Development

---

## Project Highlights

- Developed a complete Machine Learning prediction pipeline
- Implemented preprocessing using Label Encoding and Feature Scaling
- Built an end-to-end Flask web application
- Enabled real-time flood risk prediction
- Applied Machine Learning to a real-world environmental problem
- Gained hands-on experience in model deployment and inference systems
