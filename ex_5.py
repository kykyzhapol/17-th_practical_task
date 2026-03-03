import sys


def read_data() -> list:
    namefile = input('Enter file name ->')
    try:
        with open(namefile, 'r', encoding='utf-8') as f:
            # Читаем все строки, убираем пустые
            file = [line.strip() for line in f if line.strip()]
    except (FileNotFoundError, FileExistsError) as e:
        print(f'Error - {e}')
        sys.exit(1)
    return file


def build_tree(data: list) -> dict:
    tree = {}
    n = int(data[0])
    # Обрабатываем только строки с отношениями (индексы 1..n)
    for relation in data[1:n + 1]:
        parts = relation.split()
        if len(parts) >= 2:  # гарантируем наличие родителя и потомка
            parent, child = parts[0], parts[1]
            tree.setdefault(parent, []).append(child)
        # Строки с ошибками игнорируем (можно добавить предупреждение)
    return tree


def count_descendants(tree: dict, person: str) -> int:
    if person not in tree:
        return 0
    total = 0
    for child in tree[person]:
        total += 1 + count_descendants(tree, child)
    return total


def main() -> None:
    file_data = read_data()
    if not file_data or len(file_data) < 2:
        print('File is empty or has incorrect format')
        sys.exit(1)

    family_tree = build_tree(file_data)
    target_person = file_data[-1]  # последняя строка — искомое имя
    result = count_descendants(family_tree, target_person)
    print(result)


if __name__ == '__main__':
    main()
