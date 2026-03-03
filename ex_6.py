import sys
import heapq


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


def dijkstra(graph, start, end):
    """Возвращает кратчайшее расстояние между start и end или inf, если пути нет."""
    if start not in graph or end not in graph:
        return float('inf')

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]          # приоритетная очередь (расстояние, вершина)

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
        if curr_node == end:
            break
        for neighbor, weight in graph[curr_node]:
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances[end]


def filtration(file: list) -> dict:
    """
    Строит граф дорог на основе данных из файла.
    Формат файла:
        строка 0: число населенных пунктов N (не используется напрямую)
        строка 1: число дорог M
        строки 2..2+M-1: каждая содержит "город1 город2 расстояние"
        последняя строка: "город_А город_Б" (обрабатывается отдельно)
    Возвращает словарь, где ключ – название города,
    значение – список кортежей (сосед, расстояние).
    """
    m = int(file[1])  # количество дорог
    graph = {}

    for i in range(2, 2 + m):  # перебираем строки с дорогами
        parts = file[i].split()
        if len(parts) < 3:
            continue  # пропускаем некорректные строки
        city_a, city_b, dist = parts[0], parts[1], int(parts[2])

        # дорога двусторонняя – добавляем в обе стороны
        graph.setdefault(city_a, []).append((city_b, dist))
        graph.setdefault(city_b, []).append((city_a, dist))

    return graph


def main() -> None:
    enter_lst = read_data()
    start_end = enter_lst[-1].split()
    print(dijkstra(filtration(enter_lst), start_end[0], start_end[1]))


if __name__ == '__main__':
    main()
