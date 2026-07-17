# Last updated: 17/07/2026, 15:01:05
class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))