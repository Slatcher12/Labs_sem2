from collections import defaultdict
from typing import Dict, List, Tuple

VIRTUAL_START = 'F'
VIRTUAL_END = 'S'


def create_virtual_start_edges(farms: List[str], lines: List[List[str]]) -> None:
    """
    Create virtual start edges for farms.
    """
    for farm in farms:
        lines.append([VIRTUAL_START, farm, float('inf')])


def create_virtual_end_edges(stores: List[str], lines: List[List[str]]) -> None:
    """
    Create virtual end edges for stores.
    """
    for store in stores:
        lines.append([store, VIRTUAL_END, float('inf')])


def flowers_max_flow(input_file: str) -> int | None:
    """
    Calculate the maximum flow of flowers from farms to stores.
    """
    max_flow = 0
    try:
        farms, stores, lines = read_data_from_file(input_file)
        lines = [[line[0], line[1], int(line[2])] for line in lines]
        if not lines or len(farms) == 0 or len(stores) == 0:
            return
    except Exception:
        return

    create_virtual_start_edges(farms, lines)
    create_virtual_end_edges(stores, lines)

    graph = defaultdict(dict[int])

    #  fill graph with cities edge is pipeline
    for line in lines:
        start_city, end_city, weight = line

        graph[start_city][end_city] = weight
    graph = dict(graph)

    while True:
        path = dfs(graph)
        if not path:
            break
        max_flow += subtract_the_least_weight_on_the_way(graph, path)

    return max_flow


def subtract_the_least_weight_on_the_way(graph: Dict[str, Dict[str, float]], path: List[str]) -> int:
    """
    Subtract the least weight on the way.
    """
    min_weight = float('inf')
    for i in range(len(path) - 1):
        start_city = path[i]
        end_city = path[i + 1]
        min_weight = min(graph[start_city][end_city], min_weight)

    for i in range(len(path) - 1):
        start_city = path[i]
        end_city = path[i + 1]
        if graph[start_city][end_city] == min_weight:
            del graph[start_city][end_city]
        else:
            graph[start_city][end_city] -= min_weight

    return int(min_weight)


def dfs(graph):
    """
    Perform depth first search.
    """
    if not graph:
        return None
    queue = [VIRTUAL_START]
    previous_vertex = {
        VIRTUAL_START: None,
    }
    visited = set()

    while queue:
        vertex = queue.pop()
        if vertex in visited:
            continue

        if vertex == VIRTUAL_END:
            return get_path(previous_vertex, vertex, VIRTUAL_START)

        visited.add(vertex)
        for neighbour in graph[vertex]:
            queue.append(neighbour)
            previous_vertex[neighbour] = vertex

    return None


def get_path(from_dict, last_vertex, start_vertex):
    """
    Get the path. using from_dict
    """
    path = []
    while last_vertex != start_vertex:
        path.append(last_vertex)
        last_vertex = from_dict[last_vertex]
    path.append(start_vertex)
    return path[::-1]


def read_data_from_file(filename: str) -> Tuple[List[str], List[str], List[List[str]]]:
    """
    Read data from file.
    """

    with open(f"../resources/{filename}", "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines:
            farms = lines[0].strip().split()
            stores = lines[1].strip().split()
            lines = [line.strip().split() for line in lines[2:]]

    return farms, stores, lines