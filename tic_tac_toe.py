row_A = [' ',' ','X']
row_B = ['X','O','O']
row_C = ['X',' ',' ']

board = [row_A, row_B, row_C]

# row_A[0] = 'O'
board[0][0] = 'O'
board[1][1] = 'X'

for row in board:
    print row
