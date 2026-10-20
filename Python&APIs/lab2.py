from api_client import get_json

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

city_name = "Stockholm"

def find_city(city_name):
    params = {
        "name": city_name,
        "count": 1
    }

    data = get_json(GEO_URL, params=params)
    # print("Full response:", data)

    if data and data.get("results"):
        first_result = data["results"][0]
        lat = first_result["latitude"]
        lon = first_result["longitude"]
        country = first_result.get("country", "")
        name = first_result.get("name", city_name)

        return lat, lon, name, country
    else:
        return None, None, None, None


## Task 2
# lat, lon = find_city("Stockholm")

def get_weather(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m"
    }

    weather_data = get_json(WEATHER_URL, params=params)
    # print("\nFull weather response:", weather_data)

    if weather_data and weather_data.get("current"):
        current = weather_data["current"]
        units = weather_data["current_units"]

        temp = current["temperature_2m"]
        temp_unit = units["temperature_2m"]

        wind = current["wind_speed_10m"]
        wind_unit = units["wind_speed_10m"]

        return f"{temp}{temp_unit}, wind {wind} {wind_unit}"


## Task 3
user_city = input("Enter the city name: ").strip()
lat, lon, city_official_name, country = find_city(user_city)

if lat is not None and lon is not None:
    weather_info = get_weather(lat, lon)
    
    if weather_info:
        print(f"\n{city_official_name}, {country}: {weather_info}")
    else:
        print("\nCould not retrieve weather details.")
else:
    print("\nCould not get weather because the city was not found.")
