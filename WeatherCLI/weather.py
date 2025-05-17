import requests
import sys

def get_weather(city):
    API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description'].title()}")
        print(f"Temperature: {data['main']['temp']}°C")
    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python weather.py <city>")
    else:
        get_weather(sys.argv[1])