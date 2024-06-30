class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    if self.isValid(board, row, col) == False:
                        return False

        return True

    def isValid(self, board, row, col):
        for i in range(9):
            #check for row
            if i != col and board[row][i] == board[row][col]:
                return False
            #check for column
            if i != row and board[i][col] == board[row][col]:
                return False

            #check in 3 * 3 matrix
            if row != (3 * (row // 3) + i // 3) and col != (col // 3 + i % 3) and board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == board[row][col]:
                return False

        return True

