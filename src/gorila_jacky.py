def can_eat_banana(piles, hours_predicted, velocity):
    hours_gained = 0

    for pile in piles:
        hours_gained += (pile - 1) // velocity + 1

    return hours_gained <= hours_predicted


def get_max_eating_speed(piles, hours_before_security):
    result = 0
    left_iterator = 0
    right_iterator = max(piles)

    while left_iterator <= right_iterator:
        mid_distance = (left_iterator + right_iterator) // 2
        if not can_eat_banana(piles, hours_before_security, mid_distance):
            left_iterator = mid_distance + 1
        else:
            right_iterator = mid_distance - 1
            result = mid_distance

    return result
