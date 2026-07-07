class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        allLeft=[1]*len(nums)
        allRight=[1]*len(nums)
        runningSum=1
        for i in range(1, len(nums)):
            runningSum*=nums[i-1]
            allLeft[i]=runningSum
        runningSum=1
        for i in range(len(nums)-2, -1,-1):
            runningSum*=nums[i+1]
            allRight[i]=runningSum
        ans=[]
        for i in range(0, len(allLeft)):
            ans.append(allRight[i]*allLeft[i])
        return ans




        
        