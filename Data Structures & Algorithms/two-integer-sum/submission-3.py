class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #value/index hashmap
        hashMap={}
        for i in range(0, len(nums)):
            hashMap[nums[i]]=i
        
        for i in range(0, len(nums)):
            find= target-nums[i]

            index= hashMap.get(find, -1)
            if (index!=-1 and index!=i):
                return [i, index]
            
        
