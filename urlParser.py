from urllib.parse import urlparse

with open('target.txt') as file:
    urls = file.readlines()

paths = []

for url in urls:
    url = url.strip()  # Удаляем лишние пробелы и символы новой строки
    if not url:  # Пропускаем пустые строки
        continue
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path_components = parsed_url.path.split('/')[1:]
    for path in path_components:
        paths.append(domain + '/' + path)

with open('all_paths.txt', 'w') as file:
    for path in paths:
        file.write(path + '\n')
