class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixDict={}
        total=0
        prefixDict[0]=1
        count=0
        for num in nums:
            total+=num
            
            if total%k in prefixDict:
                count+=prefixDict[total%k]
                prefixDict[total%k]+=1
            else:
                prefixDict[total%k]=1
        return count
            
       
      
         
       
        
