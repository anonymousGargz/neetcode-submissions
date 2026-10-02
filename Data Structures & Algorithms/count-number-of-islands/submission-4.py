class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total=0
    
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):

                if grid[i][j]=="1":
                    grid[i][j]=="0"
                    total+=1
                    myStack=[]
                    myStack.append((i, j))
                    while myStack:
                        k,l=myStack.pop()
                        options=[(k+1, l), (k-1, l), (k, l+1), (k, l-1)]
                        for celli, cellj in options:
                            if (celli>=0 and cellj>=0 and celli<len(grid) and cellj<len(grid[0]) and grid[celli][cellj]=="1"):
                                grid[celli][cellj]="0"
                                myStack.append((celli, cellj))
        return total




        