
def largest_element(arr):
    max_value = arr[0]

    for num in arr:
        if num > max_value:
            max_value = num

    return max_value
arr = [12, 5, 8, 21, 3, 17]
print(largest_element(arr))  
    
