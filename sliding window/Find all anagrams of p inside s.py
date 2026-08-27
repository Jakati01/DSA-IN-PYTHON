'''''''''''''''''
s = "cbaebabacd"
p = "abc"
'''''

class Solution():
    def anagrams(self, s ,p):
        need = {}
        window = {}
        for char in p:
            need [char]= need.get(char,0)+1
        left = 0
        result = []
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0)+1

            while right - left+1 > len(p):
                left_char = s[left]
                window[left_char] -=1

                if window [left_char] ==0:
                    del window[left_char]
                left += 1
            if window == need:
                result.append(left)
        return result

obj = Solution()
print(obj.anagrams("cbaebabacd", "abc"))