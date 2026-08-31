class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        myHeap=[]
        for num in nums:
            heapq.heappush(myHeap, num)
            if (len(myHeap)>k):
                heapq.heappop(myHeap)
        
        return myHeap[0]
        