def findsecond_smallest(arr):
    first_smallest = float('inf')
    second_smallest = float('inf')

    for num in arr:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif num < second_smallest and num != first_smallest:
            second_smallest= num
    return second_smallest if second_smallest != float('inf') else None
arr = [7, 3, 9, 2, 5, 1, 8]
print(findsecond_smallest(arr))