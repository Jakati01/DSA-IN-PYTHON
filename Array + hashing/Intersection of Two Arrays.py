def intersection(arr1, arr2):
    seen = set(arr1)
    result =[]
    for num in arr2:
        if num in seen:
            result.append(num)
            seen.remove(num)
    return result
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 5]

print(intersection(arr1, arr2))

