##Brute Forcing Sodoku
'''
sodoku board consists of 9 3x3 squares 

2d array can be used to make the the sodoku board
    use mod3 to get the smaller 3x3 square 

brute force to solve
    scannby rows as the entire row can only be singleton (only 1 number in each row, no repeat numbers)

'''
#---------------------------------------------------------------------------------------------------------
#Check if move is able in the 3x3
def sudChk(board, curCub, pos):
    print("in sudChk")
    print(curCub)
    #check for dubs in the 3x3
    #checking for singletons
    #len(curCub) != len(set(curCub))
    single = 1
    for i in range(0,9):
        if(curCub[pos] == curCub[i] and curCub[i] != 0 and pos != i):
            print("curCub[0] = ", curCub[0])
            print("curCub[pos] = ", curCub[pos])
            print("Trigger 1")
            return (False, curCub)
    #check the verticle and horizontal lines
    #verticle 
    for i in range(0,9):
        if(board[pos][i] == curCub[pos] and curCub[i] != 0 and pos != i):
            print("Trigger 2")
            return (False, curCub)
    #horizontal
    for i in range(0,9):
        if(board[pos][i] == curCub[pos] and curCub[i] != 0 and pos != i):
            print("board[pos][i] = ", board[pos][i])
            print("curCub[pos] = ", curCub[pos])
            print("Trigger 3")
            return (False, curCub)
    print("else hit")
    return (True, curCub)
#---------------------------------------------------------------------------------------------------------
#find the square that our current item is apart of
def getSqNum(cellRow, cellCol):
    #use the row and column
    squareRow = (cellRow - 1) / 3
    squareCol = (cellCol - 1) / 3
    squareNum = int((squareRow * 3) + squareCol + 1)
    print("the square we are looking for is: ", squareNum)
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

#---------------------------------------------------------------------------------------------------------
#Create a dictionary that can store all numbers that the cur pos CANNOT BE
def noNumDict(board):
    #create a dict to store all the bad numbers of the array
    noNoNums = {}

    #for curSeq in board:
    for curArr in range(0,9):
        print("==========================curArr:", curArr, "=============================")
        curSeq = board[curArr]
        print("current Sequence: ", curSeq)
        #check along the horizontal axis 
        # in the array
        #we use range() because we want i to also be used to name keys for board positions
        for i in range(0,9):
            if(curSeq[i] == 0):
                for j in range(0,9):
                    if(curSeq[j] != 0):
                        if(curArr == 0 and i not in noNoNums):
                            noNoNums[i] = [curSeq[j]]
                        elif(curArr > 0 and (i + (9*curArr)) not in noNoNums):
                            noNoNums[(i + (9*curArr))] = [curSeq[j]]
                        else:
                            noNoNums[(i + (9*curArr))].append(curSeq[j]) 

        #check along the Vertical axis
        # keep the position but iterate through all arrays in the board
        
        for i in range(0,9):
            if(curSeq[i] == 0):
                for j in range(0,9):
                    if(board[j][i] != 0):
                        if(curArr == 0 and i not in noNoNums):
                            noNoNums[i] = [curSeq[j]]
                        elif(curArr > 0 and (i + (9*curArr)) not in noNoNums):
                            noNoNums[(i + (9*curArr))] = [board[j][i]]
                        elif(board[j][i] not in noNoNums[(i + (9*curArr))]):
                            noNoNums[(i + (9*curArr))].append(board[j][i])
        
        #check within the 3x3 square the curpos belongs too
        #find the square its apart of

        #call getSq to get a dictionary of all 3x3's
        curSqs = getSq(board)
        print("curSqs = ", curSqs)
        #then call a function to find the current square we want to use to compare against
        for pos in range(0,9):
            if(curSeq[pos] == 0):
                for arr in range(0,9):
                    #call the find curcq func
                    curSqNum = getSqNum(arr, pos)
                    curSqSeq = curSqs[curSqNum]
                    print("curSqNum = ", curSqNum)
                    print("curSqSeq = ", curSqSeq)
                    for i in range(0,9):
                        if(curSqSeq[0][i] == 0):
                            curSqSeq[0][i].remove(i)
                    print("here are the numbers that it can't be from its curSq:", curSqSeq[curSqNum])
        
        print("Numbers that the positions cannot be")
        print(noNoNums)
        #return noNoNums


#---------------------------------------------------------------------------------------------------------
#use the dictionary to find the number that should go in place
#find potential answers from the numbers that it can't be
def potAns(badNums):
    potNums = {}
    for i in range(0,9):
        for j in range(1,10):
            if(j not in badNums[i] and badNums[i] != []):
                if(i not in potNums):
                    potNums[i] = [j]
                else:
                    potNums[i].append(j)          
    print("potential answers")
    print(potNums)

#---------------------------------------------------------------------------------------------------------    
#solve the 3x3 
def sudSolv(board, curSeq):
    print("in sudSolv")
    #get the middle of a 3x3 square
    #get the 3x3 of the first square to solve
    #center of square 1 is 1,1
    #create an array that will house the 9 numbers from a 3x3 

    #for j in range(0,3):
    #    for k in range(0,3):
    #        solvSeq.append(board[j][k])
    badnums = noNumDict(board)
    #potAns(badnums)
    #increment square
    #return solved board
    #UPDATE board TO SOLVED BOARD VARIABLE
    return board
    '''compareSeq = [1,2,3,4,5,6,7,8,9]
    #compare the spots for 
    ordSeq = solvSeq.copy()
    ordSeq.sort()
    print("after ordSeq, solvSeq =", solvSeq)
    while(ordSeq != compareSeq):
        for pos in range(0,9):
            passed = False
            if(solvSeq[pos] == 0):
                while(passed == False):
                    print("=========================================")
                    print("cur pos = ", pos)
                    print("cur solvSeq[pos]", solvSeq[pos])
                    solvSeq[pos] += 1
                    print("sending ", solvSeq[pos], "to sudChk")
                    passed, solvSeq = sudChk(board, solvSeq, pos)
                    print("after passed is returned",solvSeq)
                    print("passed = ", passed)'''
            
    #if(solvSeq.sort() == compareSeq):
    #    curSq += 1
    #    sudSolv(board,curSq)

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
for row in SodBoard:
    print(row)
boardSolved = sudSolv(SodBoard, 0)
print("Solved Board:")
for row in boardSolved:
    print(row)




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
#