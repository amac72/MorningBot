import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
# In the ".env" file, this is the token from the weather API
WEATHER = os.getenv('WEATHER')

def get_temp(city_name, state_code):
    # Sends and gets requests, returns in JSON format
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},uk&APPID={WEATHER}")
    info = response.text
    
    # Gets temperature from JSON
    values = json.loads(str(info))
    main = values["main"]
    kelvin = main["temp"]
    celsius = kelvin - 273.15
    fahrenheit = (celsius * (9 / 5)) + 32

    return(celsius, fahrenheit)