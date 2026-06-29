from functools import cache

def print_board(board_string):
    for i in range(9):
        print(f"{board_string[i] if board_string[i] != "." else i} {"\n" if i in {2, 5, 8} else "| "}", end="")

@cache
def check_winner(board_string):
    #horizontals
    for i in range(0, 7, 3):
        if board_string[0 + i] != "." and (board_string[0 + i] == board_string[1 + i] == board_string[2 + i]):
            return 1 if board_string[0 + i] == "X" else -1
    #verticals
    for i in range(3):
        if board_string[0 + i] != "." and (board_string[0 + i] == board_string[3 + i] == board_string[6 + i]):
            return 1 if board_string[0 + i] == "X" else -1
    #diags
    if board_string[0] != "." and (board_string[0] == board_string[4] == board_string[8]):
        return 1 if board_string[0] == "X" else -1
    if board_string[6] != "." and (board_string[6] == board_string[4] == board_string[2]):
        return 1 if board_string[6] == "X" else -1
    #check draw
    if "." not in board_string:
        return 0
    #no winner, game still going
    return None

@cache
def minimax(turn, board_string):
    winner = check_winner(board_string)
    if winner is not None:
        return winner

    possible_moves = []
    for i in range(9):
        if board_string[i] == ".":
            possible_moves.append(board_string[:i] + turn + board_string[i + 1:])

    move_scores = []
    for string in possible_moves:
        score = minimax("O" if turn == "X" else "X", string)
        if turn == "X":
            if score == 1:
                return 1
        elif turn == "O":
            if score == -1:
                return -1
        move_scores.append(score)

    return max(move_scores) if turn == "X" else min(move_scores)

def find_best(turn, board_string):
    possible_moves = []
    for i in range(9):
        if board_string[i] == ".":
            possible_moves.append(board_string[:i] + turn + board_string[i + 1:])

    move_scores = []
    for string in possible_moves:
        move_scores.append(minimax("O" if turn == "X" else "X", string))

    return possible_moves[move_scores.index(max(move_scores) if turn == "X" else min(move_scores))]


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    string = "........."
    turn = "X" if input("Are you player 1 or 2?: ") == "1" else "O"
    if turn == "O":
        print_board(string)
        move_index = int(input("What position did player X play?: "))
        string = string[:move_index] + "X" + string[move_index + 1:]
    while string.count(".") > 0:
        print_board(string)
        print("\nYour best move is:")
        string = find_best(turn, string)
        print_board(string)
        if check_winner(string) is not None:
            break
        turn = "X" if turn == "O" else "O"

        move_index = int(input(f"What position did player {turn} play?: "))
        string = string[:move_index] + turn + string[move_index + 1:]
        turn = "X" if turn == "O" else "O"
        print("\n")
        if check_winner(string) is not None:
            break

    winner = check_winner(string)
    print("Tie! No one wins!" if winner == 0 else f"Player {turn} wins!")
    print_board(string)
