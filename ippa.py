#!/usr/bin/python3
# Written in Python3, seems to work in python2


###############
#
#       IPPA -- Icelandic Python Postbox Api
#       https://github.com/gbit-is/ippa
#
###########################

import requests
import json


auth_url = "https://api.mappan.is/epo/v1/auth/tokens" #Token URL for mappan

username = "0101501229" #Enter your username, kennitala
password = "$up3r54f3P4$$" #Enter your password


payload = "grant_type=password&username=%s&password=%s" % (username,password) # Create initial authentication payload

# Create request header
auth_headers = {
    'Authorization': "Basic bWFwcGFuLXBhc3N3b3JkOg==",
    'Content-Type': "application/x-www-form-urlencoded",
    'Accept': "application/json",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'Connection': "keep-alive",
    'Referer': "https://mappan.is/postbox/",
    }


try:
        response = requests.request("POST", auth_url, data=payload, headers=auth_headers) # Perform request
except:
        print("Couldn't connect to authenticator")
        print(response.text)
        exit(1)

try:
        response_json = json.loads(response.text) # Load response as json
except:
        print("couldn't load response as JSON")
        print(response.text)
        exit(1)

try:
         acces_token = response_json["access_token"] # Get Acces Token from response
except:
        print("Couldn't find a token in the response")
        print("Wrong user/pass ?")
        print(response.text)
        exit(1)


data_url = "https://api.mappan.is/epo/v1/postbox/deliveries" # URL for deliveries

querystring = {"active":"true","rows":"200","type":"to"} # Query active shipments


# Create second request header
data_headers = {
    'Origin': "https://mappan.is",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'Authorization': "Bearer " + acces_token, #Use token from earlier step
    'Connection': "keep-alive",
    'Referer': "https://mappan.is/mappan/",
    }



response = requests.request("GET", data_url, headers=data_headers, params=querystring) # Perform request
print(response.text) # Print to terminal
exit(0)
