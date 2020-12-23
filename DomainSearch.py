import json
import requests
import TokenGenerator

def get_domain_search(domain):
    token = TokenGenerator.get_access_token()
    params = {
    'access_token': token,
    'domain': domain,
    'type': 'all',
    'limit': 100,
    'lastId': 0
    }

    res = requests.get('https://api.snov.io/v2/domain-emails-with-info', params=params)

    return json.loads(res.text)

print(get_domain_search('jogger.com'))