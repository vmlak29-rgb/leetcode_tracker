# Last updated: 17/07/2026, 15:01:10
class Solution:
    def findWords(self, board, words):
        
        # Trie Node
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.word = None

        # Build Trie
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        result = []
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, node):
            char = board[r][c]

            # If character not in trie path
            if char not in node.children:
                return

            next_node = node.children[char]

            # Word found
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None   # Avoid duplicates

            # Mark visited
            board[r][c] = "#"

            # Explore four directions
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, next_node)

            # Restore character
            board[r][c] = char

        # Start DFS from every cell
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return result