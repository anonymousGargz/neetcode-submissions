class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #top row
        for i in range(0,9,3):
            for j in range(0, 9, 3):
                currentBox=set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l]=='.':
                            continue
                        
                        if board[k][l] in currentBox:
                            return False
                        currentBox.add(board[k][l])
        
        for i in range(0, 9):
            curRow=set()
            for j in range(0,9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in curRow:
                    return False
                curRow.add(board[i][j])
        
        for j in range(0, 9):
            curCol=set()
            for i in range(0,9):

                if board[i][j]=='.':
                    continue
                if board[i][j] in curCol:
                    return False
                curCol.add(board[i][j])
        return True


        