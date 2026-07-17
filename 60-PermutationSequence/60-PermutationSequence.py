# Last updated: 17/07/2026, 15:03:14
class Solution:
    def getPermutation(self, n, k):
        numbers = []
        fact = 1

        for i in range(1, n + 1):
            numbers.append(str(i))
            fact *= i

        k -= 1
        ans = ""

        while n > 0:
            fact //= n
            index = k // fact
            ans += numbers.pop(index)
            k %= fact
            n -= 1

        return ans
        