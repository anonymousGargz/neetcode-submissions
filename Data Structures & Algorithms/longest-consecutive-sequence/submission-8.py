class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
     
        nums=set(nums)
        nums=list(nums)
        nums.sort()
        
        print(nums)
        maxi=1
        cur=1
        for i in range(1,len(nums)):
            if abs(nums[i]-nums[i-1])==1:
                cur+=1
            else:
                maxi=max(maxi, cur)
                cur=1
        maxi=max(maxi, cur)
        return maxi

        