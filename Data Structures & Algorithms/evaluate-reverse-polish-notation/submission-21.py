class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for elem in tokens:
            if elem.lstrip('-').isdigit():
                stack.append(int(elem))
             
            else:
             
                dig1=stack.pop()
                dig2=stack.pop()
                if elem=='+':
                    stack.append(dig1+dig2)
                elif elem=='-':
                    stack.append(dig2-dig1)
                elif elem=='/':
                    stack.append(int(dig2 / dig1))
                else:
                    stack.append(dig2*dig1)
        return stack[0]


        