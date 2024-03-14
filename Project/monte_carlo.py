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
        self.move = -1

def select(node): 
    # Função para selecionar o próximo nó filho usando a política UCB (Upper Confidence Bound)
    selected_node = None
    max_ucb = -float('inf')  # Valor inicial para a pontuação UCB (menor que o menor possível)
    for child in node.children:
        if child.visits == 0:
            ucb = float('inf')  # Se o nó filho ainda não foi visitado, o UCB é definido como infinito para incentivá-lo a ser explorado
        else:
            # Fórmula do UCB: exploração (score/visits) + exploração (2 * log(total_visits) / visits) ** 0.5
            ucb = (child.score / child.visits) + (2 * (2 * node.visits / child.visits) ** 0.5)  
        if ucb > max_ucb:
            max_ucb = ucb
            selected_node = child
    return selected_node

def expand(node, color):
    # Função para expandir os filhos do nó atual para ambos os jogadores
    colors = ['R', 'B']
    for column in range(7):
        temp_game = copy.deepcopy(node.state)
        if Game_is_Over(temp_game, 'R') or Game_is_Over(temp_game, 'B'):
            break
        if temp_game.Grid[0][column] == 'X':
            for c in colors:
                Make_Move(temp_game, column, c) 
                new_node = Node(temp_game)
                new_node.parent = node
                new_node.move = column
                node.children.append(new_node)
                temp_game = copy.deepcopy(node.state)

def simulate(state, color):
    # Função para simular um jogo a partir de um estado para ambos os jogadores
    temp_game = copy.deepcopy(state)
    while True:
        for c in ['R', 'B']:
            columns = [i for i in range(7) if temp_game.Grid[0][i] == 'X']
            column = random.choice(columns)  # Escolhe uma coluna aleatória disponível
            Make_Move(temp_game, column, c) 
            if Game_is_Over(temp_game, 'R') or Game_is_Over(temp_game, 'B'):
                print(Total_Value(temp_game))
                return Total_Value(temp_game)  # Retorna a pontuação do jogo usando a heurística


def backpropagate(node, score):
    # Função para atualizar as estatísticas de visitas e pontuação dos nós após uma simulação
    while node is not None:
        node.visits += 1
        node.score += score
        node = node.parent

def mcts(state, iterations):
    # Função principal do algoritmo Monte Carlo Tree Search
    root = Node(state)
    for _ in range(iterations):
        node = root
        while node.children:
            node = select(node)  # Seleciona o próximo nó filho usando a política UCB
        expand(node, 'R')  # Expande os filhos do nó atual / MUDAR PARA COR SELECIONÁVEL AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   
        score = simulate(node.state, 'R')  # Simula um jogo a partir do estado do nó
        backpropagate(node, score)  # Retropropaga os resultados
    best_move = None
    best_score = -float('inf')
    # Encontra o melhor movimento baseado nas estatísticas coletadas durante as simulações
    # ERRRO AQUI, SEMPRE RETORNA O BEST_MOVE COMO 0, OU SEJA NA PRIMEIRA COLUNA
    for child in root.children:
        if ((child.visits > 0) and (child.score / child.visits) > best_score):
            best_move = child.move
            best_score = (child.score / child.visits)
        print(best_move)
    return best_move

def main():
    # Função principal para controlar o fluxo do jogo
    board = Board()
    board.print_grid()
    while not Game_is_Over(board, 'R') and not Game_is_Over(board, 'B'):
        move_col = int(input("Enter your move (1-7): ")) - 1
        if move_col < 0 or move_col >= 7 or board.Grid[0][move_col] != 'X':
            print("Invalid move. Try again.")
            continue
        Make_Move(board, move_col, 'R') 
        
        if Game_is_Over(board, 'R'):
            print("Red Wins!")
            break
    
        bot_move = mcts(board, iterations=5)
        if bot_move is None:
            print("No valid move found. Game over.")
            break
        print(bot_move)
        Make_Move(board, bot_move, 'B')
        if Game_is_Over(board, 'B'):
            print("Blue Wins!")
            break
        board.print_grid()

if __name__ == "__main__":
    main()
