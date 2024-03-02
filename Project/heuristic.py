from Board import Board

def Compute_Score(Count_R, Count_B, total): #Calculates the value for a set of pieces , as specified in the project worksheet
    if(Count_R >= 1 and Count_B >= 1):#Mixed pieces
        return 0
    else:
        if(Count_R != 0): #Red pieces
            match Count_R:
                case 1:
                    return (1)
                case 2:
                    return (10)
                case 3:
                    return (50)
                case 4:
                    return 512 - total
        elif(Count_B != 0):#Blue pieces
            match Count_B:
                case 1:
                    print("filha da puta")
                    return -1
                case 2:
                    print(Count_B + "FILHA DA PUTA")
                    return -10
                case 3:
                    return -50
                case 4:
                    total = 0
                    return -512 - total
    return 0

def Is_Red(piece):
    if(piece == 'R'):
        return True
    else:
        return False

def Compute_Lines(Game):
    total = 0
    count_R = 0
    count_B = 0
    for i in range(6):
        for j1 in range(0,4,1):
            for j2 in range(0,4,1):
                if(Game.Grid[i][j1+j2] == 'X'):
                    continue
                elif(Is_Red(Game.Grid[i][j1+j2])):
                    count_R += 1
                else:
                    count_B += 1
            total += Compute_Score(count_R, count_B, total)
            if(total == 512 or total == -512):
                return total
            count_R = 0
            count_B = 0
    return total        
                    
def Compute_Columns(Game):
    total = 0
    count_R = 0
    count_B = 0
    for j in range(6):
        for i1 in range(0,3,1):
            for i2 in range(0,4,1):
                if(Game.Grid[i1+i2][j] == 'X'):
                    continue
                elif(Is_Red(Game.Grid[i1+i2][j])):
                    count_R += 1
                else:
                    count_B += 1
            total = Compute_Score(count_R, count_B, total)
            if(total == 512 or total == -512):
                return total
            count_R = 0
            count_B = 0
    return total        

def Compute_Diagonals(Game):
    total = 0
    count_R = 0
    count_B = 0
    for i in range(3): #Diagonal positiva 1/2
        while(3-i>0):
            for j in range(3):
                if(Game.Grid[i+j][0+j] == 'X'):
                    continue
                elif(Is_Red(Game.Grid[i+j][0+j])):
                    count_R += 1
                else:
                    count_B += 1
            total = Compute_Score(count_R, count_B, total)
            if(total == 512 or total == -512):
                return total
            count_R = 0
            count_B = 0
            for j2 in range(3):#Diagonal positiva 2/2
                if(Game.Grid[0+j2][(i+1)+j2] == 'X'):
                    continue
                elif(Is_Red(Game.Grid[0+j2][(i+1)+j2])):
                    count_R += 1
                else:
                    count_B += 1
            total = Compute_Score(count_R, count_B, total)
            if(total == 512 or total == -512):
                return total
            count_R = 0
            count_B = 0
            break
    return total
        

def Total_Value(Game):
    sum_columns = 0
    sum_diagonals = sum_columns
    #Visited = [[False for _ in range(7)] for _ in range(6)]
    sum_lines = Compute_Lines(Game)
    if(sum_lines == 512 or sum_lines == -512):
        return sum_lines
    '''sum_columns = Compute_Columns(Game)
    if(sum_columns == 512 or sum_columns == -512):
        return sum_columns
    sum_diagonals = Compute_Diagonals(Game)
    if(sum_diagonals == 512 or sum_diagonals == -512):
        return sum_diagonals
    #return (sum_lines + sum_columns + sum_diagonals)'''
    return(sum_lines)


total = 0 #Declared as a Global Variable, mainly becaused it's used across multiple functions
bravo = Board()
bravo.Grid[0][0] = 'B'
bravo.Grid[1][1] = 'B'
bravo.Grid[2][2] = 'B'
bravo.Grid[3][3] = 'B'
bravo.print_grid()
out = Total_Value(bravo)
print(out)
