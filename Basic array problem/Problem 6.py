'''''''''''''''
Find the Largest Difference
Given:
arr = [7, 1, 5, 3, 6, 4]
Find the maximum difference between two elements where the larger element comes after the smaller element.
'''''''''

def Largest_Difference(arr):
    miniumum_so_far = arr[0]
    best_differences =0

    for num in arr:
       if num < miniumum_so_far:
           miniumum_so_far = num

       difference = num - miniumum_so_far
       if difference > best_differences:
          best_differences = difference
    return best_differences
arr = [7, 1, 5, 3, 6, 4]
print(Largest_Difference(arr))