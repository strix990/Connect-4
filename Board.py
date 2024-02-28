import copy

class Board:
    def __init__(self):
        self.Grid = [['X' for _ in range(7)] for _ in range(6)] # Initializes the Boards Grid with empty spaces

    def print_grid(self):  # Prints the Grid, pretty self intuitive
        for i in range(6):
            for j in range(7):
                print(self.Grid[i][j], end=" ")
            print()

def Make_Move(Return_Board, index, color): #Computes the move, inputed by the index argument, by the player indentified by the color argument
    for i in range(5, -1, -1):
        if(Return_Board.Grid[i][index-1] == 'X'):
            Return_Board.Grid[i][index-1] = color
            return
    print("You should not be here")

def Red_moves(Game, red_human_player): #Computes Reds movement
    Return_Board = Board() 
    lista_temp = copy.deepcopy(Game.Grid)
    setattr(Return_Board, 'Grid', lista_temp) #For the last three lines, because of python refence bullshittery, I had to make a deepcopy of the Board.Grid. Right now either the value is passed by reference or not doesn't make a difference but in order to no fuck up the code in the future I made it this way. Any other solutions are welcome since this looks ugly and must be pretty inneficient :3
    list_possible_moves = [False for _ in range(7)] #List of possible moves, for now its entirety is false
    if(red_human_player): #Checks if Red player is human or not, the negative case is not currently implemented
        print("Reds Turn")
        for i in range(7): #Checks if all columns are filled (in other words if a move is possible), if it is, print the corresponding number above the column
            if(Return_Board.Grid[0][i] == 'X'):
                print(i+1, end= " ")
                list_possible_moves[i] = True #Also sets the possible moves list in its i possition to true
            else:
                print(" ", end = " ") #Else sets it to false just to make sure
                list_possible_moves[i] = False
        print()
        Return_Board.print_grid()
        if(not(True in list_possible_moves)): #Checks if game is a tie
            print("Game is a Tie")
            exit()
        while(True):
            move = int(input('Choose your move: '))#User input, if the move is possible it calls the Make_Move function, if not outputs error and returns to here
            if(move <= 7 and move > 0):
                if(list_possible_moves[move-1]):
                    Make_Move(Return_Board, move, 'R')
                    break
            print("Invalid move you moron")
    return Return_Board

def Blue_moves(Game, blue_human_player): #Computes Blues movement
    Return_Board = Board() 
    lista_temp = copy.deepcopy(Game.Grid)
    setattr(Return_Board, 'Grid', lista_temp) #For the last three lines, because of python refence bullshittery, I had to make a deepcopy of the Board.Grid. Right now either the value is passed by reference or not doesn't matter but in order to no fuck up the code in the future I made it this way. Any other solutions are welcome since this looks ugly and must be pretty inneficient :3
    list_possible_moves = [False for _ in range(7)] #List of possible moves
    if(blue_human_player): #Checks if the blue player is human or not, the negative case is not currently implemented
        print("Blues Turn")
        for i in range(7): #Checks if all columns are filled (in other words if a move is possible), if it is, print the corresponding number above the column
            if(Return_Board.Grid[0][i] == 'X'):
                print(i+1, end= " ")
                list_possible_moves[i] = True #Also sets the possible moves list in its i possition to true
            else:
                print(" ", end = " ") #Else sets it to false just to make sure
                list_possible_moves[i] = False
        print()
        Return_Board.print_grid()
        if(not(True in list_possible_moves)): #Checks if game is a tie
            print("Game is a Tie")
            exit()
        while(True):
            move = int(input('Choose your move: '))#User input, if the move is possible it calls the Make_Move function, if not outputs error and returns to here
            if(move <= 7 and move > 0):
                if(list_possible_moves[move-1]):
                    Make_Move(Return_Board, move, 'B')
                    break
            print("Invalid move you moron")
    return Return_Board

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

def main():
    red_human_player = True
    blue_human_player = True
    print("Super duper ultra mega incredible IA project!") # Very important!
    test = Board()
    while(True): #Used for playing the game, first comes reds turn then if the game is not over comes blues turn and again if it's no over it loops back to reds turn
        test = Red_moves(test, red_human_player)
        if(Game_is_Over(test, 'R')):
            break
        test = Blue_moves(test, blue_human_player)
        if(Game_is_Over(test, 'B')):
            break 
main()#Currently nothing but the Board implemented
