import requests
import json

def get_access_token():
    params = {
        'grant_type':'client_credentials',
        'client_id':'20b2453e33887343c8c67d3d98b8f39e',
        'client_secret': '9378dfdb3be0d1063925641187e5e8ab'
    }

    res = requests.post('https://api.snov.io/v1/oauth/access_token', data=params)
    resText = res.text.encode('ascii','ignore')

    return json.loads(resText)['access_token']

print(get_access_token())