# Last updated: 17/07/2026, 15:03:32
class Solution:
    def rotate(self, matrix):
        
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()
        