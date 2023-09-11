import argparse
import requests
from termcolor import colored as cl

def extract(url):
    try:
        req = requests.get(url).text
        sensitive_data = ['username=', 'email=', 'api=', 'password=', 'secret=', 'token=', 'user=', 'database=', 'hostname=', 'host=']
        
        for data in sensitive_data:
            if data in req:
                print(cl(f"{data} in {url}", color='red'))
    except requests.exceptions.RequestException as e:
        print(f"Request error for {url}: {e}")
    except Exception as e:
        print(f"Error processing {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Extract sensitive data from URLs in a file.')
    parser.add_argument('-l', '--file', required=True, help='Path to the file containing the list of URLs.')

    args = parser.parse_args()
    
    target_file = args.file
    
    try:
        with open(target_file, 'r') as file:
            target_urls = file.read().split('\n')
            
        for url in target_urls:
            if url.strip():  # Check if the line is not empty
                extract(url)
    except FileNotFoundError:
        print(f"File '{target_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
