import sys
from urllib.parse import urlparse

def extract_domain_and_paths(url):
    parsed_url = urlparse(url)
    domain = parsed_url.scheme + "://" + parsed_url.netloc
    paths = parsed_url.path.split('/')[:2]
    path = '/'.join(paths)
    return domain + path

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_file_with_urls> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r") as file:
        urls = file.readlines()

    with open(output_file, "w") as file:
        for url in urls:
            url = url.strip()
            result = extract_domain_and_paths(url)
            file.write(result + "\n")

    print("Results written to", output_file)
