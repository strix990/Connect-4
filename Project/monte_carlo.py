import random
import math
import copy
from Board import *

class Cor: #For colors, pretty self intuitive
    RESET = '\033[0m'
    VERMELHO = '\033[91m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    
class Node:
    def __init__(self, state, player, parent=None):
        self.state = state
        self.player = player
        self.parent = parent
        self.children = []
        self.visits = 0
        self.reward = 0

    def child(self, node):
        self.children.append(node)

    def __repr__(self):
        return f"Node({self.state}, {self.player}, {self.parent})"
    
    def get_score(self):
        if len(self.children) == 0:
            return self.reward / self.visits if self.visits > 0 else 0
        total_visits = sum([child.visits for child in self.children])
        total_reward = sum([child.reward for child in self.children])
        return total_reward / total_visits + 1.4 * (math.sqrt(math.log(self.visits) / total_visits)) if total_visits > 0 else 0

def simulate(state, player): 
    while not Game_is_Over(state, player):
        move = random.randint(0, 6)
        state = Make_Move(state, player, move)
        player = -player
    return Game_is_Over(state,player)


def monte_carlo(state, iterations):
    root = Node(state, 1)

    for _ in range(iterations):
        node = root
        path = [node]
        
        while True:
            if len(node.children) == 0 or node.visits == 0:
                break
            node = max(node.children, key=lambda x: x.get_score())
            path.append(node)

        child_state = copy.deepcopy(node.state)
        child_player = -node.player
        move = random.randint(0, 6)
        child_state = Make_Move(child_state, child_player, move)
        child_node = Node(child_state, -child_player, node)
        node.child(child_node)
        reward = simulate(child_state, child_player)
        
        for n in path[::-1]:
            n.visits += 1
            n.reward += reward

    if len(root.children) == 0:
        return Node(state, 1)

    return max(root.children, key=lambda x: x.get_score())

def get_best_move(state, iterations):
    root = Node(state, 1)

    if not root.children:

        return len(state[0]) // 2
    
    best_child = max(root.children, key=lambda x: x.get_score())
    for _ in range(iterations):
        node = monte_carlo(root, iterations)
        if node.player == 1:
            best_child = node
    move = best_child.state.index(0)
    print("Best child:", best_child)
    print("Children of root:", root.children)
    return move




def main():
    board = Board() 
    current_player = 1
    iterations = 1000

    while True:
        board.print_grid()  
        if current_player == 1:
            print("Player 1's turn")
            col = int(input("Enter the column to drop your piece: "))
            if board.Grid[0][col] != 'X': 
                print("Column is full. Try again.")
                continue
            row = Make_Move(board, col, 'R')  
            board.Grid[row][col] = 'R'  
        else:
            print("Player 2's turn (AI)")
            best_move = get_best_move(board.Grid, iterations) 
            if best_move == -1:
                print("No valid moves for AI. Try again.")
                continue
            row = Make_Move(board, best_move, 'B')  
            board.Grid[row][best_move] = 'B'  

        if Game_is_Over(board, current_player): 
            board.print_grid() 
            print(f"Player {current_player} wins!")
            break

        if len([cell for row in board.Grid for cell in row if cell == 'X']) == 0:  
            board.print_grid()  
            print("It's a draw!")
            break

        current_player *= -1


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
            return i 
    print("You should not be here")


if __name__ == "__main__":
    main()