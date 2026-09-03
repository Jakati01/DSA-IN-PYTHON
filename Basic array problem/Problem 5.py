def count_numbers(arr):
    postive= 0
    negative =0
    zeros =0

    for num in arr:
        if num > 0:
            postive +=1
        elif num <0:
            negative+=1
        else:
            zeros+=1
    return (postive,negative,zeros)
arr = [4, -2, 0, 7, -5, 0, 3, -1]
print(count_numbers(arr))
            