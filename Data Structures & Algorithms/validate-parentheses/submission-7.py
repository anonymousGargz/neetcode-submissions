class Solution:
    def isValid(self, s: str) -> bool:
        myStack=[]
        stackSym=['(', '{', '[']
        mappingDict={')': '(', '}':'{', ']':'['}

        for ch in s:
            if ch in stackSym:
                myStack.append(ch)
            else:
                if (len(myStack)==0):
                    return False
                toMatch=myStack.pop()
                if mappingDict[ch]!=toMatch:
                    return False
        if (len(myStack)==0):
            return True
        else:
            return False
                
        