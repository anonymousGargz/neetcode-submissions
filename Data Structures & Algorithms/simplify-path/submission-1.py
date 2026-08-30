class Solution:
    def simplifyPath(self, path: str) -> str:
        parts=path.split('/')
        print(parts)
        stack=[]
        for elem in parts:
            if len(elem)>0:
                if elem=='..':
                    if (len(stack)>0):
                        stack.pop()

                else:
                    if elem !='.':
                        stack.append('/'+elem)
        if (len(stack)==0):
            return '/'
        return ( ''.join(stack))