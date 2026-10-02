class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        myStack=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while myStack and myStack[-1][0]<= temperatures[i]:
                myStack.pop()
            if myStack:
                ans[i]=myStack[-1][1]-i
            else:
                ans[i]=0
            myStack.append((temperatures[i], i))
        return ans


        