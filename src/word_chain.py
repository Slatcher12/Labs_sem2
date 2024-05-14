from collections import defaultdict


def read_data_from_file(filename):
    with open(f"../resources/{filename}", "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines:
            length = int(lines[0].strip().split()[0])
            words = [line.strip().split()[0] for line in lines[1:]]

    return length, words


def build_graph(words):
    graph = defaultdict(list)
    for word in words:
        for i in range(len(word)):
            '''
            adding edge if words are different
            '''
            removed_char_word = word[:i] + word[i + 1:]
            graph[word].append(removed_char_word)
    return graph


def dfs(word, graph, visited, dynamic_programming):
    if word not in graph:
        """
        if not neighbor, return 1
        """
        dynamic_programming[word] = 1
        return 1
    if dynamic_programming[word] != -1:
        return dynamic_programming[word]

    max_length = 0
    for next_word in graph[word]:
        '''
        searching max chain length
        '''
        if next_word in visited.keys() and not visited[next_word]:
            visited[next_word] = True
            max_length = max(max_length, dfs(next_word, graph, visited, dynamic_programming))
            visited[next_word] = False
    dynamic_programming[word] = max_length + 1
    return dynamic_programming[word]


def word_chain(input_file):
    try:
        """
        reading data
        """
        length, words = read_data_from_file(input_file)
    except Exception:
        return -1

    visited = {word: False for word in words}
    graph = build_graph(words)
    dynamic_programming = {word: -1 for word in words}

    max_chain_length = 0
    for word in words:
        visited[word] = True
        max_chain_length = max(max_chain_length, dfs(word, graph, visited, dynamic_programming))
        visited[word] = False

    return max_chain_length
