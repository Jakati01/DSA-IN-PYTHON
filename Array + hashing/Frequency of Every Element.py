''''''''''''''''
Problem 16 — Frequency of Every Element
Given:
arr = [4, 2, 4, 3, 2, 4, 5]
'''''

def every_element(arr):
    frequency = {}

    for num in arr:
       frequency[num] = frequency.get(num,0)+1
    return frequency

arr = [4, 2, 4, 3, 2, 4, 5]
print(every_element(arr))
