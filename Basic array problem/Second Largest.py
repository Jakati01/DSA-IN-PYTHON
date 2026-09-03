def find_second_largest(arr):
    if len(arr) < 2:
        return None
    first_largest = float("-inf")
    second_largest = float("-inf")

    for num in arr:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num

    return second_largest if second_largest != float("-inf") else None


arr = [12, 5, 8, 21, 3, 17]
print(find_second_largest(arr))  
    