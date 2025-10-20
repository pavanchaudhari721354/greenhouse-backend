from flask import Flask, jsonify, request
from flask_cors import CORS
import random, datetime, os

app = Flask(__name__)
CORS(app)  # enable frontend access

@app.route('/')
def home():
    return jsonify({"message": "Greenhouse Backend Server is Running ✅"})

@app.route('/api/sensors/latest', methods=['GET'])
def latest_sensor():
    data = {
        "zone_id": 1,
        "timestamp": datetime.datetime.now().isoformat(),
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 70), 2),
        "soil_moisture": round(random.uniform(30, 60), 2),
        "light": round(random.uniform(400, 800), 2)
    }
    return jsonify(data)

@app.route('/api/sensors/history', methods=['GET'])
def sensor_history():
    now = datetime.datetime.now()
    history = []
    for i in range(24):
        t = now - datetime.timedelta(minutes=i * 5)
        history.append({
            "timestamp": t.isoformat(),
            "temperature": round(random.uniform(20, 30), 2),
            "humidity": round(random.uniform(40, 70), 2),
            "soil_moisture": round(random.uniform(30, 60), 2),
            "light": round(random.uniform(400, 800), 2)
        })
    return jsonify(history)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    body = request.get_json()
    recommendations = [
        {"crop": "Tomato", "score": 0.92, "reason": "Ideal for warm temp and moderate moisture"},
        {"crop": "Cucumber", "score": 0.85, "reason": "Good for humidity and light"},
        {"crop": "Spinach", "score": 0.80, "reason": "Soil moisture supports leafy greens"}
    ]
    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ✅ Required for Render
    app.run(host="0.0.0.0", port=port, debug=True)
