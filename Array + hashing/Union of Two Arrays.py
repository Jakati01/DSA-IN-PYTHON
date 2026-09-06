def union(arr1,arr2):
    result = set()

    for num in arr1:
        result.add(num)

    for num in arr2:
        result.add(num)

    return list (result)
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 4, 5, 6]

print(union(arr1, arr2))