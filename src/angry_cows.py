def place_cows(free_places, cows_to_place, min_distance):
    placed_cows = 1
    last_place = free_places[0]

    for i in range(1, len(free_places)):
        if free_places[i] - last_place >= min_distance:
            placed_cows += 1
            last_place = free_places[i]

    return placed_cows >= cows_to_place


def get_max_width(cows, free_sections):

    if cows == 2:
        return max(free_sections) - min(free_sections)

    free_sections.sort()
    result = 0
    min_distance = 0
    max_distance = free_sections[-1] - free_sections[0]

    while min_distance <= max_distance:
        mid_distance = (min_distance + max_distance) // 2
        if place_cows(free_sections, cows, mid_distance):
            result = mid_distance
            min_distance = mid_distance + 1
        else:
            max_distance = mid_distance - 1

    return result