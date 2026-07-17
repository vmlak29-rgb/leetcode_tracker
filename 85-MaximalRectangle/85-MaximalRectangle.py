# Last updated: 17/07/2026, 15:02:40
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        def largestHistogram(heights):
            stack = []
            res = 0
            n = len(heights)

            for i in range(n):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    res = max(res, h * width)
                stack.append(i)

            while stack:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = n - left - 1
                res = max(res, h * width)

            return res

        for row in matrix:
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            max_area = max(max_area, largestHistogram(heights))

        return max_area
        