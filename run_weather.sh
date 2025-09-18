#!/bin/bash
# run_weather.sh

cd "$(dirname "$0")" || exit

python3 FetchWeather.py
python3 JsonToCSV.py

echo "Weather data fetched and logged at $(date)"
