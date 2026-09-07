class Solution:
   
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        
        for char in set(s):
            first = s.index(char)
            last = s.rindex(char)
            
            if first < last:
                middle_chars = set(s[first + 1:last])
                result += len(middle_chars)
                
        return result
                
                

                

        