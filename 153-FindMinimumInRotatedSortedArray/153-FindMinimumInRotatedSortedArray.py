# Last updated: 17/07/2026, 15:01:40
class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            
            # Minimum is in the left half (including mid)
            else:
                right = mid

        return nums[left]