# Last updated: 17/07/2026, 15:01:41
class Solution:
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words)