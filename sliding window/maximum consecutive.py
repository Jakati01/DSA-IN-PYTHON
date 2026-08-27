class Solution:
    def maximum_consecutive_ones(self,nums, k):
        left = 0
        zeros = 0
        maximum = 0
        for right in range(len(nums)):
            if nums[right] == 0:
             zeros +=1
            while zeros >k:
                 if nums[left] == 0:
                    zeros -=1
                 left +=1

            maximum = max(maximum,right - left+1)
        return maximum

obj = Solution()
result = obj.maximum_consecutive_ones([1, 1, 0, 0, 1, 1, 1, 0], 2)
print(result)