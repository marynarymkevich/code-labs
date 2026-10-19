from api_client import get_json

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

city_name = "Stockholm"
params = {
    "name": city_name,
    "count": 1
}

data = get_json(GEO_URL, params=params)
print("Full response:", data)

if data and data.get("results"):
    first_result = data["results"][0]
    lat = first_result["latitude"]
    lon = first_result["longitude"]
    print(f"Latitude: {lat}, Longitude: {lon}")
else:
    print("City not found")


## Task 2
params = {
    "latitude": 59.32938,
    "longitude": 18.06871,
    "current": "temperature_2m,wind_speed_10m"
}

weather_data = get_json(WEATHER_URL, params=params)
print("\nFull weather response:", weather_data)

if weather_data and weather_data.get("current"):
    current = weather_data["current"]
    units = weather_data["current_units"]

    temp = current["temperature_2m"]
    temp_unit = units["temperature_2m"]

    wind = current["wind_speed_10m"]
    wind_unit = units["wind_speed_10m"]

    print(f"\nTemperature: {temp}{temp_unit}")
    print(f"Wind speed: {wind} {wind_unit}")
