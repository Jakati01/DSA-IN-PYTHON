''''''''''''''''
Problem 17 — Contains Duplicate
Given an array, determine whether any value appears at least twice.
Example 1
arr = [1, 2, 3, 1]
'''''

def contains_Duplicate(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_Duplicate([1, 2, 3, 1]))
print(contains_Duplicate([1, 2, 3, 4]))