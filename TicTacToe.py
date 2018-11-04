def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" ", row[0], " | ", row[1], " | ", row[2])
        if i != 2:
            print("-----------------")
    print("\n")


def show_rules():
    rules_board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    rules = """
    This is a game of Tic Tac Toe.
    Take it in turns to fill in an empty square with your mark, which is either 'x' or 'o', until all someone wins.
    To win, you simply need to get a line of your mark, vertical, horizontal, or diagonal.

    To specfiy where you want your mark, you need only give the number of the square.
    The numbers are shown below. If you forget, just input "rules" or "r" instead of a number and you'll
    be given this explanation plus the print out below again.
    """
    print(rules)
    print_board(rules_board)


def check_valid_move(num, turn, board):
    input_mapping = {
        "1": (0,0), "2": (0,1), "3": (0,2), 
        "4": (1,0), "5": (1,1), "6": (1,2),
        "7": (2,0), "8": (2,1), "9": (2,2)
        }

    if num == "r" or num == "rules":
        show_rules()
    elif int(num) not in range(0,10):
        print('This is not a legal move, if you wish to see the rules again just type "rules" or "r"')
        return False
    elif board[input_mapping[num][0]][input_mapping[num][1]] != " ":
        print('This square is already occupied, please select another')
        return False
    else:
        board[input_mapping[num][0]][input_mapping[num][1]] = turn
        return True


def next_turn(turn, board):
    if turn == "x":
        turn = "o"
    else:
        turn = "x" 

    print(f"It's your turn now {turn}")
    print_board(board)

    return turn


def is_game_complete(board):
    # check rows
    for row in board:
        if row[0] != " " and (row[0] == row[1] == row[2]):
            return True
    
    # check columns
    for i in range(0,3):
        if board[0][i] != " " and (board[0][i] == board[1][i] == board[2][i]):
            return True

    # check diagonals
    if board[1][1] != " " and ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])):
        return True

    return False


def is_game_stalemate(board):
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == " ":
                return False

    return True


def print_winner(turn):
    print(f"The winner is {turn}!")


def play(board, turn):
    print_board(board)
    print("Now, let's start! The first to play is 'x'")

    while True:
        num = input(f"Which position '{turn}'?' ")

        if check_valid_move(num, turn, board):
            if is_game_complete(board):
                print_board(board)
                print_winner(turn)
                break
            elif is_game_stalemate(board):
                print_board(board)
                print("Looks like it's a draw..")
                break
            else:
                turn = next_turn(turn, board)


def play_again():
    while True: 
        answer = input("Fancy another game (yes/no)? ")

        if answer.lower().startswith("y"):
            return True
        elif answer.lower().startswith("n"):
            return False
        else:
            print("\nI don't understand this answer\n")


def main():
    show_rules()

    continue_play = True

    while continue_play:
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        turn = "x"

        play(board, turn)

        continue_play = play_again()


if __name__ == "__main__":
    main()