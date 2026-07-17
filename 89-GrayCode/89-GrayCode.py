# Last updated: 17/07/2026, 15:02:35
class Solution:
    def grayCode(self, n):
        result = []

        for i in range(2 ** n):
            result.append(i ^ (i >> 1))

        return result
        