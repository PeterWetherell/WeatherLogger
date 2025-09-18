import json
import glob
import csv
import os

csv_file = "weather_log.csv"
headers = [
    "timestamp", "city", "temp", "feels_like", "pressure",
    "humidity", "dew_point", "uvi", "clouds", "visibility",
    "wind_speed", "wind_deg", "weather"
]

if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(headers)
    print(f"Created {csv_file} with headers")

for filename in glob.glob("weather_*.json"):
    with open(filename, "r") as f:
        data = json.load(f)

        temp = data["current"]["temp"]
        feels_like = data["current"]["feels_like"]
        pressure = data["current"]["pressure"]
        humidity = data["current"]["humidity"]
        dew_point = data["current"]["dew_point"]
        uvi = data["current"]["uvi"]
        clouds = data["current"]["clouds"]
        visibility = data["current"]["visibility"]
        wind_speed = data["current"]["wind_speed"]
        wind_deg = data["current"]["wind_deg"]
        weather = data["current"]["weather"][0]["description"]

        print(f"Filename: {filename}")
        timestamp = filename[8:-5]
        print(f"Temperature: {temp}C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather}")
        print()
    
    try:
        with open(csv_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, "San Diego", temp, feels_like, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, wind_deg, weather])
        os.remove(filename)
        print(f"Deleted {filename}")
        print()

    except Exception as e:
        print(f"Error writing {filename} to CSV: {e}")
        print(f"File was NOT deleted, please check manually")


