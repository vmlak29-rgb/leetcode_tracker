# Last updated: 17/07/2026, 15:02:30
class Solution:
    def restoreIpAddresses(self, s):
        
        result = []

        def backtrack(index, parts):
            
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return

            for i in range(index, min(index + 3, len(s))):
                
                part = s[index:i + 1]

                if (part[0] == "0" and len(part) > 1) or int(part) > 255:
                    continue

                backtrack(i + 1, parts + [part])

        backtrack(0, [])

        return result
        