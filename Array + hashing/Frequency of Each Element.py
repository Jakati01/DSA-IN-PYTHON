def frequency_count(arr):
    count = {}

    for  num in (arr):
        count[num] = count.get(num,0)+1
    return count
arr = [1, 2, 2, 3, 1, 2, 4]
result = frequency_count(arr)

for key, val in result.items():
    print(f"{key} → {val}")