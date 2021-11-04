"""
Name: Steve Ford
lab10.py
"""


def build_board():
    # function which resets the board to default values
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def display_board(board):
    # prints the board to console with some formatting
    print(board[0], " | ", board[1], " | ", board[2])
    print("--------------")
    print(board[3], " | ", board[4], " | ", board[5])
    print("--------------")
    print(board[6], " | ", board[7], " | ", board[8])


def is_legal(board, pos):
    # determines if a move is legal
    if board[pos] == "x" or board[pos] == "o":
        return False
    return True


def is_over(board, token):
    # checks for lateral victories for the active player token
    for length in range(0, 9, 3):
        for i in range(length, length+3):
            if board[i] != token:
                break
            if i == length + 2 and board[i] == token:
                return True

    # checks for vertical victories for active player token
    for drop in range(0, 3):
        for i in range(drop, drop + 7, 3):
            if board[i] != token:
                break
            if i == drop + 6 and board[i] == token:
                return True

    # checks for diagonal victories for active player token
    if board[0] == token and board[4] == token and board[8] == token:
        return True
    if board[2] == token and board[4] == token and board[6] == token:
        return True

    return False


def play_game():
    # initializes board values, display, turn counter, and which player is active
    board = build_board()
    display_board(board)
    turn_tracker = 0
    token = "x"
    while not is_over(board, token):

        # checks for a tie
        if turn_tracker == 9:
            print("It's a tie!")
            input()
            play_game()

        # determines who the active player is and what their board token is
        player = str((turn_tracker % 2) + 1)
        if player == "1":
            token = "x"
        else:
            token = "o"

        # input that asks for the correct player to select a board spot with some formatting
        position = eval(input("Player " + player + " mark a spot")) - 1

        # checks to see if a move is legal; if legal increase turn tracker/change players and update board
        if is_legal(board, position):
            board[position] = token
            turn_tracker += 1
            display_board(board)
        else:
            print("Invalid move!")

    # if loop is broken via a victory
    print("The " + token + "'s win!")
    input()
    play_game()


def main():
    play_game()


main()
