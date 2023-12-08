import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_conditions = data["weather"][0]["description"]

            print(f"Weather in {location}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {weather_conditions}")
        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_key = "532e49ff611bc2e4e95a0b964997a1f3" #this is my api key in openweathermap
    location = input("Enter a city or ZIP code: ")
    get_weather(api_key, location)
