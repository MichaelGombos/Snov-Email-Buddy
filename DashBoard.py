import DomainSearch
import TokenGenerator
#Will Eventually be deprecated and replaced by a user-interface class

#your user id and secret can be found in your account page at snov.io
#this program requires a snov.io account to run.

user_id= '20b2453e33887343c8c67d3d98b8f39e'
secret= '9378dfdb3be0d1063925641187e5e8ab'

token = TokenGenerator.get_access_token(user_id,secret)
domain = 'jogger.com'

print(DomainSearch.get_domain_search(domain,token))