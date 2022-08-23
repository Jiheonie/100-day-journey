import requests


parameters = {
    'amount': 10,
    'type': 'boolean'
}


response = requests.get('https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
api_results = response.json()
question_data = api_results['results']
