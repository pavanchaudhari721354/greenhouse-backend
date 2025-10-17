from flask import Flask, jsonify, request
from flask_cors import CORS
import random, datetime

app = Flask(__name__)
CORS(app)  # Allow requests from your frontend

# ✅ Test route (you already saw this working)
@app.route('/')
def home():
    return jsonify({"message": "Greenhouse Backend Server is Running ✅"})

# ✅ Main route your frontend is calling
@app.route('/api/sensors/latest', methods=['GET'])
def get_latest_sensor_data():
    """Return a simulated latest sensor reading."""
    data = {
        "zone_id": 1,
        "timestamp": datetime.datetime.now().isoformat(),
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 70), 2),
        "soil_moisture": round(random.uniform(30, 60), 2),
        "light": round(random.uniform(400, 800), 2)
    }
    return jsonify(data)

# ✅ Optional route for future history data (won’t break if unused)
@app.route('/api/sensors/history', methods=['GET'])
def get_sensor_history():
    now = datetime.datetime.now()
    history = []
    for i in range(24):
        record_time = now - datetime.timedelta(minutes=i * 5)
        history.append({
            "timestamp": record_time.isoformat(),
            "temperature": round(random.uniform(20, 30), 2),
            "humidity": round(random.uniform(40, 70), 2),
            "soil_moisture": round(random.uniform(30, 60), 2),
            "light": round(random.uniform(400, 800), 2)
        })
    return jsonify(history)

# ✅ Optional route for recommendations (your Crop Recommendation page)
@app.route('/api/recommend', methods=['POST'])
def recommend_crop():
    data = request.get_json()
    temp = data.get("temperature", 25)
    hum = data.get("humidity", 60)
    soil = data.get("soil_moisture", 45)
    light = data.get("light", 600)
    soil_type = data.get("soil_type", "loam")
    region = data.get("region", "Unknown")

    # Dummy rule-based logic for now
    recommendations = [
        {"crop": "Tomato", "score": 0.92, "reason": "Ideal for warm and moderate moisture"},
        {"crop": "Cucumber", "score": 0.85, "reason": "Good for current humidity and light"},
        {"crop": "Spinach", "score": 0.80, "reason": "Soil moisture suitable for leafy greens"}
    ]

    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
