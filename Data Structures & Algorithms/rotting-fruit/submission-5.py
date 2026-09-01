class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        myQueue=deque()
 
        count=0
        freshFruit=False
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if (grid[i][j]==2):
                    myQueue.append((i,j))
                elif (grid[i][j]==1):
                    freshFruit=True
        if (len(myQueue)==0):
            if freshFruit:
                return -1
            return 0
        while (myQueue):
            count+=1
            level=[]
            for i in range(len(myQueue)):
                starti, startj=myQueue.popleft()
                positions=[ (starti-1, startj), (starti+1, startj), (starti, startj-1), (starti, startj+1)]

                for sti, stj in positions:
                    if (sti>=len(grid) or stj>=len(grid[0]) or sti<0 or stj<0):
                        continue
                    else:
                        if grid[sti][stj]==1:
                            grid[sti][stj]=2
                            level.append((sti, stj))
            for elem in level:
                myQueue.append(elem)
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if (grid[i][j]==1):
                    return -1


        return count-1



        
        
        

        