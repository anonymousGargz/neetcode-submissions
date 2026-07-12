class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        minSpeed=max(piles)
        while (left<=right):
            speed=(left+right)//2
            totalTime=0
            for pile in piles:
                totalTime+=pile//speed
                if (pile%speed!=0):
                    totalTime+=1
            if (totalTime<=h):
                minSpeed=min(minSpeed, speed)
                right=speed-1
            else:
                left=speed+1
        return minSpeed
        