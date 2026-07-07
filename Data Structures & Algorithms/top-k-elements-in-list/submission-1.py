class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict=Counter(nums)
        heap=[]
        for key in numDict.keys():
            heapq.heappush(heap, (numDict[key], key))
            if len(heap)>k:
                heapq.heappop(heap)
        answer=[]
        for (val, num) in heap:
            answer.append(num)
        
        return answer
