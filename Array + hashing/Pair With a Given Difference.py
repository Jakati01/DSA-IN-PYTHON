arr = [5, 20, 3, 2, 50, 80]
difference = 78

def has_pair_with_difference(arr, difference):
    seen = set()

    for num in arr:
        required = num - difference

        if required in seen:
            return True

        seen.add(num)
    return False

print(has_pair_with_difference(arr,difference))
       


