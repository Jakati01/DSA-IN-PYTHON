def majority(arr):
    candidate = None
    count =0

    for num in arr:
        if count ==0:
            candidate = num
            count =1
        elif num == candidate:
            count +=1
        else:
            count -=1
    return candidate
arr = [3, 3, 4, 2, 3, 3, 5, 3]
print(majority(arr))