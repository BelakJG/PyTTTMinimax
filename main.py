from functools import cache

player = "X"

def print_board(board_string):
    for i in range(9):
        print(f"{board_string[i] if board_string[i] != "." else i} {"\n" if i in {2, 5, 8} else "| "}", end="")

@cache
def check_winner(board_string):
    global player
    #horizontals
    for i in range(0, 7, 3):
        if board_string[0 + i] != "." and (board_string[0 + i] == board_string[1 + i] == board_string[2 + i]):
            return 1 if board_string[0 + i] == player else -1
    #verticals
    for i in range(3):
        if board_string[0 + i] != "." and (board_string[0 + i] == board_string[3 + i] == board_string[6 + i]):
            return 1 if board_string[0 + i] == player else -1
    #diags
    if board_string[0] != "." and (board_string[0] == board_string[4] == board_string[8]):
        return 1 if board_string[0] == player else -1
    if board_string[6] != "." and (board_string[6] == board_string[4] == board_string[2]):
        return 1 if board_string[6] == player else -1
    #check draw
    if "." not in board_string:
        return 0
    #no winner
    return None

@cache
def minimax(current_turn, board_string):
    global player
    winner = check_winner(board_string)
    if winner is not None:
        return winner

    possible_moves = []
    for i in range(9):
        if board_string[i] == ".":
            new_string = board_string[:i] + current_turn + board_string[i + 1:]
            possible_moves.append(new_string)
    if not possible_moves:
        return 0

    move_scores = []
    for string in possible_moves:
        move_scores.append(minimax("O" if current_turn == "X" else "X", string))

    if current_turn == player:
        return max(move_scores)
    else:
        return min(move_scores)

def find_best(board_string):
    global player
    moves = []
    for i in range(9):
        if board_string[i] == ".":
            new_string = board_string[:i] + player + board_string[i + 1:]
            moves.append(new_string)

    scores = []
    for move in moves:
        scores.append(minimax("O" if player == "X" else "X", move))
    return moves[scores.index(max(scores))]

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    string = "........."
    player = "X" if int(input("Are player 1 or 2?: ")) == 1 else "O"
    if player == "O":
        print_board(string)
        index = int(input("What position did your opponent play?: "))
        string = string[:index] + ("O" if player == "X" else "X") + string[index + 1:]
    while string.count(".") > 0:
        print("Your best move is:")
        string = find_best(string)
        print_board(string)
        index = int(input("What position did your opponent play?: "))
        string = string[:index] + ("O" if player == "X" else "X") + string[index + 1:]
        print("\n" * 25)
