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
        if(Return_Board.Grid[i][index] == 'X'):
            Return_Board.Grid[i][index] = color
            return
    print("You should not be here")

def Find_value(playerColor, value_temp):
    position = -1
    if(playerColor == 'R'):
        greatest_value = -513
        for i in range(7):
            if(value_temp[i] > greatest_value):
                greatest_value = value_temp[i]
                position = i
    elif(playerColor == 'B'):
        greatest_value = 513
        for i in range(7):
            if(value_temp[i] < greatest_value):
                greatest_value = value_temp[i]
                position = i
    #print(position)
    return position

def A_Star(visited, playerColor, game, heuristic_value):
    plusvalue = 0
    value_temp_R = [-513]*7
    value_temp_B = [513]*7
    for i in range(7):
        if (visited[i]):
            a_star_board = Board_A() 
            lista_temp = copy.deepcopy(game.Grid)
            setattr(a_star_board, 'Grid', lista_temp) 
            Make_Move(a_star_board, i, playerColor)
            if(playerColor == 'R'):
                value_temp_R[i] = Total_Value(a_star_board)
                #print("Valor na (" + str(i) + " " + str(value_temp_R[i]) + ")")
            elif(playerColor == 'B'):
                value_temp_B[i] = Total_Value(a_star_board)
                #print("Valor na (" + str(i) + " " + str(value_temp_B[i]) + ")")
    if(playerColor == 'R'):
        move_position = Find_value(playerColor, value_temp_R)
    elif(playerColor == 'B'):
        move_position = Find_value(playerColor, value_temp_B)
    Make_Move(game, move_position, playerColor)
    if(playerColor == 'R'):  
        return value_temp_R[move_position] + 16
    else:
        return value_temp_B[move_position] - 16     
