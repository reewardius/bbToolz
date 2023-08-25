import sys

def read_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.writelines(content)

def add_suffixes(targets, suffixes):
    result = []
    for target in targets:
        target = target.strip()
        if target:
            for suffix in suffixes:
                result.append(target + suffix + '\n')
    return result

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python script.py <файл_с_таргетами> <файл_с_суффиксами> result.txt")
        sys.exit(1)

    targets_file_path = sys.argv[1]
    suffixes_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    targets = read_file(targets_file_path)
    suffixes = read_file(suffixes_file_path)

    targets = [target.strip() for target in targets if target.strip()]

    if not suffixes:
        print("Файл с суффиксами пуст.")
        sys.exit(1)

    modified_targets = add_suffixes(targets, suffixes)
    
    # Объединяем строки, добавляем переносы строк и сортируем
    modified_content = "\n".join(sorted(modified_targets)).strip()

    write_file(output_file_path, modified_content)

    # Открываем файл снова для удаления пустых строк
    with open(output_file_path, 'r') as f:
        lines = f.readlines()
    non_empty_lines = filter(lambda line: line.strip(), lines)

    # Записываем обратно в файл
    with open(output_file_path, 'w') as f:
        f.writelines(non_empty_lines)
