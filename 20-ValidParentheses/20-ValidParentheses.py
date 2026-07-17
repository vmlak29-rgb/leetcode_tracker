# Last updated: 17/07/2026, 15:04:10
class Solution:
    def isValid(self, s):
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")

        return s == ""
        