#brute force solution - iterating each time for each possibility: row, col, square 
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #check sub boxes
        for r in range(3):
            for c in range(3):
                nums = []
                for i in range(3):
                    for j in range(3):
                        if board[r*3+i][c*3+j] == ".":
                            continue
                        if board[r*3+i][c*3+j] in nums:
                            return False
                        else:
                            nums.append(board[r*3+i][c*3+j])
        #check rows
        for row in range(9):
            nums = []
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in nums:
                    return False
                else:
                    nums.append(board[row][i])
        
        #check columns
        for col in range(9):
            nums = []
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in nums:
                    return False
                else:
                    nums.append(board[i][col])
        #if not returned false 
        return True