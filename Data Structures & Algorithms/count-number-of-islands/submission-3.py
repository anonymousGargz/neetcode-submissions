class Solution:
    def __init__(self):
        self.grid=[]
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS
        self.grid=grid
        counter=0
        for i in range(0 , len(self.grid)):
            for j in range(0, len(grid[0])):
                if (self.grid[i][j]=="X" or self.grid[i][j]=="0"):
                    continue
                else:
                    counter+=1
                    self.depthFirstSearch(i, j)
        return counter 
    

    def depthFirstSearch(self, starti, startj):
        self.grid[starti][startj]="X"

        positions=[[starti+1, startj], [starti-1,startj], [starti, startj+1], [starti, startj-1]]
        for pos in positions:
            if (pos[0]>= len(self.grid) or pos[0]<0 or pos[1]<0 or pos[1]>=len(self.grid[0])):
                continue
            if self.grid[pos[0]][pos[1]]=="1":
                self.depthFirstSearch(pos[0], pos[1])

        return
        
                
                


        