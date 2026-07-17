# Last updated: 17/07/2026, 15:01:44
class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            res = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for sub in dfs(end):
                        if sub == "":
                            res.append(word)
                        else:
                            res.append(word + " " + sub)

            memo[start] = res
            return res

        return dfs(0)
        