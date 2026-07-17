# Last updated: 17/07/2026, 15:03:42
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Step 1: Place numbers in correct index (1 -> index 0, 2 -> index 1, ...)
        i = 0
        while i < n:
            correct_pos = nums[i] - 1

            if 1 <= nums[i] <= n and nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1

        # Step 2: Find first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
        