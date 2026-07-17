# Last updated: 17/07/2026, 15:03:01
class Solution:
    def mySqrt(self, x):
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right