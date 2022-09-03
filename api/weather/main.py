import requests


api_key = ' '
LAT = 51.507351
LONG = -0.127758


parameter = {
    'lat': LAT,
    'lon': LONG,
    'appid': api_key
}


response = requests.get('https://api.openweathermap.org/data/2.5/weather?', params=parameter)
response.raise_for_status()
print(response.json())

