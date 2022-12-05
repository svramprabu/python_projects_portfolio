def find_next_empty(puzzle):
    #finds next empty box to fill or filled with -1 which is the empty spot in our list of lists
    #return row, col tuple or (None, None) if there is no empty spaces

    #lets begin our search
    for r in range(9): #since we r using 0 based index our range 0-8
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c 
    return None,None

def is_valid(puzzle, guess, row, col):
    #return True if it's a valid placement else False

    #What is valid?
    #it should not repart in row or col or inside that box
    row_vals=puzzle[row] #checking for row
    if guess in row_vals:
        return False
    col_vals=[puzzle[i][col] for i in range(9)] #to check in column
    if guess in col_vals:
        return False
    #to check the square but it's tricky & we need to find where this small square starts
    row_start=(row // 3) * 3    #gives the floor value i.e if row/col is 5 it will give 1 as ans and 
    col_start=(col // 3) * 3    #multiplying it by 3 gives the square number

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if guess is puzzle[r][c]:
                return False
    return True

def solve_sudoku(puzzle):
    #this solves and we are inputting list of list 9x9 puzzle
    #return if solution exists 
    #the question i.e the list mutated ot solve the puzzle
    
    #step 1 to choose a starting point of solution since we r using a powerful comp we can brute force and backtrack 
    row, col= find_next_empty(puzzle)
    #step 1.1 if None is return we check for validation and as we allowed only valid inputs in each box
    if row is None:
        return True
    
    #step 2 to place a number in that empty box 
    for guess in range(1,10):
        #step 3 check if it's valid
        if is_valid(puzzle, guess, row, col):
            #step 3.1 place it ont he puzzle
            puzzle[row][col] = guess
            #now recurse puzzle with this mutated list of list
            #step 4
            if solve_sudoku(puzzle):
                return True
            #step 5 if invalid or if our does not solve the problem, 
            # backtrack and retry with new number
        puzzle[row][col] = -1 #resetting the value at row and column

        #if none of the number work then this puzzle is unsolvable
    return False

if __name__ == '__main__':
    board=[ [_,_,_, _,_,_, _,_,_]      #replace the _ in list of list with the question puzzle and get ur answers
            [_,_,_, _,_,_, _,_,_]
            [_,_,_, _,_,_, _,_,_]

            [_,_,_, _,_,_, _,_,_]
            [_,_,_, _,_,_, _,_,_]
            [_,_,_, _,_,_, _,_,_]

            [_,_,_, _,_,_, _,_,_]
            [_,_,_, _,_,_, _,_,_]
            [_,_,_, _,_,_, _,_,_]]
    print(solve_sudoku(board))
    print(board)







