import copy
import random
from Board import Board, Make_Move, Game_is_Over
from heuristic import Total_Value

class Node:
    def __init__(self, state):
        self.state = state
        self.visits = 0
        self.score = 0
        self.children = []
        self.parent = None

def select(node): # Seleciona o nó filho com base na política UCB (Upper Confidence Bound)
    selected_node = None
    max_ucb = -float('inf')
    for child in node.children:
        if child.visits == 0:
            ucb = float('inf') 
        else:
            ucb = (child.score / child.visits) + (2 * (2 * node.visits / child.visits) ** 0.5)  # Fórmula do UCB
        if ucb > max_ucb:
            max_ucb = ucb
            selected_node = child
    return selected_node

def expand(node): # Gera todos os possíveis movimentos a partir do estado atual do jogo
    for column in range(7):
        temp_game = copy.deepcopy(node.state)
        if Game_is_Over(temp_game, 'R') or Game_is_Over(temp_game, 'B'):
            break
        if temp_game.Grid[0][column] == 'X':
            Make_Move(temp_game, column, 'R') 
            new_node = Node(temp_game)
            new_node.parent = node
            node.children.append(new_node)

def simulate(state): #Realiza uma simulação do jogo a partir do estado atual e usa a heurística para avaliar o resultado
    temp_game = copy.deepcopy(state)
    while not Game_is_Over(temp_game, 'R') and not Game_is_Over(temp_game, 'B'): # Simula movimentos aleatórios até que o jogo termine
        columns = [i for i in range(7) if temp_game.Grid[0][i] == 'X']
        column = random.choice(columns)
        Make_Move(temp_game, column, 'R') 
    return Total_Value(temp_game) 

def backpropagate(node, score): # Atualiza as estatísticas de visitas e pontuação de todos os nós percorridos de volta à raiz
    while node is not None:
        node.visits += 1
        node.score += score
        node = node.parent

def mcts(state, iterations):
    root = Node(state)
    for _ in range(iterations):
        node = root
        while node.children:
            node = select(node)
        expand(node)
        score = simulate(node.state)
        backpropagate(node, score)
    best_move = None
    best_score = -float('inf')
    for child in root.children:
        if child.visits > 0 and child.score / child.visits > best_score:
            best_move = child.state
            best_score = child.score / child.visits

    return best_move

def main():
    board = Board()
    while not Game_is_Over(board, 'R') and not Game_is_Over(board, 'B'):
        board.print_grid()
        move_col = int(input("Enter your move (1-7): ")) - 1
        if move_col < 0 or move_col >= 7 or board.Grid[0][move_col] != 'X':
            print("Invalid move. Try again.")
            continue
        Make_Move(board, move_col, 'B') 
        
        if Game_is_Over(board, 'B'):
            print("Blue Wins!")
            break
        
        move = mcts(board, iterations=1000)
        if move is None:
            print("No valid move found. Game over.")
            break
        Make_Move(board, move, 'R')
        
        if Game_is_Over(board, 'R'):
            print("Red Wins!")
            break

    board.print_grid()

if __name__ == "__main__":
    main()
