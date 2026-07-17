# Last updated: 17/07/2026, 15:01:09
class Solution:
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_linear(arr):
            prev = 0
            curr = 0

            for x in arr:
                prev, curr = curr, max(curr, prev + x)

            return curr

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
        