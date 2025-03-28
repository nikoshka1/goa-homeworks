def sort_by_length(arr):
    sorted_list = []
    while len(arr) > 0:
        shortest = arr[0]
        for string in arr:
            if len(string) < len(shortest):
                shortest = string
        arr.remove(shortest)
        sorted_list.append(shortest)
    return sorted_list

def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    num = 0
    while begin_number <= end_number:
        num += begin_number
        begin_number += step
    return num

def series_sum(n):
    result = 0
    for i in range(n):
        result += 1 / (3 * i + 1)
    if len(str(round(result, 2))) == 3:
        return str(round(result, 2)) + "0"
    return str(round(result, 2))

def round_to_next5(n):
    if n % 5 == 0:
        return n
    elif n > 0:
        return n + (5 - (n % 5))
    else:
        return n + (5 - (n % 5))
    
def two_oldest_ages(ages):
    arr = sorted(ages)
    return [arr[-2], arr[-1]]    