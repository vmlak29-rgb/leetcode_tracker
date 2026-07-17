# Last updated: 17/07/2026, 15:01:08
class Solution:
    def shortestPalindrome(self, s):
        if not s:
            return ""

        rev = s[::-1]
        temp = s + "#" + rev

        lps = [0] * len(temp)
        j = 0

        for i in range(1, len(temp)):
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]

            if temp[i] == temp[j]:
                j += 1
                lps[i] = j

        prefix_len = lps[-1]
        add = rev[:len(s) - prefix_len]

        return add + s
        