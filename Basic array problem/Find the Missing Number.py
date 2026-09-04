def missing_number(arr):
    n = len(arr)

    except_value = n*(n+1)//2
    actual_value = 0

    for num in arr:
        actual_value +=num

    return except_value - actual_value

arr=[0, 1]
print(missing_number(arr))

#time = 0(n)
#space = 0(1)
   