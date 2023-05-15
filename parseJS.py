# python parseJS.py -i input.txt

import argparse
import re
import urllib.request

def extract_links_from_url(url, regex_pattern):
    try:
        response = urllib.request.urlopen(url)
        html_content = response.read().decode('utf-8')
        links = re.findall(regex_pattern, html_content)
        return links
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def parse_urls(input_file, output_file, regex_pattern):
    with open(input_file, 'r') as file:
        urls = file.readlines()

    with open(output_file, 'w') as file:
        for url in urls:
            url = url.strip()
            found_links = extract_links_from_url(url, regex_pattern)
            for link in found_links:
                file.write(link + '\n')

# Создаем парсер аргументов командной строки
parser = argparse.ArgumentParser(description='URL Parser')
parser.add_argument('-i', '--input', type=str, help='Input file containing URLs')
args = parser.parse_args()

# Проверяем наличие аргумента -i
if not args.input:
    print("Input file not specified. Please use the -i or --input argument to specify the input file.")
else:
    input_file = args.input
    output_file = "output.txt"
    regex_pattern = r"s3\.amazonaws\.com|storage\.googleapis\.com|blob\.core\.windows\.net"

    parse_urls(input_file, output_file, regex_pattern)
