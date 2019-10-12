class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0), (1,-1), (0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    if (r<rows and r>=0) and (c<cols and c>=0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                # Rule 1 or Rule 3
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
                # Rule 4
                elif board[row][col] == 0 and live_neighbors == 3:
                    # Signifies the cell is now live but was originally dead
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0



"""
本题布局上只有0和1出现，但同时也要知道并不是用单个比特表示，因此可以考虑用其它数字来标记，由活的细胞变成死的可以标记为-1，这样用单元格的绝对值就可以获取变化之前的细胞是死的还是活的
同时死的细胞变成活的，那么一定可用2来标记。遍历完后，则可以再将这些标记转化为0和1
"""