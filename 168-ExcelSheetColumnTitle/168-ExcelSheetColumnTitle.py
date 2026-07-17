# Last updated: 17/07/2026, 15:01:35
class Solution:
    def convertToTitle(self, columnNumber):
        result = []

        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26

        return ''.join(reversed(result))
        