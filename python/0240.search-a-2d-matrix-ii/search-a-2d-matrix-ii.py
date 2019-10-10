class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # obviously empty matrix should return False result
        if not matrix or not matrix[0]:
            return False

        width, height = len(matrix[0]), len(matrix)
        row, col = height - 1, 0
        while row >=0 and col < width:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                # find the target
                return True

                # search out of bounds, target not in matrix
        return False