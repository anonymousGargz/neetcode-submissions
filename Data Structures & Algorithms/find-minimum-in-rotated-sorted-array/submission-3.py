class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        mini=1000000000
        while (left<=right):
            mid=(left+right)//2
            mini=min(nums[mid], mini)
            if (nums[right]<nums[left] and not(nums[mid]<nums[right] and nums[mid]<nums[left])):
                left=mid+1
            else:
                right=mid-1
        return mini