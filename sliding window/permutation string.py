class Solution:
    def permutation_string(self, s1,s2):
        need = {}
        window = {}
        left = 0
        for char in s1:
            need[char] = need.get(char,0)+1
            
        for right in range(len(s2)):
            char = s2[right]
            window[char] = window.get(char,0)+1

            while right - left +1 > len(s1):
                left_char = s2[left]
                window[left_char] -= 1

                if window [left_char] == 0:
                    del window[left_char]
                left +=1
                if window == need:
                    return True
        return False
obj = Solution()
result = obj.permutation_string("ab", "eidbaooo")
print(result)


        
