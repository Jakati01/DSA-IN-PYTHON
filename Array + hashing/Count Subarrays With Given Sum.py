def count_subarrays_with_sum(arr, target):
    prefix_sum = 0
    count = 0
    prefix_frequency = {0: 1}

    for num in arr:
        prefix_sum += num

        needed = prefix_sum - target

        count += prefix_frequency.get(needed, 0)

        prefix_frequency[prefix_sum] = prefix_frequency.get(prefix_sum, 0) + 1

    return count


arr = [1, 2, 3, -2, 5]
target = 3

print(count_subarrays_with_sum(arr, target))