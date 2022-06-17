from socket import getnameinfo
from numpy import row_stack

rows = int(input("Give the number of rows:"))  
cols = int(input("Give the number of columns:"))  
  
class gameLife:
        
    def gameOfLife(self, board: list[list[int]]) -> None:
        
        row, col = len(board), len(board[0])
        
        def countNeighbour(r, c):
            neighbour = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i == r and j == c) or i < 0 or j < 0 or i == row or j == col:
                        continue
                    if board[i][j] in [1, 2]:
                        neighbour += 1
            return neighbour
        
        for r in range(row):
            for c in range(col):
                neighbours = countNeighbour(r, c)
                if board[r][c]:
                    if neighbours in [2, 3]:
                        board[r][c] = 3
                elif neighbours == 3:
                    board[r][c] = 2

        for r in range(row):
            for c in range(col):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1
                    
        
        