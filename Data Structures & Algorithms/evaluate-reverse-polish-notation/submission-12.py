class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Evaluate the expression in RPN; that is doable
        stack=[]
        for token in tokens:
            print(stack)
            if (token.isalnum()):
                stack.append(int(token))

            else:
                try:
                    num=int(token)
                    stack.append(num)
                except:
                    if (token=='+'):
                        num1=stack.pop()
                        num2=stack.pop()
                        stack.append(num1+num2)
                    elif (token=='*'):
                        num1=stack.pop()
                        num2=stack.pop()
                        stack.append(num1*num2)
                    elif (token=='-'):
                        num1=stack.pop()
                        num2=stack.pop()
                        stack.append(num2-num1)
                    else:
                        num1=stack.pop()
                        num2=stack.pop()
                        stack.append(int(num2/num1))
        return (stack.pop())

                
                    