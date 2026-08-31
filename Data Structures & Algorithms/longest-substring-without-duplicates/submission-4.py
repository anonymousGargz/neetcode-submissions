class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenDict={}
        mySet=set()
        left=0 
        right=0
        maxString=0 
        while(right<len(s)):
            if s[right] in mySet:
                newLeft=seenDict[s[right]]+1
                seenDict[s[right]]=right
                maxString=max(maxString, right-left)
                right+=1
                for elem in range(left, newLeft-1):
                    mySet.remove(s[elem])
                
                left=newLeft
                
            else:
                seenDict[s[right]]=right
                mySet.add(s[right])
                right+=1
               

        return max(maxString, right-left)      
