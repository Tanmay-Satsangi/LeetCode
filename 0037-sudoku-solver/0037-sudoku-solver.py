class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':

                    for val in range(1, 10):
                        val = str(val)

                        if self.isValid(board, row, col, val):
                            board[row][col] = val
                        
                            if self.solveSudoku(board) == True:
                                return True
                            else:
                                board[row][col] = '.'
                                # return False

                    return False
        return True            

    def isValid(self, board, r, c, val):
        for i in range(9):
            if board[i][c] == val:     #Check in column
                return False
            if board[r][i] == val:      #Check in row
                return False
            #Check in correspoding (3 * 3) matrix
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == val:
                return False
            
        return True

        

        