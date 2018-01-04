def tied(game_board):
    """ checks to see if there's a tie
        returns True if there are no moves left
        returns False if there are moves left
    """
    for row in game_board:
        for element in row:
            if element.isdigit():
                return False
    return True   # check every element first!

def won(board):
    """ checks to see if someone won
        returns True if there are 3 in a row
        returns False if no 3-in-a-rows
    """
    # check horizontal - TODO
    # check vertical - TODO
    # check diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        return True
    # no one has won if none of these if statements were True
    return False

if __name__ == "__main__":
    # step 0: make a board
    board = [['1','2','3'],
             ['4','5','6'],
             ['7','8','9']]
    # step 1: take turns until tie or win
    # boolean approach (True = X, False = O)
    is_X_turn = True
    while not tied(board) and not won(board):
        # NOTE: currently this does not display the board
        # step 2: pick a spot
        if is_X_turn:
            player = 'X'
        else:
            player = 'O'
        move = int(raw_input(player+"'s Move:"))-1

        # step 3: move there
        row = move/len(board)
        col = move%len(board[row])
        board[row][col] = player

        # step 4: switch players
        is_X_turn = not is_X_turn
