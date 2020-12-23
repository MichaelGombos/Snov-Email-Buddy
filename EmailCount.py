import TokenGenerator
import requests
import json

def get_email_count():
    token = TokenGenerator.get_access_token()
    params = {'access_token':token,
            'domain':'jogger.com'

    }

    res = requests.post('https://api.snov.io/v1/get-domain-emails-count', data=params)

    return json.loads(res.text)

print(get_email_count())