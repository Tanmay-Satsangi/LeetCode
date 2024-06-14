class Solution:
    def searchMatrix(self, arr: List[List[int]], target: int) -> bool:
        #Treat 2D array as 1D array.

        row = len(arr)
        col = len(arr[0])

        low = 0
        high = row * col - 1

        while (low <= high):
            mid = (low + high) // 2

            # To convert the 1D array index into 2D array index.
            # 1st element of each row is always multiple of column
            # and column element is modulus of column i.e. how much we have to go extra from 1st element of row.
            mid_element = arr[mid // col][mid % col]

            if mid_element == target:
                return True

            if mid_element < target:
                low = mid + 1

            else:
                high = mid - 1

        return False