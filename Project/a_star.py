import copy
from heuristic import *

class Cor: #For colors, pretty self intuitive
    RESET = '\033[0m'
    VERMELHO = '\033[91m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'

class Board_A: #The Board contains the games grid and a method to output the grid to the stdout
    def __init__(self):
        self.Grid = [['X' for _ in range(7)] for _ in range(6)] # Initializes the Boards Grid with empty spaces

    def print_grid(self):  # Prints the Grid, pretty self intuitive
        for i in range(6):
            for j in range(7):
                if(self.Grid[i][j] == 'R'):
                    print(Cor.VERMELHO + self.Grid[i][j] + Cor.RESET, end=" ")
                if(self.Grid[i][j] == 'B'):
                    print(Cor.AZUL + self.Grid[i][j] + Cor.RESET, end=" ")
                if(self.Grid[i][j] == 'X'):
                    print(self.Grid[i][j], end=" ")    
            print()

def Make_Move(Return_Board, index, color): #Computes the move, inputed by the index argument, by the player indentified by the color argument
    for i in range(5, -1, -1):
        if(Return_Board.Grid[i][index-1] == 'X'):
            Return_Board.Grid[i][index-1] = color
            return
    print("You should not be here")

def A_Star(visited, playerColor, game, heuristic_value):
    greatest_value = 0
    move_position = 0
    for i in range(7):
        if (visited[i]):
            a_star_board = Board_A() 
            lista_temp = copy.deepcopy(game.Grid)
            setattr(a_star_board, 'Grid', lista_temp) #For the last three lines, because of python refence bullshittery, I had to make a deepcopy of the Board.Grid. Right now either the value is passed by reference or not doesn't make a difference but in order to no fuck up the code in the future I made it this way. Any other solutions are welcome since this looks ugly and must be pretty inneficient :3
            Make_Move(a_star_board, i, playerColor)
            value_temp = Total_Value(a_star_board)
            if(Is_Red(playerColor)):
                 if(value_temp > heuristic_value):
                     greatest_value = value_temp
                     move_position = i + 1
            else:
                if(value_temp < heuristic_value):
                     greatest_value = value_temp
                     move_position = i + 1
            value_temp = 0            
    Make_Move(game, move_position, playerColor)    
    return greatest_value           
