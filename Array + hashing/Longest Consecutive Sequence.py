def longest_consecutive(arr):
    numbers = set(arr)
    longest = 0

    for num in numbers :
         if num - 1 not in numbers:
              current = num
              count =1
         while current +1 in numbers:
              current +=1
              count +=1
         longest = max(longest, count)

    return longest

arr = [100, 4, 200, 3, 1, 2]

print(longest_consecutive(arr))

    