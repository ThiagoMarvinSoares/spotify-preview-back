from flask import Flask, jsonify
import requests

app = Flask(__name__)

#Defining variables for access in the API
clientID ='1d8753533ab74648ba0984010c594d4d'
clientSecret = '89d92c67511b4851828cf4c4bf9acb36'
urlToken = 'https://accounts.spotify.com/api/token'

accessTokenInfo = ""

#Requesting the token to make request to the API
@app.route("/", methods = ['POST', 'GET'])
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
        return accessTokenInfo
    else:
        return jsonify({'error': response.text}), response.status_code

#Function that print the artist data
@app.route("/1", methods=['GET','POST'])
def artistData():
    
    #Made global to be accessible inside the function
    global accessTokenInfo
    
    #Header passing the auth type with the token retrieved
    headers = {
        "Authorization": f"Bearer {accessTokenInfo}" 
    }
    
    #response passing the method + url with the artists ID
    artistID = 'https://api.spotify.com/v1/artists/3qm84nBOXUEQ2vnTfUTTFC'
    response = requests.get(artistID, headers=headers)
    
    #Cheking status code + returning a json with the band data
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': response.text}), response.status_code