def contains_duplicate(arr):
    hash_set = set()
    for number in arr:
        if number in hash_set:
            return True
        hash_set.add(number)
    return False


print(contains_duplicate([0, 4, 3, 5, 6]))
print(contains_duplicate([0, 4, 3, 5, 4]))
