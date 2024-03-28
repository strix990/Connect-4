from Board import *
from heuristic import *
from a_star import *

class Cor: #For colors, pretty self intuitive
    RESET = '\033[0m'
    VERMELHO = '\033[91m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'

def main(): #Used to run the program
    print(""" 

 ____                                           __        __ __      
/\  _`\                                        /\ \__    /\ \\ \     
\ \ \/\_\    ___     ___     ___      __    ___\ \ ,_\   \ \ \\ \    
 \ \ \/_/_  / __`\ /' _ `\ /' _ `\  /'__`\ /'___\ \ \/    \ \ \\ \_  
  \ \ \L\ \/\ \L\ \/\ \/\ \/\ \/\ \/\  __//\ \__/\ \ \_    \ \__ ,__\
   \ \____/\ \____/\ \_\ \_\ \_\ \_\ \____\ \____\\ \__\    \/_/\_\_/
    \/___/  \/___/  \/_/\/_/\/_/\/_/\/____/\/____/ \/__/       \/_/  
                                                                     
                                                                     
    """)
    print("Options")
    print("[1]Play as Red")
    print("[2]Play as Blue")
    print("[3]Two player mode")
    print("[4]CPU vs CPU")
    while(True):
        try:
            opt = int(input())
            break
        except ValueError:
            continue
    match opt:
        case 1:
            red_human_player = True
            blue_human_player = False
        case 2:
            red_human_player = False
            blue_human_player = True
        case 3:
            red_human_player = True
            blue_human_player = True
        case 4:
            red_human_player = False
            blue_human_player = False
    print("Choose an algorithm: ")
    print("[1] A * Star")
    print("[2] MCTS")
    while(True):
        try:
            opc = int(input())
            break
        except ValueError:
            continue
    heuristic = 0
    print(Cor.MAGENTA + "Start!" + Cor.RESET) # Very important!
    test = Board()
    while(True): #Used for playing the game, first comes reds turn then if the game is not over comes blues turn and again if it's no over it loops back to reds turn
        heuristic = Red_moves(test, red_human_player, heuristic, opc)
        if(Game_is_Over(test, 'R')):
            break
        heuristic = Blue_moves(test, blue_human_player,heuristic, opc)
        if(Game_is_Over(test, 'B')):
            break
    print()
    if(Game_is_Over(test, 'R')):
        print ("RED WINS!")
    if(Game_is_Over(test, 'B')):
        print ("BLUE WINS!")
    if(not(Game_is_Over(test, 'R') and Game_is_Over(test, 'B'))):
        print("DRAW!")
    test.print_grid()
main()#Currently nothing but the Board implemented
