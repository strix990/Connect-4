from os import system
# #from a_star impor A_Star
import copy
from a_star import *

class Cor: #For colors, pretty self intuitive
    RESET = '\033[0m'
    VERMELHO = '\033[91m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'

class Board: #The Board contains the games grid and a method to output the grid to the stdout
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

def Take_Int_input(): #Takes input from the stdin and makes sure the input is an int
    while(True):
        try:
            ret = int(input('Choose your move: '))
            return ret
        except ValueError:
            continue

def Make_Move(Return_Board, index, color): #Computes the move, inputed by the index argument, by the player indentified by the color argument
    for i in range(5, -1, -1):
        if(Return_Board.Grid[i][index] == 'X'):
            Return_Board.Grid[i][index] = color
            return
    print("You should not be here")

def Red_moves(Return_Board, red_human_player, heuristic): #Computes Reds movement
    print("Reds Turn")
    print()
    list_possible_moves = [False for _ in range(7)] #List of possible moves, for now its entirety is false
    for i in range(7): #Checks if all columns are filled (in other words if a move is possible), if it is, print the corresponding number above the column
            if(Return_Board.Grid[0][i] == 'X'):
                print(i+1, end= " ")
                list_possible_moves[i] = True #Also sets the possible moves list in its i possition to true
            else:
                print(" ", end = " ") #Else sets it to false just to make sure
                list_possible_moves[i] = False
    if(red_human_player): #Checks if Red player is human or not, the negative case is not currently implemented
        print()
        Return_Board.print_grid()
        if(not(True in list_possible_moves)): #Checks if game is a tie
            print("Game is a Tie")
            exit()
        while(True):
            move = Take_Int_input() - 1#User input, if the move is possible it calls the Make_Move function, if not outputs error and returns to here
            if(move <= 6 and move >= 0):
                if(list_possible_moves[move]):
                    Make_Move(Return_Board, move, 'R')
                    break
        heuristic = Total_Value(Return_Board)
    else:
        print()
        Return_Board.print_grid()
        heuristic = A_Star(list_possible_moves, 'R', Return_Board, heuristic)
        Return_Board.print_grid()
    #system('clear')
    return heuristic

def Blue_moves(Return_Board:Board, blue_human_player, heuristic): #Computes Blues movement
    print("Blues Turn")
    print()
    list_possible_moves = [False for _ in range(7)] #List of possible moves
    for i in range(7): #Checks if all columns are filled (in other words if a move is possible), if it is, print the corresponding number above the column
            if(Return_Board.Grid[0][i] == 'X'):
                print(i+1, end= " ")
                list_possible_moves[i] = True #Also sets the possible moves list in its i possition to true
            else:
                print(" ", end = " ") #Else sets it to false just to make sure
                list_possible_moves[i] = False
    print()
    if(blue_human_player): #Checks if the blue player is human or not, the negative case is not currently implemented
        Return_Board.print_grid()
        if(not(True in list_possible_moves)): #Checks if game is a tie
            print("Game is a Tie")
            exit()
        while(True):
            move = Take_Int_input() - 1#User input, if the move is possible it calls the Make_Move function, if not outputs error and returns to here
            if(move <= 6 and move >= 0):
                if(list_possible_moves[move]):
                    Make_Move(Return_Board, move, 'B')
                    break
    else:
        print()
        Return_Board.print_grid()
        heuristic = A_Star(list_possible_moves, 'B', Return_Board, heuristic)
        Return_Board.print_grid()
    #system('clear')
    return heuristic

def Game_is_Over(test, color): #Checks if the Game is over
    for i in range(3):
        for j in range(4):
            if(Check_Column(test, i, j, color)): # Here it checks the Columns
                print(color +" Wins")
                test.print_grid()
                return True
            if(Check_Line(test, i, j, color)): # Here it checks the Lines
                print(color + " Wins")
                test.print_grid()
                return True
            if(Check_Diagonal(test, i, j, color)): # Here it checks the Diagonals
                print(color + " Wins")
                test.print_grid()
                return True
    return False

def Check_Line(Game, i_plus, j_plus, player): # Simple checking line algorithm, could be improved(probably)
    for i in range(4):
        if(Game.Grid[i + i_plus][0 + j_plus] == player and Game.Grid[i + i_plus][1 + j_plus] == player and Game.Grid[i + i_plus][2 + j_plus] == player and Game.Grid[i + i_plus][3 + j_plus] == player):
            return True
    return False

def Check_Column(Game, i_plus, j_plus, player): # Simple checking Column algorithm, could be improved(probably)
    for j in range(4):
        if(Game.Grid[0 + i_plus][j + j_plus] == player and Game.Grid[1 + i_plus][j + j_plus] == player and Game.Grid[2 + i_plus][j + j_plus] == player and Game.Grid[3 + i_plus][j + j_plus] == player):
            return True
    return False

def Check_Diagonal(Game, i_plus, j_plus, player): # Simple checking Diagonal algorithm
    
    if((Game.Grid[0 + i_plus][0 + j_plus] == player and Game.Grid[1 + i_plus][1 + j_plus] == player and Game.Grid[2 + i_plus][2 + j_plus] == player and Game.Grid[3 + i_plus][3 + j_plus] == player) or (Game.Grid[0 + i_plus][3 + j_plus] == player and Game.Grid[1 + i_plus][2 + j_plus] == player and Game.Grid[2 + i_plus][1 + j_plus] == player and Game.Grid[3 + i_plus][0 + j_plus] == player)):
        return True
    return False


