# Last updated: 17/07/2026, 15:03:44
class Solution:
    def combinationSum(self, candidates, target):
        
        result = []

        def backtrack(start, path, total):
            
            if total == target:
                result.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)

        return result