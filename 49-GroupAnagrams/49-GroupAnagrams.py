# Last updated: 17/07/2026, 15:03:31
class Solution:
    def groupAnagrams(self, strs):
        d = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in d:
                d[key] = []

            d[key].append(word)

        return list(d.values())