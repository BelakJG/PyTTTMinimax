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
    #no winner
    return 0



# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    string = "XO..X.OOX"
    print_board(string)
    print(check_winner(string))
