import requests

api_key = "a2811e34c16e69053249665820876507"

city = input("Enter City: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No city found")
    
else:
    weather = weather_data.json()['weather'][0]['main']
    temperature = round(weather_data.json()['main']['temp'])

    print(f'The weather in {city} is: {weather}')
    print(f'The temperature in {city} is: {temperature}°C')