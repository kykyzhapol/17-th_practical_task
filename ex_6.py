"""Module for finding shortest path between cities using Dijkstra's algorithm."""

import sys
import heapq


def read_data() -> list:
    """
    Read and parse the road network data file from user input.

    Prompts user for filename, reads the file content,
    and returns non-empty lines as a list without trailing newlines.

    Returns:
        list: List of strings, each representing a non-empty line from the file.

    Raises:
        SystemExit: If file cannot be found or opened.
    """
    filename = input('Enter file name -> ')
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Read all lines, filtering out empty ones
            file_content = [line.strip() for line in file if line.strip()]
    except (FileNotFoundError, FileExistsError) as e:
        print(f'Error - {e}')
        sys.exit(1)
    return file_content


def dijkstra(graph: dict, start: str, end: str) -> float:
    """
    Find the shortest distance between two nodes in a weighted graph.

    Uses Dijkstra's algorithm with a priority queue to find the minimum
    distance from start node to end node.

    Args:
        graph (dict): Graph represented as adjacency list.
                     Format: {node: [(neighbor, weight), ...]}
        start (str): Starting node name.
        end (str): Target node name.

    Returns:
        float: Shortest distance between start and end.
               Returns infinity if no path exists or nodes not in graph.
    """
    # Check if nodes exist in graph
    if start not in graph or end not in graph:
        return float('inf')

    # Initialize distances with infinity, except start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue stores tuples of (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we've found a better path already
        if current_distance > distances[current_node]:
            continue

        # Early exit if we reached the target
        if current_node == end:
            break

        # Check all neighbors of current node
        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances[end]


def build_graph(file_content: list) -> dict:
    """
    Build a graph of roads based on file data.

    File format:
        line 0: number of settlements N (not directly used)
        line 1: number of roads M
        lines 2..2+M-1: each contains "city1 city2 distance"
        last line: "city_A city_B" (processed separately in main)

    Args:
        file_content (list): List of strings from the file.

    Returns:
        dict: Graph as adjacency list where key is city name,
              value is list of tuples (neighbor, distance).
    """
    number_of_roads = int(file_content[1])
    graph = {}

    # Process only the road description lines
    for i in range(2, 2 + number_of_roads):
        parts = file_content[i].split()
        if len(parts) < 3:
            continue  # Skip invalid lines

        city_a, city_b, distance = parts[0], parts[1], int(parts[2])

        # Roads are bidirectional - add to both cities' adjacency lists
        graph.setdefault(city_a, []).append((city_b, distance))
        graph.setdefault(city_b, []).append((city_a, distance))

    return graph


def main() -> None:
    """
    Main program execution.

    Reads road network data from file, builds a graph,
    and finds the shortest path between cities specified in the last line.
    """
    # Read file content
    file_lines = read_data()

    # Last line contains start and end cities
    start_city, end_city = file_lines[-1].split()

    # Build graph and find shortest path
    road_graph = build_graph(file_lines)
    shortest_distance = dijkstra(road_graph, start_city, end_city)

    print(shortest_distance)


if __name__ == '__main__':
    main()
