def twosum(arr,target):
    seen ={}

    for i, num in enumerate(arr):
        complement = target- num

        if complement in seen:
            return[seen[complement],i]

        seen[num] =i
    return []

print(twosum([3, 2, 4],6))