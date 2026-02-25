import requests
import dotenv
from dotenv import find_dotenv, set_key
import base64
import os

client_ID = dotenv.dotenv_values(".env").get("CLIENT_ID")
secret_ID = dotenv.dotenv_values(".env").get("SECRET_KEY")
str = client_ID + ':' + secret_ID
encoded = base64.b64encode(str.encode('utf-8'))
url = "https://accounts.spotify.com/api/token"

def token_req(URL, CLIENT, SECRET):  # sends an HTTP POST request to the specified URL, this is how you request your API key via spotify
    DATA = {"grant_type": "client_credentials"}
    str = CLIENT + ':' + SECRET
    encoded = base64.b64encode(str.encode("utf-8")).decode("utf-8")
    head = {"Authorization": 'Basic ' + f"{encoded}"}
    req = requests.post(url=URL,headers=head,data=DATA)
    response = req.json()
    return response['access_token']

def update(key_name, new_value): # updates the values in our .env file
    file = find_dotenv()
    set_key(file,key_name,new_value)
    os.environ[key_name] = new_value

token = token_req(url, client_ID, secret_ID)
update('API_KEY', token)

access = dotenv.dotenv_values(".env").get("API_KEY")
type = dotenv.dotenv_values(".env").get("TOKEN_TYPE")

def get_artist(ID, type, access): # returns the artist's name
    URL = f"https://api.spotify.com/v1/artists/{ID}"
    head = {'Authorization' : f'{type} {access}'}
    r = requests.get(url=URL, headers=head)
    response = r.json()
    return response['name']

Mac = get_artist("7eKkW1zo5uzW8kUntiiBvz", type, access)
print(Mac)
