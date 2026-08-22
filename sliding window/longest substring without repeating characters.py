'''
s = "pwwkew"
Question:
Find the length of the longest substring without repeating characters.
'''
class Solution:
    def longest_substring(self,strs ):
        left =0
        maximum =0
        seen =set()
        for right in range(len(strs)):
            while strs[right] in seen:
                seen.remove(strs[left])
                left+=1
            seen.add(strs[right])
            maximum =max(maximum,right - left+1)
        return maximum

obj = Solution()
print(obj.longest_substring("pwwkew"))