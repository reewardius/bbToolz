# python parseJS.py -i input.txt

import argparse
import re

def extract_links_from_file(file_path, regex_pattern):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            links = re.findall(regex_pattern, file_content)
            return links
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def parse_files(input_file, regex_pattern):
    with open(input_file, 'r') as file:
        file_paths = file.readlines()

    for file_path in file_paths:
        file_path = file_path.strip()
        found_links = extract_links_from_file(file_path, regex_pattern)
        for link in found_links:
            print(link)

# Создаем парсер аргументов командной строки
parser = argparse.ArgumentParser(description='JavaScript File Parser')
parser.add_argument('-i', '--input', type=str, help='Input file containing file paths')
args = parser.parse_args()

# Проверяем наличие аргумента -i
if not args.input:
    print("Input file not specified. Please use the -i or --input argument to specify the input file.")
else:
    input_file = args.input
    regex_pattern = r"s3\.amazonaws\.com|storage\.googleapis\.com|blob\.core\.windows\.net"

    parse_files(input_file, regex_pattern)
