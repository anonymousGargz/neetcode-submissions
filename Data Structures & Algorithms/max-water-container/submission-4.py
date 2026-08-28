class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxAr=0


        while (left<right):
            curArea=min(heights[left], heights[right])*(right-left)
            maxAr=max(curArea, maxAr)
            if (heights[left]<heights[right]):
                left+=1
            else:
                right-=1
        return maxAr


