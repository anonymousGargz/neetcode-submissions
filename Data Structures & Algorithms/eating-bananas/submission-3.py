class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        minTotal=float("inf")
        while (left<=right):
            hours=(left+right)//2
            total=0
            for i in range(0, len(piles)):
                if hours>=piles[i]:
                    total+=1
                else:
                    total += (piles[i] + hours - 1) // hours
            if total>h:
                left=hours+1
            else:
                right=hours-1
                minTotal=min(minTotal, hours)
        return minTotal


