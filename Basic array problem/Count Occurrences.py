def find_count_occurences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count +=1
    return count
arr = [2, 5, 2, 8, 2, 9, 5]
target = 2

print(find_count_occurences([2, 5, 2, 8, 2, 9, 5],2))