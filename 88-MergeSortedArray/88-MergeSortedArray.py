# Last updated: 17/07/2026, 15:02:36
class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2)