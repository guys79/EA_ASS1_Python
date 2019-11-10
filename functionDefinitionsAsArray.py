# This file contains the definitions of the functions
import random
count =0
board = []
# Creating a random board at the size of NxN
def createBoard (N):
    global count
    global board
    if count%N == 0:
        count = 0
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
        return board[0]
    else:
        return board[count]
    count = count + 1


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
    sum = 0
    if checkForValid(individual):
        for i in range(0,len(individual)):
            for j in range(0,len(individual[i])):
                if individual[i][j] == 1:
                    sum+=getChecks(i,j,individual)
        #print(individual)
        #print(sum)
        return  (len(individual) ** 2 )- sum,
    return 0,
def checkForValid(ind):
    counter = 0
    for line in ind:
        for i in range(0,len(line)):
            counter = counter + line[i]
    return count == len(ind) and count == len(ind[0])
# This function will return the number of checks
def getChecks(row,col,ind):
    count = 0
    # up
    for k in range(0,row):
        if ind[k][col] == 1:
            count = count + 1
    # down
    for k in range(row+1,len(ind)):
        if ind[k][col] == 1:
            count = count + 1
    # left
    for k in range(0,col):
        if ind[row][k] == 1:
            count = count + 1
    # right
    for k in range(col+1,len(ind[row])):
        if ind[row][k] == 1:
            count = count + 1
    # up - right
    i = row -1
    j = col +1
    while(i >=0 and j <len(ind[row])):
        if ind[i][j] == 1:
            count = count + 1
        i = i - 1
        j = j + 1

    # up - left
    i = row - 1
    j = col - 1
    while (i >= 0 and j >=0):
        if ind[i][j] == 1:
            count = count + 1
        i = i - 1
        j = j - 1

    # down - right
    i = row + 1
    j = col + 1
    while (i<len(ind) and j<len(ind[row])):
        if ind[i][j] == 1:
            count = count + 1
        i = i + 1
        j = j + 1

    # down - left
    i = row + 1
    j = col - 1
    while (j >= 0 and i < len(ind)):
        if ind[i][ j] == 1:
            count = count + 1
        i = i + 1
        j = j - 1
    return count

#b = createBoard(4)
#b= [[0, 0, 1, 1], [0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0]]
#printBoard(b)
#print(evaluation(b))
# 1 + 3+2+2