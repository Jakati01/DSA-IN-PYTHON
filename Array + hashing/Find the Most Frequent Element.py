def most_frequent(arr):
    frequences ={}
    max_count= 0
    most_frequent_item = None

    for num in arr:
        frequences[num] = frequences.get(num,0)+1
        

    for key, value in frequences.items():
        if value > max_count:
            max_count = value
            most_frequent_item = key
            
    return most_frequent_item

arr = [1, 2, 2, 3, 1, 2, 4, 2]
print(most_frequent(arr))
    

