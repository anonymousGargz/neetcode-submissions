class Solution:
    def simplifyPath(self, path: str) -> str:
        pathSplit=path.split('/')
        print(pathSplit)
        stack=[]
        for i in range(0, len(pathSplit)):
            print(pathSplit[i], stack)
            if pathSplit[i]=='..' or pathSplit[i]=='' or pathSplit[i]=='.':
            
                if len(stack)>0 and pathSplit[i]=='..':
                    stack.pop()
                else:
                    stack=stack
            else:
                stack.append(pathSplit[i])
              
    
        
        return '/'+'/'.join(stack)

        