import requests
import json

domain = "tesla.com" # change

url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns"

headers = {
    "Accept": "application/json",
    "X-OTX-API-KEY": "a70cde795be80ab10244bd5bfc65dc79b60101bf7d302600bb5d48d033aa191b" # Replace <API_KEY> with your OTX API key
}

response = requests.get(url, headers=headers)

data = json.loads(response.text)

for record in data['passive_dns']:
    if record['record_type'] == "CNAME":
        print(record['hostname'])