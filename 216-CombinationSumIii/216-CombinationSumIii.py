# Last updated: 17/07/2026, 15:01:06
class Solution:
    def combinationSum3(self, k, n):
        result = []

        def backtrack(start, path, total):
            # Valid combination found
            if len(path) == k:
                if total == n:
                    result.append(path[:])
                return

            # Try numbers from start to 9
            for num in range(start, 10):
                
                # Stop if sum exceeds n
                if total + num > n:
                    break

                path.append(num)

                backtrack(num + 1, path, total + num)

                # Backtrack
                path.pop()

        backtrack(1, [], 0)

        return result