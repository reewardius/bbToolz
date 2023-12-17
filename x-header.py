import argparse
import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

def read_sites_from_file(file_name):
    with open(file_name, 'r') as file:
        sites = file.readlines()
    sites = [site.strip() for site in sites]
    return sites

def read_headers_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    headers = {line.strip().split(':', 1)[0]: line.strip().split(':', 1)[1].strip() for line in lines if line.strip()}
    return headers

def add_url_scheme(site):
    parsed = urlparse(site)
    if parsed.scheme == '':
        return 'https://' + site
    return site

def make_request(site, session, headers):
    site = add_url_scheme(site)

    if not headers:
        headers = {'X-Forwarded-Host': '127.0.0.1'}

    response = session.get(site, headers=headers)
    initial_body = response.content
    initial_body_length = len(initial_body)
    
    modified_response = session.get(site)
    modified_body = modified_response.content
    modified_body_length = len(modified_body)
    
    if initial_body_length != modified_body_length:
        changed_headers = ', '.join(headers.keys())
        return f"Site {site} - body changed after applying headers: {changed_headers}. Body before: {initial_body_length} bytes, Body after: {modified_body_length} bytes\n"

def make_requests_multithreaded(sites, headers, num_threads):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        with requests.Session() as session:
            futures = [executor.submit(make_request, site, session, headers) for site in sites]
            for future in futures:
                result = future.result()
                if result:
                    print(result, end='')

parser = argparse.ArgumentParser(description='Checking for changes in sites\' response bodies')
parser.add_argument('-l', '-list', metavar='file', type=str, help='File with list of sites')
parser.add_argument('-o', '-output', metavar='file', type=str, help='File to save results')
parser.add_argument('-c', '-threads', metavar='num_threads', type=int, default=5, help='Number of threads')
parser.add_argument('-H', '-headers', metavar='file', type=str, help='File with custom headers')

args = parser.parse_args()

if args.l:
    file_name = args.l
    sites = read_sites_from_file(file_name)
    num_threads = args.c
    headers = read_headers_from_file(args.H) if args.H else {}
    make_requests_multithreaded(sites, headers, num_threads)
else:
    print("Specify a file with a list of sites using -l or -list.")
