def longest_peak(arr):
    left_length = 0
    right_length = 0
    result = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i+1]:
            if right_length == 0:
                left_length += 1
            else:
                right_length = 0
                left_length = 1
        if arr[i] > arr[i+1]:
            right_length += 1
            if left_length != 0:
                if result <= (right_length + left_length + 1):
                    result = right_length + left_length + 1
        if arr[i] == arr[i+1]:
            left_length = 0
            right_length = 0

    return result
