# Last updated: 17/07/2026, 15:03:11
class Solution:
    def uniquePaths(self, m, n):
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[-1]
        