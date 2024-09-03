from flask import Flask, jsonify
import requests

app = Flask(__name__)

#Defining variables for access in the API
clientID ='1d8753533ab74648ba0984010c594d4d'
clientSecret = '89d92c67511b4851828cf4c4bf9acb36'
urlToken = 'https://accounts.spotify.com/api/token'

accessTokenInfo = ""

#Requesting the token to make request to the API
@app.route("/accessToken", methods = ['POST', 'GET'])
def accessToken():
    global accessTokenInfo
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials",
        "client_id": clientID,
        "client_secret": clientSecret
    }
    
    #Requesting the json file passing the header and the data
    response = requests.post(urlToken, headers=headers, data=data)   

    #Checking if the server was able to get the access token for requests
    if response.status_code == 200:
        response_data = response.json()
        accessTokenInfo = response_data.get("access_token")
        return jsonify(accessTokenInfo)
    else:
        return jsonify({'error': response.text}), response.status_code