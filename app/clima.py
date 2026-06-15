import requests

def get_weather(city):
    api_key = "969c2d2ff445f9873d4afa65e8748366"
    base_url = "http://api.openweathermap.org/data/2.5/weather" 
    complete_url = f"{base_url}?q={city}&lang=es&appid={api_key}&units=metric"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']    
        return {
            "temperature": main['temp'],
            "pressure": main['pressure'],
            "humidity": main['humidity'],
            "wind_speed": wind['speed'],
            "description": weather_desc
        }
    else:
        return {"error": "City not found"}

#print(get_weather("Madrid"))    