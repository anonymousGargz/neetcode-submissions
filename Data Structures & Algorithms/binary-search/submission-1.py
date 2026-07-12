class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while (left<=right):
            midP=(left+right)//2
            print(nums[midP], target)
            if (nums[midP]==target):
                return midP
            elif (nums[midP]<target):
                left=midP+1
            else:
                right=midP-1
        return -1
            
