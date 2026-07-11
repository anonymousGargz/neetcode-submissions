class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1

        while (left<right):
            print(left, right)
            while (left<right and s[left].isalnum() !=True):
                left+=1
            while (right>left and s[right].isalnum()!=True):
                right-=1
            if (left>=right):
                return True
            else:
                print(s[right].lower(), s[left].lower())
                if (s[right].lower()!=s[left].lower()):
                    return False
                else:
                    left+=1
                    right-=1
        return True

        