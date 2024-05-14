from src.list_based_priority_queue import PriorityQueue


def get_unreachable_cities_for_supply(input_file, output_file):
    cities, storages, gas_lines = read_data_from_file(input_file)
    if len(cities) == 0:
        write_data_to_file(output_file, ["-1"])
        return

    unreachable = []

    graph = {city: [] for city in cities}
    #  fill graph with cities edge is pipeline
    for gas_pipe in gas_lines:
        start_city, end_city = gas_pipe
        if start_city not in cities and end_city not in cities:
            continue
        graph[start_city].append(end_city)

    #  find unreachable cities for each gas storage
    for storage in storages:
        if storage not in cities:
            continue
        visited = dfs(graph, storage)
        unreachable_cities_for_gas_storage = get_unreachable_cities_for_gas_storage(storage, visited, cities)
        if len(unreachable_cities_for_gas_storage[1]) == 0:
            continue
        unreachable.append(str(unreachable_cities_for_gas_storage) + "\n")

    write_data_to_file(output_file, unreachable)


def dfs(graph, start):

    stack = PriorityQueue()
    stack.insert_to_queue(start, 1)
    visited = []
    while stack:
        current_city = stack.delete_from_queue()
        if not current_city:
            return visited

        visited.append(current_city)
        for neighbour in graph[current_city]:
            stack.insert_to_queue(neighbour, 1)
    return visited


def get_unreachable_cities_for_gas_storage(storage, visited, cities):
    difference = []
    for city in cities:
        if city not in visited:
            difference.append(city)
    return storage, difference


def read_data_from_file(filename):
    cities = []
    storages = []
    gas_lines = []

    with open(f"../resources/{filename}", "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines:
            cities = lines[0].strip().split()
            storages = lines[1].strip().split()
            gas_lines = [line.strip().split() for line in lines[2:]]

    return cities, storages, gas_lines


def write_data_to_file(filename, result):
    with open(
        f"../resources/{filename}",
        "w",
        encoding="utf-8",
    ) as file:
        file.writelines(result)
