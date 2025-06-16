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
#Create a dictionary that can store all numbers that the cur pos CANNOT BE

def noNumDict(board, solvSq):
    noNoNums = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
    for pos in range(0,9):
        print("---------------CURRENT POSITION: ", pos, " ------------------------")
        if(solvSq[pos] == 0):
            for i in range(0,9):
                print("CURRENT pos = ", pos, "pos//3 = ", pos//3, " (pos+1)//3 = ", (pos+1)//3, "AND CURRENT i = ", i)
                #check the 3x3 for numbers
                print("checking solvSq[i] = ", solvSq[i])
                if(solvSq[i] != 0):
                    print("adding: ", solvSq[i])
                    noNoNums[pos].append(solvSq[i])
                #check across the current array our pos is in
                #do integer division to keep the correct array
                print("checking board[pos//3][i] = ", board[pos//3][i])
                if(board[pos//3][i] != 0 and board[pos//3][i] not in noNoNums[pos]):
                    print("adding: ", board[pos//3][i])
                    noNoNums[pos].append(board[pos//3][i])
                #keep the current pos and iterate down the arrays
                if(pos in [0,3,6]):
                    newpos = 0
                elif(pos in [1,4,7]):
                    newpos = 1
                elif(pos in [2,5,8]):
                    newpos = 2
                print("checking board[i][pos] = ", board[i][newpos])
                if(board[i][newpos] != 0 and board[i][newpos] not in noNoNums[pos]):
                    print("adding: ", board[i][newpos])
                    noNoNums[pos].append(board[i][newpos])
    print("cur dictionary of numbers that cannot be")
    print(noNoNums)
    return noNoNums

#---------------------------------------------------------------------------------------------------------
#use the dictionary to find the number that should go in place
#find potential answers from the numbers that it can't be
def potAns(badNums):
    potNums = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
    for i in range(0,9):
        for j in range(1,10):
            if(j not in badNums[i] and badNums[i] != []):
                potNums[i].append(j)         
    print("potential answers")
    print(potNums)

#---------------------------------------------------------------------------------------------------------    
#solve the 3x3 
def sudSolv(board, curSq):
    print("in sudSolv")
    if(curSq == 10):
        return board
    #get the middle of a 3x3 square
    #get the 3x3 of the first square to solve
    #center of square 1 is 1,1
    #create an array that will house the 9 numbers from a 3x3 
    solvSeq = []
    for j in range(0,3):
        for k in range(0,3):
            solvSeq.append(board[j][k])
    print("cur solvSeq", solvSeq)
    badnums = noNumDict(board, solvSeq)
    potAns(badnums)
    #increment square
    curSq += 1
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
print("first 3x3")
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