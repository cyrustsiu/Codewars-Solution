def remove_smallest(numbers):
    result = numbers[:]
    if len(result) < 1:
        return result
    else:
        result.remove(min(result))
        return result
