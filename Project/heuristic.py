#from Board import Board

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
                if(self.Grid[i][j] == 'T'):
                    print(Cor.MAGENTA + self.Grid[i][j] + Cor.RESET, end=" ")
            print()

def Compute_Score(count_R, count_B): #Calculates the value for a set of pieces , as specified in the project worksheet
    if(count_R >= 1 and count_B >= 1):#Mixed pieces
        return 0
    else:
        if(count_R != 0): #Red pieces
            match count_R:
                case 1:
                    return (1)
                case 2:
                    return (10)
                case 3:
                    return (50)
                case 4:
                    return 512
        elif(count_B != 0): #Blue pieces
            match count_B:
                case 1:
                    return -1
                case 2:
                    return -10
                case 3:
                    return -50
                case 4:
                    return -512
    return 0

def Is_Red(piece):
    if(piece == 'R'):
        return True
    else:
        return False

def Compute_Lines(Game): #Compute all 4 line pieces segments
    total = 0
    total_temp = 0
    count_R = 0
    count_B = 0
    for i in range(6): #Grid Lines
        for j1 in range(0,4,1): #segment offset, 4 for each line
            for j2 in range(0,4,1): #4 pieces
                if(Game.Grid[i][j1+j2] == 'X'):
                    continue
                elif(Is_Red(Game.Grid[i][j1+j2])):
                    count_R += 1
                else:
                    count_B += 1
            total_temp = Compute_Score(count_R, count_B) #Score calculation
            if(total_temp == 512 or total_temp == -512):
                return total_temp
            total += total_temp
            total_temp = 0
            count_R = 0
            count_B = 0
    return total        
                    
def Compute_Columns(Game): #Compute all 4 columns pieces segments
    total = 0
    total_temp = 0
    count_R = 0
    count_B = 0
    for j in range(7): #Grid Columns
        for i1 in range(0,3,1): #segment offset, 3 for each column
            for i2 in range(0,4,1): #4 pieces
                if(Game.Grid[i1+i2][j] == 'X'):
                    continue
                elif(Is_Red(Game.Grid[i1+i2][j])):
                    count_R += 1
                else:
                    count_B += 1
            total_temp = Compute_Score(count_R, count_B) #Score calculation
            if(total_temp == 512 or total_temp == -512):
                return total_temp
            total += total_temp
            total_temp = 0
            count_R = 0
            count_B = 0
    return total        

def Compute_Diagonals_Positive(Game):
    total = 0
    total_temp = 0
    count_R = 0
    count_B = 0
    count_number_fors = 3
    for i in range(3): #Diagonal positiva 1/2
        for temp in range (count_number_fors):
            for j in range(4):
                if(Game.Grid[i+j+temp][0+j+temp] == 'X'):
                    continue
                elif(Is_Red(Game.Grid[i+j+temp][0+j+temp])):
                    count_R += 1
                else:
                    count_B += 1
            total_temp = Compute_Score(count_R, count_B) #Score calculation
            if(total_temp == 512 or total_temp == -512):
                return total_temp
            total += total_temp
            total_temp = 0
            count_R = 0
            count_B = 0
        count_number_fors -= 1
    count_number_fors = 3
    for i in range(3): #Diagonal positiva 2/2
        for temp in range (count_number_fors):
            for j in range(4):
                if(Game.Grid[j+temp][1+j+temp+i] == 'X'):
                    continue
                elif(Is_Red(Game.Grid[j+temp][1+j+temp+i])):
                    count_R += 1
                else:
                    count_B += 1
            total_temp = Compute_Score(count_R, count_B) #Score calculation
            if(total_temp == 512 or total_temp == -512):
                return total_temp
            total += total_temp
            total_temp = 0
            count_R = 0
            count_B = 0
        count_number_fors -= 1
    count_number_fors = 3
    for i in range(3): #Diagonal negativa 1/2
        for temp in range (count_number_fors):
            for j in range(4):
                if(Game.Grid[0+j+temp+i][6-j-temp] == 'X'):
                    continue
                elif(Is_Red(Game.Grid[0+j+temp+i][6-j-temp])):
                    count_R += 1
                else:
                    count_B += 1
            total_temp = Compute_Score(count_R, count_B) #Score calculation
            if(total_temp == 512 or total_temp == -512):
                return total_temp
            total += total_temp
            total_temp = 0
            count_R = 0
            count_B = 0
        count_number_fors -= 1
    count_number_fors = 3
    for i in range(3): #Diagonal negativa 1/2
        for temp in range (count_number_fors):
            for j in range(4):
                if(Game.Grid[0+j+temp][5-i-j-temp] == 'X'):
                    continue
                elif(Is_Red(Game.Grid[0+j+temp][5-i-j-temp])):
                    count_R += 1
                else:
                    count_B += 1
            total_temp = Compute_Score(count_R, count_B) #Score calculation
            if(total_temp == 512 or total_temp == -512):
                return total_temp
            total += total_temp
            total_temp = 0
            count_R = 0
            count_B = 0
        count_number_fors -= 1
    count_number_fors = 3
    return total

def Total_Value(Game):
    sum_columns = 0
    sum_diagonals = 0 
    sum_columns = 0
    sum_lines = Compute_Lines(Game)
    if(sum_lines == 512 or sum_lines == -512):
        return sum_lines
    sum_columns = Compute_Columns(Game)
    if(sum_columns == 512 or sum_columns == -512):
        return sum_columns
    sum_diagonals = Compute_Diagonals_Positive(Game)
    if(sum_diagonals == 512 or sum_diagonals == -512):
        return sum_diagonals
    return (sum_lines + sum_columns + sum_diagonals)

# bravo = Board()
# bravo.Grid[0][5] = 'B'
# bravo.Grid[0][1] = 'R'
# bravo.Grid[0][2] = 'R'
# bravo.Grid[0][3] = 'R'
# bravo.Grid[5][3] = 'R'
# bravo.Grid[5][6] = 'R'
# bravo.print_grid()
# out = Total_Value(bravo)
# print(out)
