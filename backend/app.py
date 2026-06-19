from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

# Load model, scaler, and encoders
model = joblib.load("../backend/flood_model.pkl")
scaler = joblib.load("../backend/scaler.pkl")
label_encoders = joblib.load("../backend/label_encoders.pkl")

app = Flask(__name__, template_folder="../frontend", static_folder="../frontend")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        print("Received Form Data:", request.form)  # Debugging line

        data = {
            "Rainfall_Range_mm": request.form["rainfall_range"],
            "Num_Rainy_Days": int(request.form["num_rainy_days"]),
            "River_Flow_m3s": float(request.form["river_flow"]),
            "Soil_Moisture": float(request.form["soil_moisture"]),
            "Humidity": float(request.form["humidity"]),
            "Temperature": float(request.form["temperature"]),
            "Drainage_Capacity": float(request.form["drainage_capacity"]),
            "Urbanization_Index": float(request.form["urbanization_index"]),
            "Deforestation_Index": float(request.form["deforestation_index"])
        }

        # Encode categorical values
        if data["Rainfall_Range_mm"] in label_encoders["Rainfall_Range_mm"].classes_:
            data["Rainfall_Range_mm"] = label_encoders["Rainfall_Range_mm"].transform([data["Rainfall_Range_mm"]])[0]
        else:
            return jsonify({"error": "Invalid Rainfall Range value."}), 400

        # Convert to DataFrame and scale
        input_df = pd.DataFrame([data])
        input_scaled = scaler.transform(input_df)

        # Predict flood probability
        prediction = model.predict(input_scaled)[0]
        risk_level = "High Risk" if prediction > 0.7 else "Medium Risk" if prediction > 0.4 else "Low Risk"

        return render_template("result.html", prediction=f"Flood Risk: {risk_level} ({prediction:.2f})")

    except Exception as e:
        print("Error:", str(e))  # Debugging line
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
