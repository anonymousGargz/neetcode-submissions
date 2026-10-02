class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen={}
        mySet=set()
        maxi=0
        left=0
        right=0
        while right<len(s):
            if s[right] in mySet:
                maxi=max(maxi, right-left)
                newLeft=lastSeen[s[right]]
     
                for j in range(left, newLeft):

               
                    mySet.remove(s[j])
                left=newLeft+1
            lastSeen[s[right]]=right
            mySet.add(s[right])
            right+=1
        maxi=max(maxi, right-left)
        return maxi
                    

        