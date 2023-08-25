# https://www.googleapis.com/storage/v1/b/{{bucket_name}}

import requests

def get_hostnames(domain):
    API_KEY = "a70cde795be80ab10244bd5bfc65dc79b60101bf7d302600bb5d48d033aa191b"
    BASE_URL = "https://otx.alienvault.com/api/v1/indicators/domain/"
    URL = BASE_URL + domain + "/passive_dns"

    headers = {
        "X-OTX-API-KEY": API_KEY
    }

    response = requests.get(URL, headers=headers)
    data = response.json()
    hostnames = list(set([entry["hostname"] for entry in data["passive_dns"]]))

    return hostnames

domain = "storage.googleapis.com"
hostnames = get_hostnames(domain)

with open("gcp_buckets.txt", "w") as f:
    for hostname in hostnames:
            f.write(hostname + "\n")
