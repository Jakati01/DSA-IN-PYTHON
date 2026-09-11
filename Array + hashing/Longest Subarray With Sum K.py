def longest_subarray_sum_k(arr, target):
    prefix_sum = 0
    longest = 0
    prefix_index = {0: -1}

    for i, num in enumerate(arr):
        prefix_sum += num

        needed = prefix_sum - target

        if needed in prefix_index:
            length = i - prefix_index[needed]
            longest = max(longest, length)

        if prefix_sum not in prefix_index:
            prefix_index[prefix_sum] = i

    return longest


arr = [10, 5, 2, 7, 1, 9]
target = 15

print(longest_subarray_sum_k(arr, target))