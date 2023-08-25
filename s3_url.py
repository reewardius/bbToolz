import requests

def get_associated_urls(domain):
    API_KEY = "a70cde795be80ab10244bd5bfc65dc79b60101bf7d302600bb5d48d033aa191b"
    BASE_URL = "https://otx.alienvault.com/api/v1/indicators/hostname/"
    URL = BASE_URL + domain + "/url_list?limit=1000"

    headers = {
        "X-OTX-API-KEY": API_KEY
    }

    response = requests.get(URL, headers=headers)
    data = response.json()
    urls = [entry["url"] for entry in data["url_list"]]

    return urls

domain = "s3.amazonaws.com"
urls = get_associated_urls(domain)

with open("urls.txt", "w") as f:
    for url in urls:
        f.write(url + "\n")