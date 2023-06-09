# python parseJS.py -l js.txt

import argparse
import re
import urllib.request

def extract_links_from_url(url, regex_pattern):
    try:
        response = urllib.request.urlopen(url)
        file_content = response.read().decode('utf-8')
        links = re.findall(regex_pattern, file_content)
        return links
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Создаем парсер аргументов командной строки
parser = argparse.ArgumentParser(description='JavaScript URL Parser')
parser.add_argument('-l', '--url_list', type=str, help='File containing URL list')
args = parser.parse_args()

# Проверяем наличие аргумента -l
if not args.url_list:
    print("URL list file not specified. Please use the -l or --url_list argument to specify the file.")
else:
    url_list_file = args.url_list
    regex_pattern = r's3\.amazonaws\.com|storage\.googleapis\.com|blob\.core\.windows\.net'

    with open(url_list_file, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        found_links = extract_links_from_url(url, regex_pattern)
        for link in found_links:
            print(link)
