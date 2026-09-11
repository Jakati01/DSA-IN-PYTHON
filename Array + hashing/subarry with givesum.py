def subarray(arr, target):
   perfix_sum = 0
   seen ={0}


   for num in arr:
      perfix_sum += num

      if perfix_sum - target in seen :
         return True

      seen.add(perfix_sum)
   return False

arr = [1, 2, 3, 7, 5]
target = 12

print(subarray(arr, target))