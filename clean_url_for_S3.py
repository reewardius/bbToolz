import re

def extract_value(url):
    match = re.search(r'//[^/]+/([^/]+?)/', url)
    if match:
        return match.group(1)
    else:
        return ""

# Read the URLs from the input file
with open("urls.txt", "r") as f:
    urls = f.readlines()

# Strip the newline characters from each URL
urls = [url.strip() for url in urls]

# Extract the values from the URLs and write them to the output file
seen = set()
with open("output_values.txt", "w") as f:
    for url in urls:
        value = extract_value(url)
        if value not in seen:
            f.write(value + "\n")
            seen.add(value)
