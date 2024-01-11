# python xss.py -u input.txt -p knoxss-payloads.txt -o out.txt

# The main task of this script is to take the URL from the file, the value of the parameter should be FUZZ, 
# values from the file payloads.txt are substituted into it, all generated values should be opened through OpenMultipleUrls to check for those that worked.


import argparse
import re

def replace_fuzz(input_url, replacement_file, output_file):
    with open(replacement_file, 'r') as replacement_file:
        replacements = [re.escape(line.strip()) for line in replacement_file.readlines()]

    with open(input_url, 'r') as input_file:
        urls = input_file.readlines()

    with open(output_file, 'w') as output_file:
        for url in urls:
            for replacement in replacements:
                modified_url = re.sub(r'FUZZ', replacement, url)
                output_file.write(modified_url.strip() + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Replace FUZZ in URLs with values from another file")
    parser.add_argument("-u", "--url_file", help="Input file with URLs containing FUZZ", required=True)
    parser.add_argument("-p", "--replacement_file", help="File with replacement values", required=True)
    parser.add_argument("-o", "--output_file", help="Output file for modified URLs", required=True)
    args = parser.parse_args()

    replace_fuzz(args.url_file, args.replacement_file, args.output_file)
