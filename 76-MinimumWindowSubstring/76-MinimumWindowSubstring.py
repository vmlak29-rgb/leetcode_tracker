# Last updated: 17/07/2026, 15:02:50
class Solution:
    def minWindow(self, s, t):
        
        if len(s) < len(t):
            return ""

        from collections import Counter

        need = Counter(t)
        window = {}

        left = 0
        count = 0
        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] <= need[char]:
                count += 1

            while count == len(t):

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    count -= 1

                left += 1

        return "" if min_len == float("inf") else s[start:start + min_len]
        