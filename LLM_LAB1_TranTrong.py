# Trong Tran
# 10/29/2026
# LLM_LAB1
# Use AI to create a Python program for weather checking API

import json
import urllib.request
from datetime import datetime
# Coordinates for Fayetteville, NC
LATITUDE = 35.0527
LONGITUDE = -78.8781

# Open-Meteo API endpoint
# temperature_unit=fahrenheit requests degrees F
# timezone=America/New_York forces Eastern Time (EDT/EST)
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={LATITUDE}&longitude={LONGITUDE}&"
    f"current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m&"
    f"temperature_unit=fahrenheit&"
    f"wind_speed_unit=mph&"
    f"timezone=America/New_York"
)


def fetch_weather():
    try:
        # Send HTTP GET request to the API
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        # Extract current weather data and units dictionary
        current = data["current"]
        units = data["current_units"]

        # Neatly format and print the weather report
        print("=" * 40)
        print(" WEATHER REPORT: FAYETTEVILLE, NC ")
        print("=" * 40)
        # print(f"Time (Local):        {current['time']}")
        dt_object = datetime.fromisoformat(current["time"])
        clean_time = dt_object.strftime("%B %d, %Y at %I:%M %p")
        #print(clean_time)
        print(f"Time (Local):        {clean_time}")
        print(
            f"Temperature:         {current['temperature_2m']} {units['temperature_2m']}"
        )
        print(
            f"Feels Like:          {current['apparent_temperature']} {units['apparent_temperature']}"
        )
        print(
            f"Relative Humidity:   {current['relative_humidity_2m']}{units['relative_humidity_2m']}"
        )
        print(
            f"Precipitation:       {current['precipitation']} {units['precipitation']}"
        )
        print(
            f"Wind Speed:          {current['wind_speed_10m']} {units['wind_speed_10m']}"
        )
        print("=" * 40)

    except Exception as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    fetch_weather()