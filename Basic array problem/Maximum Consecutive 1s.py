
def max_consecutive_ones(arr):
    current = 0
    maximum = 0

    for num in arr:
        if num ==1:
            current +=1
            if current > maximum:
                maximum = current
        else:
            current = 0
    return maximum
arr = [1, 1, 0, 1, 1, 1, 0, 1]
print(max_consecutive_ones(arr))
