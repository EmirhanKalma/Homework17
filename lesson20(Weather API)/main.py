import requests
import json

name_city = input("Введите город: ")

geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={name_city}&count=1&language=ru&format=json"
geo_response = requests.get(geo_url)

if geo_response.status_code == 200:
    geo_data = geo_response.json()
    
    if "results" in geo_data:
        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]
        city_name_resolved = geo_data["results"][0]["name"]
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
        weather_response = requests.get(weather_url)
        
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            current_temp = weather_data["current"]["temperature_2m"]
            with open("weather.txt" , 'w' , encoding='utf-8') as file:
                file.write(f"\nГород: {city_name_resolved}\nTемпература: {current_temp}°C\n")
            print(f"Текущая температура: {current_temp}°C")
        else:
            print("Ошибка при получении погоды:", weather_response.status_code)
    else:   
        print(f"Город '{name_city}' не найден.")
else:
    print("Ошибка при поиске города:", geo_response.status_code)