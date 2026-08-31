class Solution:
    def decodeString(self, s: str) -> str:
        resStack=[]
        prev=''
        numStack=[]
        for ch in s:
            print(resStack)
            if ch=='[':
                resStack.append(ch)
                numStack.append(int(prev))
                prev=ch
            elif ch==']':
                pattern=''
                elem=resStack.pop()
                while(elem!='['):
                    pattern=elem+pattern
                    elem=resStack.pop()
               
                for i in range(0, numStack.pop()):
                    resStack.append(pattern)
                prev=ch
            elif ch.isdigit():
                if prev.isdigit():
                    prev= str(int(prev)*10+int(ch))
                else:
                    prev=ch
            else:
                resStack.append(ch)
                prev=ch
        
        return ''.join(resStack)

        