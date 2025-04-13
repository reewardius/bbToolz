import sys
from urllib.parse import urlparse, unquote

def extract_domain_and_paths(url, depth=2, max_path_length=20):
    parsed_url = urlparse(url)
    domain = parsed_url.scheme + "://" + parsed_url.netloc

    # Расшифровка %20 и подобного
    raw_path = unquote(parsed_url.path).strip('/')

    if not raw_path or raw_path.strip() == '':
        return None

    path_parts = [part for part in raw_path.split('/') if part.strip()]
    if not path_parts:
        return None

    trimmed_parts = path_parts[:depth]
    path = '/' + '/'.join(trimmed_parts)

    if len(path) > max_path_length:
        return None

    return domain + path

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_file_with_urls> <output_file_prefix>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_prefix = sys.argv[2]

    with open(input_file, "r") as file:
        urls = file.readlines()

    one_level_set = set()
    two_level_set = set()

    for url in urls:
        url = url.strip()
        if not url:
            continue

        one_level = extract_domain_and_paths(url, depth=1)
        two_level = extract_domain_and_paths(url, depth=2)

        if one_level:
            one_level_set.add(one_level)
        if two_level:
            two_level_set.add(two_level)

    with open(f"{output_prefix}_1level.txt", "w") as file1, \
         open(f"{output_prefix}_2level.txt", "w") as file2:

        for entry in sorted(one_level_set):
            file1.write(entry + "\n")
        for entry in sorted(two_level_set):
            file2.write(entry + "\n")

    print("Created:")
    print(f"  One-level paths (unique) → {output_prefix}_1level.txt")
    print(f"  Two-level paths (unique) → {output_prefix}_2level.txt")
