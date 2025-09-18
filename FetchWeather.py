import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
lat = os.getenv("LAT")
lon = os.getenv("LON")

URL = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourly,daily,minutely&appid={api_key}&units=metric"

response = requests.get(URL)
data = response.json()

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"weather_{timestamp}.json"

with open(filename, "w") as f:
    json.dump(data, f, indent=2)

print(f"Weather data saved to {filename}")