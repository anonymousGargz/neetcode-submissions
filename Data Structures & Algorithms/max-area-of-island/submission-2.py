class Solution:
    def __init__(self):
        self.grid=[]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid=grid
        count=0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if self.grid[i][j]==1:
                    area=self.dfs(i, j)
                    count=max(area, count)
                    self.grid=grid
        return count


    



    def dfs(self, starti, startj):
        stack=[]
        counter=0
        
        stack.append((starti, startj))
        while (stack):
            starti, startj=stack.pop()
            if self.grid[starti][startj]==1:
                self.grid[starti][startj]=5
                counter+=1
                pos=[(starti-1, startj), (starti+1, startj), (starti, startj-1), (starti, startj+1)]
                for si, sj in pos:
                    if (si>=len(self.grid) or sj>=len(self.grid[0]) or si<0 or sj<0):
                        continue
                    else:
                        stack.append((si, sj))
        return counter

        