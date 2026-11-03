import json
import urllib.request


def get_fayetteville_weather():
    # Fayetteville, North Carolina coordinates
    latitude = 35.0527
    longitude = -78.8784

    # Open-Meteo API URL with parameters for 7-day daily forecast, Fahrenheit, and NC time zone
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&"
        f"daily=temperature_2m_max,temperature_2m_min&"
        f"temperature_unit=fahrenheit&"
        f"timezone=America%2FNew_York"
    )

    print("Fetching weather data for Fayetteville, North Carolina...\n")

    try:
        # Open the URL and read the JSON response using built-in libraries
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        # Extract the daily forecast lists from the JSON dictionary
        dates = data["daily"]["time"]
        max_temps = data["daily"]["temperature_2m_max"]
        min_temps = data["daily"]["temperature_2m_min"]

        # Display the data neatly
        print("=" * 45)
        print(" 7-DAY WEATHER FORECAST: FAYETTEVILLE, NC ")
        print("=" * 45)

        # Loop through the 7 days and print each line cleanly
        for i in range(len(dates)):
            date = dates[i]
            max_t = max_temps[i]
            min_t = min_temps[i]
            print(f" Date: {date}  |  High: {max_t}°F  |  Low: {min_t}°F")

        print("=" * 45)

    except Exception as e:
        print(f"An error occurred while fetching the weather data: {e}")


# Run the program
if __name__ == "__main__":
    get_fayetteville_weather()