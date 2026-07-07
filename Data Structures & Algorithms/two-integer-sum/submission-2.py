class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict={}
        duplicateDict={}
        duplicates=[]
        for i in range(0, len(nums)):
            if myDict.get(nums[i]) is None:
                myDict[nums[i]]=i
            else:
                duplicates.append(nums[i])
                duplicateDict[nums[i]]=i
        for num in nums:
            toFind=target-num
            if myDict.get(toFind)!=None:
                i=myDict[num]
                j=myDict[toFind]
                if (i==j):
                    if num in duplicates:
                        return [i, duplicateDict[num]]
                    else:
                        continue
                else:
                    return [i, j]
                    
                
        