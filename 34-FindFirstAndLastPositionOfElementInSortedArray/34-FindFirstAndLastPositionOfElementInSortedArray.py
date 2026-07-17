# Last updated: 17/07/2026, 15:03:50
class Solution:
    def searchRange(self, nums, target):

        if target not in nums:
            return [-1, -1]

        first = nums.index(target)
        last = len(nums) - 1 - nums[::-1].index(target)

        return [first, last]
        