class Solution:
    def isValid(self, s: str) -> bool:
        end=[')', '}', ']']
        matchDict={')': '(', '}': '{', ']': '['}
        stack=[]

        for ch in s:
            if ch not in end:
                stack.append(ch)
            else:
                if (len(stack)==0):
                    return False
                else:
                    elem=stack.pop()
                    print(elem, matchDict.get(ch))
                    if elem!=matchDict.get(ch):
                        return False
        if (len(stack)==0):
            return True
        else:
            return False


