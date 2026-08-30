class Solution:
    def calculate(self, s: str) -> int:

        # Remove spaces
        s = s.replace(' ', '')

        # First pass: * and /
        stack = []
        i = 0

        while i < len(s):

            if s[i].isdigit():
                stack.append(s[i])
                i += 1

            elif s[i] == '*' or s[i] == '/':
                # Get left number
                num1 = ''
                while stack and stack[-1].isdigit():
                    num1 += stack.pop()

                num1 = int(num1[::-1])

                # Get operator
                op = s[i]
                i += 1

                # Get right number
                num2 = ''
                while i < len(s) and s[i].isdigit():
                    num2 += s[i]
                    i += 1

                num2 = int(num2)

                if op == '*':
                    result = num1 * num2
                else:
                    result = num1 // num2

                # Put result back
                for digit in str(result):
                    stack.append(digit)

            else:
                stack.append(s[i])
                i += 1

        # Second pass: + and -
        s = ''.join(stack)

        result = 0
        num = ''
        op = '+'

        for ch in s:
            if ch.isdigit():
                num += ch

            else:
                if op == '+':
                    result += int(num)
                else:
                    result -= int(num)

                op = ch
                num = ''

        # Process final number
        if op == '+':
            result += int(num)
        else:
            result -= int(num)

        return result