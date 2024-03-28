import copy
import random
#from Board import Board, Make_Move, Game_is_Over
from heuristic import Total_Value

class Node:
    def __init__(self, state):
        self.state = state
        self.visits = 0
        self.score = 0
        self.children = []
        self.parent = None
        self.move = -1

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

def expand(node, jogadas):
    # Função para expandir os filhos do nó atual para ambos os jogadores
    for column in range(7):
        temp_game = copy.deepcopy(node.state)
        if Game_is_Over(temp_game, 'R') or Game_is_Over(temp_game, 'B'):
            break
        if temp_game.Grid[0][column] == 'X':
            for c in jogadas:
                Make_Move(temp_game, column, c) 
                new_node = Node(temp_game)
                new_node.parent = node
                new_node.move = column
                node.children.append(new_node)
                temp_game = copy.deepcopy(node.state)

def simulate(state, jogadas):
    # Função para simular um jogo a partir de um estado para ambos os jogadores
    temp_game = copy.deepcopy(state)
    while True:
        for c in jogadas:
            columns = [i for i in range(7) if temp_game.Grid[0][i] == 'X']
            if (len(columns) != 0):
                column = random.choice(columns)  # Escolhe uma coluna aleatória disponível
                Make_Move(temp_game, column, c) 
            else:
                return Total_Value(temp_game)
            if Game_is_Over(temp_game, 'R') or Game_is_Over(temp_game, 'B'):
                #print(Total_Value(temp_game))
                return Total_Value(temp_game)  # Retorna a pontuação do jogo usando a heurística

def backpropagate(node, score):
    # Função para atualizar as estatísticas de visitas e pontuação dos nós após uma simulação
    while node is not None:
        node.visits += 1
        node.score += score
        node = node.parent

def mcts(state, iterations, player):
    # Função principal do algoritmo Monte Carlo Tree Search
    if (player == 1):
        jogadas = ['R', 'B']
    else:
        jogadas = ['B', 'R']
    root = Node(state)
    for _ in range(iterations):
        node = root
        while node.children:
            node = select(node)  # Seleciona o próximo nó filho usando a política UCB
        expand(node, jogadas)  # Expande os filhos do nó atual / MUDAR PARA COR SELECIONÁVEL AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   
        score = simulate(node.state, jogadas)  # Simula um jogo a partir do estado do nó
        backpropagate(node, score)  # Retropropaga os resultados
    best_move = None
    best_score = -float('inf')
    # Encontra o melhor movimento baseado nas estatísticas coletadas durante as simulações
    # ERRRO AQUI, SEMPRE RETORNA O BEST_MOVE COMO 0, OU SEJA NA PRIMEIRA COLUNA
    for child in root.children:
        if ((child.visits > 0) and (child.score / child.visits) > best_score):
            best_move = child.move
            best_score = (child.score / child.visits)
    return best_move

def Make_Move(Return_Board, index, color): #Computes the move, inputed by the index argument, by the player indentified by the color argument
    for i in range(5, -1, -1):
        if(Return_Board.Grid[i][index] == 'X'):
            Return_Board.Grid[i][index] = color
            return
    print("You should not be here")

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

def Game_is_Over(test, color): #Checks if the Game is over
    for i in range(3):
        for j in range(4):
            if(Check_Column(test, i, j, color)): # Here it checks the Columns
                #print(color +" Wins")
                #test.print_grid()
                return True
            if(Check_Line(test, i, j, color)): # Here it checks the Lines
                #print(color + " Wins")
                #test.print_grid()
                return True
            if(Check_Diagonal(test, i, j, color)): # Here it checks the Diagonals
                #print(color + " Wins")
                #test.print_grid()
                return True
    return False
