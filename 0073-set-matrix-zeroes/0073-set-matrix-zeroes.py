class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_row = len(matrix)
        len_col = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        # Track zeroes
        for r in range(len_row):
            for c in range(len_col):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_has_zero = True
                    if c == 0:
                        first_col_has_zero = True
                    matrix[r][0] = matrix[0][c] = 0

        # Iterate the rows and column from (1, 1)
        for r in range(1, len_row):
            for c in range(1, len_col):
                if  matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_has_zero:
            for c in range(len_col):
                matrix[0][c] = 0

        if first_col_has_zero:
            for r in range(len_row):
                matrix[r][0] = 0

        