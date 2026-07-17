#--------------------------helper funcs-------------------------------------
def printArray(Board):
    for row in Board:
        print(row)

#---------------------------------Check if move is possible------------------------------------------------------------------------
'''
NEED TO REWRITE sudChk

not looping thru arrays properly.
'''

#Check if move is able in the 3x3
def sudChk(board, curCub, pos):
    print("in sudChk")
    print("curCub: ", curCub)
    #check for dubs in the 3x3
    #checking for singletons
    #len(curCub) != len(set(curCub))
    single = 1
    for i in range(0,9):
        print("curCub[0] = ", curCub[0])
        print("curCub[pos] = ", curCub[pos])
        if(curCub[pos] == curCub[i] and curCub[i] != 0 and pos != i):
            print("Square Trigger")
            return (True)
    #check the verticle and horizontal lines
    #verticle 
    for i in range(0,9):
        if(board[pos][i] == curCub[pos] and curCub[i] != 0 and pos != i):
            print("Vert Trigger")
            return (True)
    #horizontal
    for i in range(0,9):
        if(board[pos][i] == curCub[pos] and curCub[i] != 0 and pos != i):
            print("board[pos][i] = ", board[pos][i])
            print("curCub[pos] = ", curCub[pos])
            print("Horiz Trigger")
            return (True)
    print("no issues in sudChk")
    return False

#-----------------------------Get 3x3----------------------------------------------------------------------------
#find the square that our current item is apart of
def getSqNum(cellRow, cellCol):
    print("cur row:", cellRow)
    print("cur Col:", cellCol)
    #use the row and column
    squareRow = (cellRow - 1) / 3
    squareCol = (cellCol - 1) / 3
    squareNum = int((squareRow * 3) + squareCol + 1)
    #print("the square we are looking for is: ", squareNum)
    if(squareNum > 8):
        return 8
    else:
        return squareNum

#get a list of all 3x3 squares for later use
def getSq(board):
    cubSeq = {}
    k = 0
    for r in range(0,3):
        for c in range(0,3):
            block = []
            for i in range(0,3):
                for j in range(0,3):
                    block.append(board[3*r + i][3*c + j])
            if(k not in cubSeq):
                cubSeq[k] = [block]
                k+=1
            else:
                cubSeq[k].append(block) 
                k+=1
    return cubSeq

#------------------------------Master Func--------------------------------------------
#Main sequence of code to loop thru
def sudSolv(board):
    #Make note of positions that had a starting number so they don't change
    #loop thru each position's value is 0, and test values 1-9
    # proceed to check that iteration with the 3 rules
    # if fails, increase val and check 3 rules again
    # else move to next pos and repeat.
    #if no values work, backtrack and increase val. 
    # repeat backtrack if it fails again

    #get an array for each 3x3 sq
    Squares = getSq(board)

    print("Generating Mask Board...")
    #create a mask of the board to keep track of the numbers we can't change
    mask = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
    for i in range(0, len(mask[0])):
        for j in range(0, len(mask[0])):
            #if curitem is a non zero number
            if(board[i][j] != 0):
                #update the mask with a flag in that pos
                mask[i][j] = 1
            j+=1
        i+1

    print("\nMask Board:")
    printArray(mask)
    
    print("\nAppllying Nums...")
    #get first item in each array and start applying numbers
    for i in range(0, len(board[0])):
        for j in range(0, len(board[0])):
            if(mask[i][j] == 0):
                for itt in range(1,9):
                    print("cur pos: Row = ", i, " Col = ", j)
                    failed = True
                    #if mask == 0 and this position isn't at the limit of 9
                    print("Mask:", mask[i][j] == 0)
                    print("Board num: ", board[i][j])
                    if(mask[i][j] == 0 and board[i][j] < 9):
                        #if we meet those terms, inc cur pos by one
                        board[i][j] = itt
                        print("current num: ", board[i][j])
                        #get cur num of square we are in
                        curSq = getSqNum(i, j)
                        print("curSq = ", curSq)
                        #update current set of 3x3 (TBT) squares
                        curTBTsq = getSq(board)
                        #call for check
                        print("Running check")
                        failed = sudChk(board, curTBTsq[curSq][0], j)
                        if(failed == False):
                            print("Check Pass\n")
                            break
                    else:
                        #backtrack
                        #subtract j by 1, if j == 1, subtract i by 1
                        if(j != 1):
                            print("backing j up")
                            j -= 1
                        elif(j == 1 and i != 0):
                            print("backing i up")
                            i -= 1
                        else:
                            print("I shouldn't be here")
                    

                    
    
    #return solved board
    return board
        
#----------------------------------------------------------------------------
SodBoard = [[0,1,0,5,0,9,0,7,0],
            [0,0,0,8,6,1,0,0,0],
            [0,0,8,0,2,0,9,0,0],
            [7,3,0,0,0,0,0,2,5],
            [0,9,4,0,0,0,6,3,0],
            [6,8,0,0,0,0,0,9,1],
            [0,0,5,0,4,0,1,0,0],
            [0,0,0,9,1,7,0,0,0],
            [0,6,0,2,0,8,0,4,0]]

print("initial board")
printArray(SodBoard)
boardSolved = sudSolv(SodBoard)
print("\nFinal Board:")
printArray(SodBoard)


#Algorithms
#Knuth's exact problem algorithm
#interesting read
#https://11011110.github.io/blog/2008/01/10/analyzing-algorithm-x.html

#Backtracking - depth first search
#simpler to understand however Big O notation is much higher
#Goal of the algo:
#fill in the first blank space, then slowly work through the next blank spaces until you hit one where its unsolveable.
#if an unsolveable spot is met, backtrack to a previous point and try to change that, hoping it changes the outcome.
#BackTracking uses set rules to contain the seach, this case it will be that each row, column, and 3x3 square must have 1-9. no repeats.