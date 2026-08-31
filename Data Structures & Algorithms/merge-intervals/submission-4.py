class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervalsS= sorted(intervals)
        res=[]
        myStack=[]
        for start,end in intervalsS:
            if not myStack:
                myStack.append(start)
                myStack.append(end)

            if start>myStack[-1]:
                second=myStack.pop()
                first=myStack.pop()
                res.append([first, second])
                myStack.append(start)
                myStack.append(end)
            else:
                if end>myStack[-1]:
                    myStack.pop()
                    myStack.append(end)
        second=myStack.pop()
        first=myStack.pop()
        res.append([first, second])
        return res

        