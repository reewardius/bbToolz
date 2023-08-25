import requests
import json

# AlienVault OTX API key
api_key = 'a70cde795be80ab10244bd5bfc65dc79b60101bf7d302600bb5d48d033aa191b'

# Domain to search for subdomains
domain = 'firebaseio.com'

# OTX API endpoint for subdomains
endpoint = f'https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns'

# Headers for the API request
headers = {'X-OTX-API-KEY': api_key}

# Make the API request
response = requests.get(endpoint, headers=headers)

# Parse the JSON response
data = json.loads(response.text)

# Extract the subdomains from the response and remove duplicates
subdomains = list(set([subdomain['hostname'] for subdomain in data['passive_dns']]))

# Save the subdomains to a file
with open('firebase.txt', 'w') as f:
    for subdomain in subdomains:
        f.write(subdomain + '\n')