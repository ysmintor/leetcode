class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Typically use space to exchange time
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == '.':
                    continue
                if cell in row[r]:
                    return False
                if cell in col[c]:
                    return False

                g = r // 3 * 3 + c // 3
                if cell in grid[g]:
                    return False

                # first time appear in grid, col, row, then add it
                grid[g].add(cell)
                row[r].add(cell)
                col[c].add(cell)
        return True