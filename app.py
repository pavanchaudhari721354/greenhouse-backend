# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
CORS(app)
import random, datetime
import os

# Create Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend (browser) requests

# --- Simulated data (for now) ---
current_data = {
    "zone_id": 1,
    "temperature": 25.4,
    "humidity": 61.3,
    "soil_moisture": 42.5,
    "light": 580,
    "timestamp": datetime.datetime.utcnow().isoformat()
}

# ✅ 1. Route: Get latest sensor data
@app.route('/api/sensors/latest', methods=['GET'])
def get_latest():
    # Simulate small random updates
    current_data["temperature"] += random.uniform(-0.5, 0.5)
    current_data["humidity"] += random.uniform(-1, 1)
    current_data["soil_moisture"] += random.uniform(-0.5, 0.5)
    current_data["light"] += random.uniform(-10, 10)
    current_data["timestamp"] = datetime.datetime.utcnow().isoformat()
    return jsonify(current_data)


# ✅ 2. Route: Get history (generate dummy data)
@app.route('/api/sensors/history', methods=['GET'])
def get_history():
    history = []
    now = datetime.datetime.utcnow()
    for i in range(10):  # last 10 readings (every 5 mins)
        reading = {
            "timestamp": (now - datetime.timedelta(minutes=i*5)).isoformat(),
            "temperature": 25 + random.uniform(-2, 2),
            "humidity": 60 + random.uniform(-5, 5),
            "soil_moisture": 45 + random.uniform(-5, 5),
            "light": 600 + random.uniform(-50, 50)
        }
        history.append(reading)
    return jsonify(history[::-1])  # oldest first


# ✅ 3. Route: Crop recommendation (simple rule-based)
@app.route('/api/recommend', methods=['POST'])
def recommend_crop():
    data = request.get_json()
    t = data.get("temperature", 25)
    h = data.get("humidity", 60)
    s = data.get("soil_moisture", 45)
    l = data.get("light", 600)

    # Simple rule-based logic
    if 18 <= t <= 30 and 50 <= h <= 85:
        crop = "Tomato"
        reason = "Ideal warm temp and good humidity"
    elif 10 <= t <= 24 and 60 <= h <= 90:
        crop = "Lettuce"
        reason = "Cool temp and high humidity"
    else:
        crop = "Spinach"
        reason = "Moderate tolerance to varied conditions"

    return jsonify({
        "recommendations": [
            {"crop": crop, "score": 0.9, "reason": reason}
        ]
    })

# ✅ Root route to verify deployment
@app.route('/')
def home():
    return jsonify({"message": "Greenhouse Backend Server is Running ✅"})

# ✅ Start Flask server
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
#if __name__ == '__main__':
 #   app.run(debug=True) */
