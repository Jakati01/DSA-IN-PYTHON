def unique(arr):
    count= {}
    

    for num in arr:
        count[num] = count.get(num,0)+1

    for num in arr:
        if count[num] ==1:
            return num
    return None

    
arr = [4, 5, 1, 2, 1, 4, 5, 6]
print(unique(arr))
