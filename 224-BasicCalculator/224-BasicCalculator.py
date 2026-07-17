# Last updated: 17/07/2026, 15:00:59
class Solution:
    def calculate(self, s):
        stack = []
        num = 0
        sign = 1
        result = 0

        i = 0
        while i < len(s):
            c = s[i]

            if c.isdigit():
                num = num * 10 + int(c)

            elif c == '+':
                result += sign * num
                num = 0
                sign = 1

            elif c == '-':
                result += sign * num
                num = 0
                sign = -1

            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif c == ')':
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()

            i += 1

        result += sign * num
        return result