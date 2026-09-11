def zerosubarray(arr):
    perfix_sum = 0
    seen = {0}

    for num in arr:
        perfix_sum +=num

        if perfix_sum in seen:
            return True

        seen.add(perfix_sum)

    return False

arr = [4, 2, -3, 1, 6]

print(zerosubarray(arr))