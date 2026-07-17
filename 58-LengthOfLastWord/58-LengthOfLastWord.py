# Last updated: 17/07/2026, 15:03:18
class Solution:
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])