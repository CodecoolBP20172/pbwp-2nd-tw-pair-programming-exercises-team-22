import os


def game_winner(row, col):
    if board[row][col] == zen:
        winner = False
        t = 0
        while winner != True:
            try:
                if t >= table_size:
                    winner = True
                    if player == True:
                        print("Congrats Player 2 !!!")
                    else:
                        print("Congrats Player 1 !!!")
                    exit()
                if board[row + 1][col - 1] == zen and board[row - 1][col + 1] == zen:
                    t += 50
                    continue
                if board[row - 1][col] == zen and board[row + 1][col] == zen:
                    t += 50
                    continue
                if board[row][col - 1] == zen and board[row][col + 1] == zen:
                    t += 50
                    continue
                if board[row - 1][col - 1] == zen and board[row + 1][col + 1] == zen:
                    t += 50
                    continue
                if board[row - 1][col] == zen and board[row - 2][col] == zen:
                    t += 50
                    continue
                if board[row + 1][col] == zen and board[row + 2][col] == zen:
                    t += 50
                    continue
                if board[row][col + 1] == zen and board[row][col + 2] == zen:
                    t += 50
                    continue
                if board[row][col - 1] == zen and board[row][col - 2] == zen:
                    t += 50
                    continue
                if board[row - 1][col - 1] == zen and board[row - 2][col - 2] == zen:
                    t += 50
                    continue
                if board[row - 1][col + 1] == zen and board[row - 2][col + 2] == zen:
                    t += 50
                    continue
                if board[row + 1][col + 1] == zen and board[row + 2][col + 2] == zen:
                    t += 50
                    continue
                if board[row + 1][col - 1] == zen and board[row + 2][col - 2] == zen:
                    t += 50
                    continue
                else:
                    break
            except IndexError:
                break

#Creating the table with input parameters
def input_board():
    isboard = False
    while isboard != True:
        global board
        global table_size
        board = []
        try:
            table_size = int(input("Table size?(min:3 max:10): "))
        except KeyboardInterrupt:
            print("--->Please don't do that")
            continue
        except ValueError:
            print("Please enter valid integers for row and collum.")
            continue
        if table_size < 3 or table_size > 10:
            print("Wrong number,try again")
            continue
        for x in range(1, table_size + 1):
            board.append(["¤"] * table_size)
        printboard()
        isboard = True

# main funciton
def game():
    global player
    global turn
    global zen
    turn = 0
    if turn % 2 == 0:
        player = True
    else:
        player = False
    winner = False
    input_board()
    while winner != True:
        try:
            choice_col = int(input("Place your sign in col: "))
            choice_row = int(input("Place your sign in row: "))
        except ValueError:
            print("Please enter valid integers for row and collum.")
            continue
        except KeyboardInterrupt:
            print("--->Please don't do that")
            continue
        if (choice_col) > table_size or -1 > (choice_col):
            print(" Longshot")
            continue
        elif (choice_row) > table_size or 0 > (choice_row):
            print("Hold your horses!!!")
            continue
        elif board[choice_row - 1][choice_col - 1] == "X" or board[choice_row - 1][choice_col - 1] == "O":
            print("Already Occupied :(")
            continue
        if player == True:
            zen = "X"
            board[choice_row - 1][choice_col - 1] = zen
            os.system("clear")
            printboard()
            player = False
        else:
            zen = "O"
            board[choice_row - 1][choice_col - 1] = zen
            os.system("clear")
            printboard()
            player = True
        row = choice_row - 1
        col = choice_col - 1
        turn += 1
        draw()
        game_winner(row, col)


def draw():
    if turn == table_size ** 2:
        print("Draw")
        winner = True
        exit()


def printboard():
    for row in board:
        print(" ".join(row))


game()
