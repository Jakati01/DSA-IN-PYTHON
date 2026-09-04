arr = [4, 7, 4, 2, 7, 9]

def  non_repeating(arr):
    frequency = {}
    
#phase1 -- 
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] =1
#phase 2
    for num in arr:
        if frequency[num] ==1:
            return num
    return None

print(non_repeating(arr))
        
        