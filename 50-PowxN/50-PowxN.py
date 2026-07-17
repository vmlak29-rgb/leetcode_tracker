# Last updated: 17/07/2026, 15:03:29
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        return result