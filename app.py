from flask import Flask, jsonify, request
from flask_cors import CORS
import random, datetime, os

app = Flask(__name__)
CORS(app)

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
def history():
    now = datetime.datetime.now()
    hist = []
    for i in range(24):
        t = now - datetime.timedelta(minutes=i*5)
        hist.append({
            "timestamp": t.isoformat(),
            "temperature": round(random.uniform(20, 30), 2),
            "humidity": round(random.uniform(40, 70), 2),
            "soil_moisture": round(random.uniform(30, 60), 2),
            "light": round(random.uniform(400, 800), 2)
        })
    return jsonify(hist)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
