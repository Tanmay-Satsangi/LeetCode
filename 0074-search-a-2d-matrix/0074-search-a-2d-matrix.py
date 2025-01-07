class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_row = len(matrix)
        len_col = len(matrix[0])

        low = 0
        high = (len_row * len_col) - 1

        while (low <= high):
            mid = (low + high) // 2

            # To convert the 1D array index into 2D array index.
            # 1st element of each row is always multiple of column
            # and column element is modulus of column i.e. how much we have to go extra from 1st element of row.
            mid_element = matrix[mid // len_col][mid % len_col]

            if mid_element == target:
                return True

            elif mid_element < target:
                low = mid + 1

            else:
                high = mid - 1


        return False