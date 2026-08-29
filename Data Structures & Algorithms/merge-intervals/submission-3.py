class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Sort by start time
        #And then use a stack 
        ans=[]
        intervalsS=sorted(intervals)
        stack=[]
        for elem in intervalsS:
            if stack and elem[0]>stack[-1]:
                ans.append([stack[0], stack[-1]])
                stack=[]
                stack.append(elem[0])
                stack.append(elem[1])
            else:
                if stack and (elem[1]>stack[-1]):
                    stack.append(elem[1])
                else:
                    if not stack:
                        stack.append(elem[0])
                        stack.append(elem[1])
        if stack:
            ans.append([stack[0], stack[-1]])
        return ans


        