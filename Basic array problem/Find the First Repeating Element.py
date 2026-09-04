'''''''''''''''''''''''''''
Given:
arr = [4, 7, 2, 7, 9, 4]

'''''''''''''''

def first_repeating(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None

arr = [4, 7, 2, 7, 9, 4]
print(first_repeating(arr))

