class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Find the kth largest element in sorted order
        #can't you just add it to heap?
        minHeap=[]
        for num in nums:
            heapq.heappush(minHeap,num)
            if (len(minHeap)>k):
                heapq.heappop(minHeap)
        
        return minHeap[0]
