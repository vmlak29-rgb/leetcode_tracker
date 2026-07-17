# Last updated: 17/07/2026, 15:03:54
class Solution:
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if len(s) < total_len:
            return []

        # Store frequency of words
        target = {}

        for word in words:
            target[word] = target.get(word, 0) + 1

        result = []

        # Try every possible starting offset
        for i in range(word_len):

            left = i
            right = i
            current = {}
            count = 0

            while right + word_len <= len(s):

                # Take next word
                word = s[right:right + word_len]
                right += word_len

                if word in target:

                    current[word] = current.get(word, 0) + 1
                    count += 1

                    # Remove extra occurrences
                    while current[word] > target[word]:
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                    # If window contains all words
                    if count == word_count:
                        result.append(left)

                        # Move left for next possible answer
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    # Reset window
                    current.clear()
                    count = 0
                    left = right

        return result
        