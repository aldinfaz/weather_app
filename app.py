from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "xxx"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_info = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={API_KEY}"
        )
        data = response.json()

        if data.get("cod") == "404":
            error = "City not found."
        else:
            weather = data["weather"][0]["main"]
            temp = round(data["main"]["temp"])
            weather_info = {
                "city": city,
                "weather": weather,
                "temp": temp
            }

    return render_template("index.html", weather_info=weather_info, error=error)

if __name__ == "__main__":
    app.run(debug=True)
