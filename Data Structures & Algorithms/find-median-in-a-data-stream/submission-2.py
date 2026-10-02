import heapq

class MedianFinder:

    def __init__(self):
        self.low = []   # max heap via negatives
        self.high = []  # min heap

    def addNum(self, num: int) -> None:
        # Add to lower half
        heapq.heappush(self.low, -num)

        # Make sure every value in low <= every value in high
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # Keep low the same size as high, or 1 bigger
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]

        return (-self.low[0] + self.high[0]) / 2