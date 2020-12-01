import msvcrt
import os

# variables to define play area
global boardX 
boardX = 40
global boardY 
boardY = 20

class Square(object):
    def __init__(self, positions, size = 1):
        """clockwise from top left"""
        self.positions = [positions, (positions + size), ((positions + size) + (boardX * (size-1))), (positions + (boardX * (size-1)))]

    def __change_pos(self, amount):
        """function to move the square object by a given amount"""
        #print('change:',self.positions)
        # move every corner by  amount
        for i in range(len(self.positions)):
            self.positions[i] += amount

    def move_shape(self):
        """User input function"""
        # gets keyboard input using msvcrt
        direction = ord(msvcrt.getch())
        #print("direction=",direction)
        # have to use ascii codes for this
        if direction == 119:        # w for up
            self.__change_pos((boardX-(boardX*2)))
        elif direction == 97:       # a for left
            self.__change_pos(-1)   
        elif direction == 115:      # s for down
            self.__change_pos(boardX)
        elif direction == 100:      # d for right
            self.__change_pos(1)
        elif direction == 113:      # q for quit
            exit()


class BoardClass(object):
    def __init__(self, fill = '0', border_fill = '#'):
        self.boardX = boardX            # make the board X and Y an
        self.boardY = boardY            # attribute of boardclass
        self.fill = fill                # background will become this char
        self.border_fill = border_fill  # border will become this char
        self.grid = boardX * boardY     # this will be the grid that i print
        self.border_values = self.__make_border() # get border indexes


    def clear_board(self):
        """function to empty the board"""
        self.grid = [self.fill for i in range(0, (self.boardX*self.boardY))]


    def fill_shape(self, shape, fill = '1'):
        """This function fills the space between the edges"""
        for i in range(shape.positions[0], shape.positions[1], 1):
            self.grid[i] = fill
        
        for i in range(shape.positions[3], shape.positions[2], 1):
            self.grid[i] = fill

        for i in range(shape.positions[0], shape.positions[3], self.boardX):
            self.grid[i] = fill

        for i in range(shape.positions[1], shape.positions[2], self.boardX):
            self.grid[i-1] = fill


    def __make_border(self):
        """Get the values that will become the border"""
        border_values_list = []
        for i in range(self.grid):
            if i < boardX:
                border_values_list.append(i)
            if i >= boardX * (boardY - 1):
                border_values_list.append(i)
            if i % boardX == 0:
                border_values_list.append(i)
                border_values_list.append(i-1)
        return border_values_list


    def draw_board(self):
        """print the board"""
        #self.draw_border('#')
        #print(self.border_values)
        for i in self.border_values:
            self.grid[i] = self.border_fill
        for i, j in enumerate(self.grid):
            if (i+1) % boardX == 0 and i != 0:
                print(j)
            else:
                print(j, end='')

def draw():
    os.system('cls')
    board.clear_board()
    board.fill_shape(shape1)
    board.draw_board()

#------------------------------------MAIN---------------------------------------
board = BoardClass(' ', '#')
shape1 = Square(0, 5)

while True:
    draw()
    shape1.move_shape()