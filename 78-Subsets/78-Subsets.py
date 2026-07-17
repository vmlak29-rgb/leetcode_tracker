# Last updated: 17/07/2026, 15:02:47
class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])

        return result
        