from heuristic import heuristic
from board import Board


class A_Star(visited, playerColor, game):
    greatest_value = [0,0]
    for i in range(7):
        if (visited[i]):
            a_star_board = Board() 
            lista_temp = copy.deepcopy(game.Grid)
            setattr(a_star_board, 'Grid', lista_temp) #For the last three lines, because of python refence bullshittery, I had to make a deepcopy of the Board.Grid. Right now either the value is passed by reference or not doesn't make a difference but in order to no fuck up the code in the future I made it this way. Any other solutions are welcome since this looks ugly and must be pretty inneficient :3
            Make_Move(a_star_board, i, playerColor)
            value_temp = Total_Value(a_star_board)
            if(Is_Red(PlayerColor)):
                 if(value_temp > greatest_value[0]):
                     greatest_value[0] = value_temp
                     greatest_value[1] = i
                     value_temp = 0
    Make_Move(game, greatest_value[1], playerColor)               