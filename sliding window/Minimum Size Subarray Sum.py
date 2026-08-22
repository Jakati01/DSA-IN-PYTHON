''''''''''''''''
arr = [2, 3, 1, 2, 4, 3]
target = 7
Find the minimum length subarray whose sum is:
'''''''''

class Solution:
    def minimum_length_subarray(self,arr,target):
        left = 0
        window_sum = 0
        minimum =float('inf')
        for right in range(len(arr)):
            window_sum+= arr[right]
            while window_sum >= target:
                minimum =min(minimum, right - left+1)
                window_sum -= arr[left]
                left +=1
                
        return minimum
obj = Solution()
result = obj.minimum_length_subarray([2, 3, 1, 2, 4, 3],7)
print(result)

             
            