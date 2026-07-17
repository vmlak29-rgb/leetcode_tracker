# Last updated: 17/07/2026, 15:01:00
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = set()

        for i in range(len(nums)):

            # If number already exists in current window
            if nums[i] in window:
                return True

            # Add current number
            window.add(nums[i])

            # Maintain window size k
            if len(window) > k:
                window.remove(nums[i - k])

        return False
        