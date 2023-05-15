# python3 sliceurl.py -i input.txt -o output.txt

import argparse
from urllib.parse import urlparse

def contains_percent(word):
    return '%' in word

def contains_special_chars(word, chars):
    return any(char in word for char in chars)

def main(input_file, output_file, level):
    urls_list = []
    chars = ":*;(){}[]@\".&"

    with open(input_file, 'r') as file:
        for line in file:
            url_str = line.strip()

            if contains_percent(url_str):
                continue

            url_parts = urlparse(url_str)
            path_parts = url_parts.path.split('/')

            for i in range(level):
                if i == 0:
                    base_url = f"{url_parts.scheme}://{url_parts.netloc}"
                    urls_list.append(base_url)
                else:
                    if len(path_parts) < i + 1:
                        break

                    path = '/'.join(path_parts[:i + 1])
                    counter = path.count('-')

                    if contains_special_chars(path, chars) or counter > 1:
                        continue
                    else:
                        values = path.split('/')
                        verify_numeric_values = 0

                        for value in values:
                            if value.isdigit():
                                verify_numeric_values += 1

                        if verify_numeric_values > 0:
                            continue
                        else:
                            resultant_url = f"{url_parts.scheme}://{url_parts.netloc}/{path}"
                            index = resultant_url.find('//')

                            if index != -1:
                                second_index = resultant_url[index + 2:].find('//')
                                if second_index != -1:
                                    resultant_url = resultant_url[:index + 2 + second_index] + '/' + resultant_url[index + 2 + second_index + 2:]

                            urls_list.append(resultant_url)

    # Remove duplicate URLs from the list
    urls_list = list(set(urls_list))

    # Write the resulting URLs to the output file
    with open(output_file, 'w') as file:
        for url in urls_list:
            file.write(url + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='URL Processing')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output file')
    parser.add_argument('-l', '--level', type=int, default=2, help='Level [1, 2 or 3]')
    args = parser.parse_args()

    main(args.input, args.output, args.level)
