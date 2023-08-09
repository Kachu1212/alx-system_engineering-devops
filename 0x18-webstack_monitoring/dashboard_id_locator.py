#!/usr/bin/python3
import requests

# Set up the API endpoint and parameters
api_url = "https://api.datadoghq.com/api/v1/dashboard/"
api_key = "d4856644351b156fbc9057d09a3eba64"
api_app_key = "c08448f2f2311e14821accfd4c45010e7266b2f2"
headers = {'Content-type': 'application/json', 'DD-API-KEY': api_key, 'DD-APPLICATION-KEY': api_app_key}
query_params = {'filter': 'host:187813-web-01'}

# Make the API call to get the host details
response = requests.get(api_url, headers=headers, params=query_params)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()
    print(response_json)
