def count_pairs(pairs):
    tribes = {}
    for pair in pairs:
        boy, girl = pair
        tribes.setdefault(boy, [0, 0])[0] += 1
        tribes.setdefault(girl, [0, 0])[1] += 1

    total_pairs = 0
    for tribe in tribes.values():
        total_pairs += tribe[0] * tribe[1]

    return total_pairs


def check_amount_of_pairs(input_file, output_file):
    pairs = read_file(input_file)
    count_pairs_result = count_pairs(pairs)

    if count_pairs_result:
        result = f"amount of pairs is {count_pairs_result}"
    else:
        result = "no pairs found."
    write_file(output_file, result)


def read_file(input_file):
    pairs = []

    with open(f"D:/Workspace/Labs_sem2/resources/{input_file}", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            pair = line.strip().split()
            if len(pair) == 2:
                pairs.append(pair)
    return pairs


def write_file(output_file, result):
    with open(f"D:/Workspace/Labs_sem2/resources/{output_file}", "w", encoding="utf-8") as file:
        file.write(result)
