from functools import cache

def print_board(board_string):
    for i in range(0, 9):
        print(f"{board_string[i] if board_string[i] != "." else i} {"\n" if i in {2, 5, 8} else "| "}", end="")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_board("XØXØ...XX")
