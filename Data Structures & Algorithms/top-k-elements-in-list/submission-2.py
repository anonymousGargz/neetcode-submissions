
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This is a min heap problem 
        
        count = Counter(nums)
        
        myHeap = []
        for num, freq in count.items():
            heapq.heappush(myHeap, (freq, num))
            if len(myHeap) > k:
                heapq.heappop(myHeap)
        
        output = []
        for (freq, elem) in myHeap:
            output.append(elem)
        return output

            
        