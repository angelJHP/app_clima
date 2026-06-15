import os
import requests

def get_weather(city):
    api_key = os.getenv('API_KEY')
    base_url = "http://api.openweathermap.org/data/2.5/weather" 
    complete_url = f"{base_url}?q={city}&lang=es&appid={api_key}&units=metric"
    
    try:
        response = requests.get(complete_url)
        response.raise_for_status()

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
            return {"error": "Ciudad no encontrada"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error al conectar con la API: {str(e)}"}
    except (KeyError, ValueError) as e:
        return {"error": f"Error al procesar los datos: {str(e)}"}

