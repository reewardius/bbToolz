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

domain = "s3.amazonaws.com"
hostnames = get_hostnames(domain)

with open("testbuckets.txt", "w") as f:
    for hostname in hostnames:
        if ".s3.amazonaws.com" in hostname:
            f.write(hostname.replace(".s3.amazonaws.com", "") + "\n")
        else:
            f.write(hostname + "\n")