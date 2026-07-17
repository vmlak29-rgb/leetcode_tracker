# Last updated: 17/07/2026, 15:04:14
class Solution:
    def letterCombinations(self, digits):
        
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, current):

            # If all digits are processed
            if index == len(digits):
                result.append(current)
                return

            # Get letters of current digit
            letters = phone[digits[index]]

            # Try every letter
            for letter in letters:
                backtrack(index + 1, current + letter)

        backtrack(0, "")

        return result