class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
           
            if not tempStack:
                res[i]=0
                tempStack.append((temperatures[i], i))
            else:
                temp, index= tempStack.pop()
                while (temp<=temperatures[i] and tempStack):
                    temp, index= tempStack.pop()
                if temp>temperatures[i]:
                    res[i]=index-i
                    tempStack.append((temp, index))
                    tempStack.append((temperatures[i], i))
                else:
                    res[i]=0
                    tempStack.append((temperatures[i], i))

        return res
