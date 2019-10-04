from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return

        n, m = len(board), len(board[0])
        # get four edges all coordination
        q = [ij for k in range(max(n,m)) for ij in ((0, k), (n-1, k), (k, 0), (k, m-1))]
        while q:
            i, j = q.pop()
            # DFS all O connect to bounds which is also O
            if 0 <= i < n and 0 <= j < m and board[i][j] == 'O':
                board[i][j] = 'W'
                q += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
        # 这里想不通为什么必须用 board[:]来接收
        board[:] = [['XO'[c == 'W'] for c in row] for row in board]
        print(board)

if __name__ == '__main__':
    solution = Solution()
    solution.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])