    
#sudoku to be solved
sudoku = [
    [4,0,0,0,0,1,7,0,0],
    [0,0,0,0,5,0,0,4,0],
    [0,1,0,9,0,2,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,4,0,0,5,3,0,0],
    [3,2,0,0,0,0,0,7,1],
    [7,8,1,4,0,0,0,0,0],
    [0,0,0,7,0,0,0,0,2],
    [0,9,0,0,0,0,0,3,0]
]

#function to print the board elegantly
def printBoard(sudoku):
    for row in range(len(sudoku)):
        print("")
        if row % 3 == 0:
            print("-----------------------------------------")
        for col in range(len(sudoku)):  
            if col == 0:
                print(end="           ")          
            if col % 3 == 0 and col != 0:
                print("|", end =" ")
            print(sudoku[row][col], end = " ")
    print("\n-----------------------------------------")

        
#finds spaces where there is an empty space(0)
def FindEmptySpace(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] == 0:
                return (i,j)
    return None

#checks whether value is already in its box
def isNumber_inBox(sudoku, row, col, value):

    box_row = row - row % 3 
    box_col = col - col % 3
    for i in range(3): 
        for j in range(3): 
            if(sudoku[i + box_row][j + box_col] == value): 
                return True
    return False
        

#checks whether value is already in its row
def isNumber_inRow(sudoku, row, value):
    for i in range(len(sudoku)):
        if sudoku[row][i] == value:
            return True
        
    return False

#checks whether value is already in its column
def isNumber_inCol(sudoku, col, value):
    for i in range(len(sudoku)):
        if sudoku[i][col] == value:
            return True
        
    return False

#checks whether value is valid in certain positon
def isNumberValid(sudoku, row, col, value):
    if (isNumber_inBox(sudoku, row, col, value) or isNumber_inCol(sudoku, col, value) or isNumber_inRow(sudoku, row, value)):
        return False
    else:
        return True

#solves sudoku
def execute(sudoku):
    
    if not FindEmptySpace(sudoku):
        return True

    else:  
        row,col = FindEmptySpace(sudoku)    
        for i in range(1, 10):
            if isNumberValid(sudoku,row, col, i):                
                sudoku[row][col] = i                       
                
                if execute(sudoku):
                    return True   

                sudoku[row][col]=0


    return False


                 0-
print("\nInput sudoku: ", end="")          
printBoard(sudoku)

if execute(sudoku):
    print("\n\nSolved sudoku: ",end="")       
    printBoard(sudoku)
    print("\n\n")
    
else:
    print("\n\nSudoku does not have a solution")



    
