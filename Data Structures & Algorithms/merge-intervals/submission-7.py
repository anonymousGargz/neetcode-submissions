class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        myStack=[]
        intervals.sort(key=lambda x: x[0])
        for i in range(0, len(intervals)):
            if myStack:
                if myStack[-1][1]>=intervals[i][0]:
                    if myStack[-1][1]>=intervals[i][1]:
                        continue
                    else:
                        start, end= myStack.pop()
                        myStack.append((start, intervals[i][1]))
                else:
                    myStack.append((intervals[i][0], intervals[i][1]))
            else:
                myStack.append((intervals[i][0], intervals[i][1]))

        return myStack


        