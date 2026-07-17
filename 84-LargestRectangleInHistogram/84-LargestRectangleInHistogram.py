# Last updated: 17/07/2026, 15:02:41
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, h * width)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = n - left - 1
            max_area = max(max_area, h * width)

        return max_area
        