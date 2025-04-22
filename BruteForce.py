##Brute Forcing Sodoku
'''
sodoku board consists of 9 3x3 squares 

2d array can be used to make the the sodoku board
    use mod3 to get the smaller 3x3 square 

brute force to solve
    scannby rows as the entire row can only be singleton (only 1 number in each row, no repeat numbers)

'''

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
        if(board[i][0] == curCub[pos] and curCub[i] != 0 and pos != i):
            print("Trigger 2")
            return (False, curCub)
    #horizontal
    for i in range(0,9):
        for j in range(0,9):
            if(board[i][j] == curCub[pos] and curCub[i] != 0 and pos != i):
                print("board[i][j] = ", board[i][j])
                print("curCub[pos] = ", curCub[pos])
                print("Trigger 3")
                return (False, curCub)
    print("else hit")
    return (True, curCub)
    
    

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
    compareSeq = [1,2,3,4,5,6,7,8,9]
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
                    print("passed = ", passed)
            
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