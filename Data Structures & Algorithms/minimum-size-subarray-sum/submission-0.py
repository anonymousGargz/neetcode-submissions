class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left=0
        right=0
        minLength=100000000000
        curSum=0
        while left<=right and left<len(nums):
            while (curSum<target and right<=len(nums)-1):
                curSum+=nums[right]

                right+=1
            if (curSum>=target):
                minLength=min(minLength, (right-left))
            curSum-=nums[left]
            left+=1
            if (right==left and right<len(nums)-2):
                right+=1
        if (minLength == 100000000000):
            return 0
        else:
            return minLength