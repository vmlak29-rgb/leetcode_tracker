# Last updated: 17/07/2026, 15:03:27
class Solution:
    def totalNQueens(self, n):

        count = [0]

        cols = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        def backtrack(row):

            # All queens placed
            if row == n:
                count[0] += 1
                return

            for col in range(n):

                # Check attacks
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Go to next row
                backtrack(row + 1)

                # Remove queen (backtrack)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return count[0]