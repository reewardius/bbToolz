#python path-slicer.py -l input_file.txt -o output_file.txt

# https://www.example.com/path/to/something
# https://www.example.com/another/path/to/file.html
# https://www.example.com/one_more_path
# https://www.example.com/just-one-segment

# /path/to/something
# /another/path/to/file.html
# /one_more_path
# /just-one-segment




import argparse
from urllib.parse import urlparse

def extract_paths(links_file, output_file):
    with open(links_file, 'r') as file:
        lines = file.readlines()
        with open(output_file, 'w') as output:
            for line in lines:
                url = line.strip()
                parsed_url = urlparse(url)
                path = parsed_url.path
                output.write(path + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract paths from URLs')
    parser.add_argument('-l', '--links', type=str, help='Path to the file containing URLs')
    parser.add_argument('-o', '--output', type=str, help='Output file to save paths')
    args = parser.parse_args()

    if args.links and args.output:
        extract_paths(args.links, args.output)
    else:
        print("Please provide both input (-l) and output (-o) file paths.")
