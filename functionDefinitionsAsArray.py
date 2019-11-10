# This file contains the definitions of the functions
import random

# Creating a random board at the size of NxN
def createBoard (N):
    set = [] # Set of locations
    include = [] # already existing locations

    # Create locations
    for i in range(0,N):
        loc = createRand(-1,N*N-1,include)
        include.append(loc)
        set.append([int(loc/N),loc%N])

    # Init board
    board = []
    for i in range(0,N):
        line = [0]*N
        board.append(line)

    # Updating board with coordinates
    for coord in set:
        board[coord[0]][coord[1]]=1
    return board


# This function will create a random number from (min -1 to max, included) that doesn't include in the notInclude set
def createRand (min,max,notInclude):
    num = random.randint(min,max)
    while(num in notInclude):
        num = random.randint(min, max)
    return num;

# This function will print the given board
def printBoard(board):
    for line in board:
        print(line)

# Evaluation function
def evaluation(individual):
    # assumption, individual is a board
    print(individual)
    sum = 0
    for i in range(0,len(individual)):
        for j in range(0,len(individual[i])):
            if individual[i][j] == 1:
                sum+=getChecks(i,j,individual)
    return sum

# This function will return the number of checks
def getChecks(row,col,board):
    count = 0
    # up
    for k in range(0,row):
        if board[k][col] == 1:
            count = count + 1
    # down
    for k in range(row+1,len(board)):
        if board[k][col] == 1:
            count = count + 1
    # left
    for k in range(0,col):
        if board[row][k] == 1:
            count = count + 1
    # right
    for k in range(col+1,len(board[row])):
        if board[row][k] == 1:
            count = count + 1
    # up - right
    i = row -1
    j = col +1
    while(i >=0 and j <len(board[col])):
        if board[i][j] == 1:
            count = count + 1
        i = i - 1
        j = j + 1

    # up - left
    i = row - 1
    j = col - 1
    while (i >= 0 and j >=0):
        if board[i][j] == 1:
            count = count + 1
        i = i - 1
        j = j - 1

    # down - right
    i = row + 1
    j = col + 1
    while (i<<len(board) and j<len(board[col])):
        if board[i][ j] == 1:
            count = count + 1
        i = i + 1
        j = j + 1

    # down - left
    i = row + 1
    j = col - 1
    while (j >= 0 and i < len(board)):
        if board[i][ j] == 1:
            count = count + 1
        i = i + 1
        j = j - 1
    return count

b = createBoard(4)
printBoard(b)
print(evaluation(b))