class Solution:
    # space complexity O(m*n)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row_flags = [False] * m
        col_flags = [False] * n
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    # set row flag
                    row_flags[r] = True
                    # set col flag
                    col_flags[c] = True

        for r in range(m):
            if row_flags[r]:
                matrix[r] = [0] * n
        for c in range(n):
            if col_flags[c]:
                for i in range(m):
                    matrix[i][c] = 0




