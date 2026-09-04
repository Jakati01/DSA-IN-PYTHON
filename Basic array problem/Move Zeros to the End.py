def move_zeros(arr):
    insert_pos =0

    for num in arr:
        if num !=0:
            arr[insert_pos] = num
            insert_pos+=1

    while insert_pos < len(arr):
        arr[insert_pos] = 0
        insert_pos +=1
    return arr

arr = [0, 1, 0, 3, 12]

print(move_zeros(arr))

#time o(n)
#space o(1)