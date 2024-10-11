import game_board

def play_connect_four():
    '''
    Main function that starts the game
    '''
    rows = int(input()) 
    cols = int(input())
    game = game_board.ConnectFourGame(rows, cols)
    action = input()
    valid_letters = {'S', 'T', 'V', 'W', 'X', 'Y', 'Z', ' '}
    last = 0
    landed = 0
    match = 0

    if action == "EMPTY":
        game.print_board(last, landed, match) 

    if action == "CONTENTS":
        row = 0
        while row < rows:
            contents = input()
            if len(contents) != cols or not all(item in valid_letters for item in contents):
                print("Invalid input")
                break
            col = 0
            for i in range(cols):
                game.board[row][col] = contents[i]
                col += 1
            row += 1

        if game.remove_matches(last, landed, match):
            game.print_board(last, landed, match)
            print("Game Over")
            exit()

    while True:
        user = input().split()
        if "Q" in user:
            exit()

        if user[0] == "F":
            col = int(user[1]) - 1
            letter = user[2:]

            if len(letter) != 3 or not all(item in valid_letters for item in letter):
                print("Invalid input. You must enter exactly 3 letters.")
                break

            temp = letter[0]
            letter[0] = letter[2]
            letter[2] = temp
            letter[0] = "[" + letter[0] + "]"
            letter[1] = "[" + letter[1] + "]"
            letter[2] = "[" + letter[2] + "]"

            landed = 0
            last = 0
            count, row = game.create_piece(letter, col)
            game.print_board(last, landed, match)
            frozen = 0

            while True:
                if frozen == 1:
                    break
                move = input()
                if move == "" and count == 3:
                    row, frozen, last, landed = game.move_down(col, letter, row, frozen, last, landed)
                if move == "" and count == 2:
                    count, row = game.drop_third(col, letter)
                if move == "" and count == 1:
                    count, row = game.drop_second(col, letter)
                if move == "R":
                    letter = game.rotate_jewel(row, col, letter)
                if move == ">":
                    col = game.move_right(row, col, letter, cols)
                if move == "<":
                    col = game.move_left(row, col, letter, cols)
                if move == "Q":
                    exit()
                game.print_board(last, landed, match)

            if game.remove_matches(last, landed, match):
                game.print_board(last, landed, match)
                print("Game Over")
                break

if __name__ == "__main__":
    play_connect_four()
