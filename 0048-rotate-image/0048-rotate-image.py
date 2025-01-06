#https://www.youtube.com/watch?v=Z0R2u6gd3GU&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=30

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        print("n:", n)

        #Reverse the rows
        matrix.reverse()
        print(matrix)

        #Transpose the matrix
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
