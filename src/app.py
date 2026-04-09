import os
import requests
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/weather")
def get_weather():
    city = request.args.get("city", "Chennai")

    if not API_KEY:
        return jsonify({"error": "API_KEY not configured"}), 500

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    return jsonify({
        "city": city,
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)