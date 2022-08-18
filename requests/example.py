import requests


MY_LAT = 21.027763
MY_LONG = 105.834160


parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,   
}


response = requests.get(url='https://api.sunrise-sunset.org/json', verify=False, params=parameters)

response.raise_for_status()

data = response.json()
results = data['results']
sunrise = results['sunrise']

formatted_sunrise = sunrise.split('T')

print(formatted_sunrise)
