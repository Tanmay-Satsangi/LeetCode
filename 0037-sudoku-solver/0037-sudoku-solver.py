# //MUST REMEMBER: https://stackoverflow.com/questions/44266609/what-is-the-difference-between-str-and-in-python
# With str() function you are changing the number type to String but with "" you just pass the String.

# str(3.14) # 3.14 is a number and your are converting it into String.

# "3.14" is an String value.

#--------------------------------------------------------------------------------------------------

# https://www.youtube.com/watch?v=FWAIf_EVUKE&t=1019s
# TC = O(9 * 9 * N ^ 2)
# SC = O(1)

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                #Find the empty cell
                if board[row][col] == ".":
                    #Call the for loop to check which value is to be assign in the empty cell according to isValid() function.
                    for val in range(1, 10):
                        val = str(val)
                        if self.isValid(board, row, col, val):
                            board[row][col] = val
                    #Before assign value is True then we return True
                            if self.solveSudoku(board) == True:  
                                return True
                    #If before assign value is wrong then we convert filled cell into empty cell.
                            else:
                                board[row][col] = "."
                    
                    #If we cannot fill any value from 1 to 9 in the for loop then, we just false to recently call solveSudoku() function.
                    return False
        return True 
     
    
    #isValid() function is created to check the value forwarded by for loop is doesn't exist in the entire row, entire column and also in corresponding (3 * 3) matrix.            
    def isValid(self, board, r, c, val):
        for i in range(9):
            if board[i][c] == val:     #Check in column (To check for column constant the column)
                return False
            if board[r][i] == val:      #Check in column (To check for row constand the row)
                return False
            #Check in correspoding (3 * 3) matrix
            #3 * (r // 3) return the row number and i // 3 return the specific position at that row
            # Similarly the 3 * (c // 3) return the column number and i // 3 return the specific position at that column
            if board[3 * (r // 3) + i // 3] [3 * (c // 3) + i % 3] == val:
                return False
            
        return True