# Last updated: 17/07/2026, 15:03:21
class Solution:
    def canJump(self, nums):

        reach = 0

        for i in range(len(nums)):

            if i > reach:
                return False

            reach = max(reach, i + nums[i])

        return True
        