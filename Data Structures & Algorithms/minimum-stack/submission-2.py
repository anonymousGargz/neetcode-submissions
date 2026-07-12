class MinStack:

    def __init__(self):
        self.stack=[]
      

    def push(self, val: int) -> None:
        if ((len(self.stack))>0):

            prevVal, minVal=self.stack.pop()
            if (minVal<=val):
                self.stack.append((prevVal, minVal))
                self.stack.append((val, minVal))
            else:
                self.stack.append((prevVal, minVal))
                self.stack.append((val, val))        
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        if ((len(self.stack))>0):
            self.stack.pop()
        

    def top(self) -> int:
        if ((len(self.stack))>0):
            prevVal, minVal=self.stack.pop()
            self.stack.append((prevVal, minVal))
            return prevVal
        else:
            return None
        
        

    def getMin(self) -> int:
        if ((len(self.stack))>0):
            prevVal, minVal=self.stack.pop()
            self.stack.append((prevVal, minVal))
            return minVal
        else:
            return None

        
