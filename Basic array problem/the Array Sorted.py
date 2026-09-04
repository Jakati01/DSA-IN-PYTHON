arr = [2, 4, 7, 9, 12]

def is_sorted(arr):
   for i in range(1,len(arr)):
      if arr[i] < arr[i-1]:
         return False
   return True

print(is_sorted([2, 4, 7, 9, 12]))
print(is_sorted([2, 5, 3, 8]))