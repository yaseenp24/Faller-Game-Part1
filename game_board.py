
class ConnectFourGame:
    def __init__(self, rows, cols):
        '''
        Initialize connect four game object with the specified
        number of rows and columns 
        '''
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]

    def print_board(self, last, landed, match):
        '''
        Prints current state of the board
        ''' 
        # Prints **
        if match == 1:
            for row in self.board:
                print('|', end='')
                for cell in row:
                    if cell[0] == "*":
                        print(cell, end='')
                    elif cell != " ":
                        print(" " + cell + " ", end='')
                    else:
                        print("   ", end='')
                print('|', end='')
                print()
            print(" ", end='')
            for _ in range(len(self.board[0])):
                print("---", end='')
            print(" ")
        # Prints with ||
        elif landed == 1:
            for row in self.board:
                print('|', end='')
                for cell in row:
                    if cell[0] == "|":
                        print(cell, end='')
                    elif cell != " ":
                        print(" " + cell + " ", end='')
                    else:
                        print("   ", end='')
                print('|', end='')
                print()
            print(" ", end='')
            for _ in range(len(self.board[0])):
                print("---", end='')
            print(" ")
            landed = 0

        # Prints frozen
        elif last == 1:
            for row in self.board:
                print('|', end='')
                for cell in row:
                    if cell != " ":
                        print(" " + cell + " ", end='')
                    else:
                        print("   ", end='')
                print('|', end='')
                print()
            print(" ", end='')
            for _ in range(len(self.board[0])):
                print("---", end='')
            print(" ")
        else:
            # Prints []
            for row in self.board:
                print('|', end='')
                for cell in row:
                    if cell[0] == "[":
                        print(cell, end='')
                    elif cell != " ":
                        print(" " + cell + " ", end='')
                    else:
                        print("   ", end='')
                print('|', end='')
                print()

            print(" ", end='')
            for _ in range(len(self.board[0])):
                print("---", end='')
            print(" ")

    def create_piece(self, jewels, col):
        '''
        Creates a new jewel and palces it in the specified column
        '''
        if self.board[0][col] == " ":
            self.board[0][col] = jewels[0]
            row = 0
        else:
            print("Game Over")
            exit()
        count = 1
        return count, row

    def drop_second(self, col, jewels):
        '''
        Drops the second jewel into the specified column
        '''
        if self.board[1][col] == " ":
            self.board[1][col] = jewels[0]
            self.board[0][col] = jewels[1]
            row = 1
        else:
            print("Game Over")
            exit()
        count = 2
        return count, row

    def drop_third(self, col, jewels):
        '''
        Drops the third jewel into the specified column
        '''
        if self.board[2][col] == " ":
            self.board[2][col] = jewels[0]
            self.board[1][col] = jewels[1]
            self.board[0][col] = jewels[2]
            row = 2
        else:
            print("Game Over")
            exit()
        count = 3
        return count, row

    def move_down(self, col, jewels, row, frozen, last, landed):
        '''
        Shifts all three jewels down
        '''
        if row + 2 == self.rows:
            jewels[0] = jewels[0].replace("[", "|")
            jewels[0] = jewels[0].replace("]", "|")
            jewels[1] = jewels[1].replace("[", "|")
            jewels[1] = jewels[1].replace("]", "|")
            jewels[2] = jewels[2].replace("[", "|")
            jewels[2] = jewels[2].replace("]", "|")
            landed = 1
            last = 0
        if row + 1 == self.rows:
            jewels[0] = jewels[0].replace("|", "")
            jewels[0] = jewels[0].replace("|", "")
            jewels[1] = jewels[1].replace("|", "")
            jewels[1] = jewels[1].replace("|", "")
            jewels[2] = jewels[2].replace("|", "")
            jewels[2] = jewels[2].replace("|", "")
            self.board[row][col] = jewels[0]
            self.board[row - 1][col] = jewels[1]
            self.board[row - 2][col] = jewels[2]
            frozen = 1
            last = 1
        elif self.board[row + 1][col] != " ":
            jewels[0] = jewels[0].replace("[", "")
            jewels[0] = jewels[0].replace("]", "")
            jewels[1] = jewels[1].replace("[", "")
            jewels[1] = jewels[1].replace("]", "")
            jewels[2] = jewels[2].replace("[", "")
            jewels[2] = jewels[2].replace("]", "")
            self.board[row][col] = jewels[0]
            self.board[row - 1][col] = jewels[1]
            self.board[row - 2][col] = jewels[2]
            frozen = 1
            last = 1

        else:
            if self.board[row + 1][col] == " ":
                self.board[row + 1][col] = jewels[0]
                self.board[row][col] = jewels[1]
                self.board[row - 1][col] = jewels[2]
                self.board[row - 2][col] = " "
                row = row + 1
        return row, frozen, last, landed

    def rotate_jewel(self, row, col, jewels):
        '''
        Rotates the jewels
        '''
        if row == 0:
            self.board[row][col] = jewels[1]
        if row == 1:
            self.board[row][col] = jewels[1]
            self.board[row - 1][col] = jewels[2]
        if row > 1:
            temp = self.board[row][col]
            self.board[row][col] = self.board[row - 1][col]
            self.board[row - 1][col] = self.board[row - 2][col]
            self.board[row - 2][col] = temp
        temp = jewels[0]
        jewels[0] = jewels[1]
        jewels[1] = jewels[2]
        jewels[2] = temp
        return jewels

    def move_right(self, row, col, jewels, cols):
        '''
        Moves all three jewels to the right
        '''
        if row == 0:
            if col + 1 <= self.cols - 1 and self.board[row][col + 1] == " ":
                self.board[row][col + 1] = self.board[row][col]
                self.board[row][col] = " "
                col = col + 1
        if row == 1:
            if col + 1 <= self.cols - 1 and self.board[row][col + 1] == " ":
                self.board[row][col + 1] = self.board[row][col]
                self.board[row - 1][col + 1] = self.board[row - 1][col]
                self.board[row][col] = " "
                self.board[row - 1][col] = " "
                col = col + 1
        if row > 1:
            if col + 1 <= self.cols - 1 and self.board[row][col + 1] == " ":
                self.board[row][col + 1] = self.board[row][col]
                self.board[row - 1][col + 1] = self.board[row - 1][col]
                self.board[row - 2][col + 1] = self.board[row - 2][col]
                self.board[row][col] = " "
                self.board[row - 1][col] = " "
                self.board[row - 2][col] = " "
                col = col + 1
            else:
                print()
        return col

    def move_left(self, row, col, jewels, cols):
        '''
        Moves all three jewels to the left
        '''
        if row == 0:
            if col > 0 and self.board[row][col - 1] == " ":
                self.board[row][col - 1] = self.board[row][col]
                self.board[row][col] = " "
                col = col - 1
        if row == 1:
            if col > 0 and self.board[row][col - 1] == " ":
                self.board[row][col - 1] = self.board[row][col]
                self.board[row - 1][col - 1] = self.board[row - 1][col]
                self.board[row][col] = " "
                self.board[row - 1][col] = " "
                col = col - 1
        if row > 1:
            if col > 0 and self.board[row][col - 1] == " ":
                self.board[row][col - 1] = self.board[row][col]
                self.board[row - 1][col - 1] = self.board[row - 1][col]
                self.board[row - 2][col - 1] = self.board[row - 2][col]
                self.board[row][col] = " "
                self.board[row - 1][col] = " "
                self.board[row - 2][col] = " "
                col = col - 1
        return col

    def move_down_as_far_as_possible(self):
        '''
        Moves the jewels down as far as possible to fill in all gaps
        that may exist when entering contents of the board
        '''
        moved_down = True
        while moved_down:
            moved_down = False
            for j in range(len(self.board[0])):
                for i in range(len(self.board) - 1, 0, -1):
                    if self.board[i][j] == ' ' and self.board[i - 1][j] != ' ':
                        self.board[i][j] = self.board[i - 1][j]
                        self.board[i - 1][j] = ' '
                        moved_down = True

    def remove_matches(self, last, landed, match):
        '''
        Locates matches and puts * around them, then turns them into ' '
        '''
        while True:
            self.move_down_as_far_as_possible()

            matches = set()

            for i in range(len(self.board)):
                for j in range(len(self.board[0]) - 2):
                    if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] and self.board[i][j] != ' ':
                        matches.add((i, j))
                        matches.add((i, j + 1))
                        matches.add((i, j + 2))

            for i in range(len(self.board) - 2):
                for j in range(len(self.board[0])):
                    if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] and self.board[i][j] != ' ':
                        matches.add((i, j))
                        matches.add((i + 1, j))
                        matches.add((i + 2, j))

            for i in range(len(self.board) - 2):
                for j in range(len(self.board[0]) - 2):
                    if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] and self.board[i][j] != ' ':
                        matches.add((i, j))
                        matches.add((i + 1, j + 1))
                        matches.add((i + 2, j + 2))

            for i in range(2, len(self.board)):
                for j in range(len(self.board[0]) - 2):
                    if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] and self.board[i][j] != ' ':
                        matches.add((i, j))
                        matches.add((i - 1, j + 1))
                        matches.add((i - 2, j + 2))

            if not matches:
                break

            for i, j in matches:
                self.board[i][j] = '*' + self.board[i][j] + '*'
                match = 1
            self.print_board(last, landed, match)
            print()
            match = 0

            for i, j in matches:
                self.board[i][j] = ' '
        self.print_board(last, landed, match)
    
