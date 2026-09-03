class Solution():
    def subarry_product(self, nums, k):
        if k<=0:
            return False
        left = 0
        product =1
        result=0
        

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product //= nums[left]

                left +=1
            result += right -left+1
        return result
obj = Solution()
result = obj.subarry_product([10, 5, 2, 6], 1)
print(result)



                