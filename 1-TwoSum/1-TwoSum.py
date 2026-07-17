# Last updated: 17/07/2026, 15:04:35
class Solution:
    def twoSum(self, nums, target):
        d = {}

        for i in range(len(nums)):
            x = target - nums[i]

            if x in d:
                return [d[x], i]

            d[nums[i]] = i