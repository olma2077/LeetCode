class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check lines
        for i in board:
            for j in range(1, 10):
                if i.count(str(j)) > 1:
                    return False
        
        # Check columns
        for i in range(9):
            col = [line[i] for line in board]
            for j in range(1, 10):
                if col.count(str(j)) > 1:
                    return False
        
        # Check boxes
        for i in range(3):
            for j in range(3):
                block = [item for lines in board[j*3:j*3+3] for item in lines[i*3:i*3+3]]
                for k in range(1, 10):
                    if block.count(str(k)) > 1:
                        return False
        
        # Board valid
        return True
