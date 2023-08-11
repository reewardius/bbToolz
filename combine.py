import sys

def add_suffix_to_lines(input_file_path, suffix_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, \
         open(suffix_file_path, 'r') as suffix_file, \
         open(output_file_path, 'w') as output_file:

        suffix = suffix_file.readline().strip()

        for line in input_file:
            line = line.strip()
            new_line = f"{line}{suffix}\n"
            output_file.write(new_line)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py input_file_path suffix_file_path output_file_path")
        sys.exit(1)

    input_file_path = sys.argv[1]
    suffix_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    add_suffix_to_lines(input_file_path, suffix_file_path, output_file_path)
