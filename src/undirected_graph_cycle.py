from collections import deque


def is_cycle(graph):
    for node in graph:
        visited = set()
        queue = deque([(node, None)])
        while queue:
            current_node, parent_node = queue.popleft()
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, current_node))
                elif neighbor != parent_node:
                    return True
    return False


def check_for_cycle_in_graph(input_file, output_file):
    graph = read_file(input_file)

    is_cycle_result = is_cycle(graph)

    if is_cycle_result:
        result = "graph has cycle"
    else:
        result = "graph has not cycle"

    write_file(output_file, result)


def read_file(input_file):
    graph = {}

    with open(f"../resources/{input_file}", "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines:
            for index in range(len(lines)):
                graph[str(index + 1)] = lines[index].strip().split()

    return graph


def write_file(output_file, result):
    with open(
            f"../resources/{output_file}",
            "w",
            encoding="utf-8",
    ) as file:
        file.writelines(result)
