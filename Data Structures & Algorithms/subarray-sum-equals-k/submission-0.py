class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res=0
        prefixSum=0
        prefixDict={0:1}
        for num in nums:
            prefixSum+=num
            diff=prefixSum-k
            

            res += prefixDict.get(diff, 0)
            prefixDict[prefixSum]= 1 + prefixDict.get(prefixSum, 0)

        return res
