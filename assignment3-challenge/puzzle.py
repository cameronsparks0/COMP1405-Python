import sudoku

def main():
    '''Description of Function
    Uses the functions of sudoku.py to create a playable version of sudoku.
    Works for any n^2 * n^2 grid (for any integer n>1)
     '''
    sudokuGame=input("Please enter your sudoku puzzle file: ") 
    puzzle = sudoku.load_puzzle(sudokuGame) #The google sheets csv files seem to work, but some csv generators seem to add extra things that break the given load_puzzle function.
    invalidMoveCounter=0
    totalMoveCounter=0
    previousMove=0
    isSolved=1
    while(1==1):
        print("Current Grid:")
        print(sudoku.puzzle_to_string(puzzle))
        usrMove=input("Enter move row/col/number(Use commas to seperate)(quit to exit): ")
        if(usrMove.lower())=="quit":
            break
        else:
            usrMove = usrMove.split(",")
        previousMove = puzzle[int(usrMove[0])][int(usrMove[1])] #Storing the previous move incase of an invalid placement
        puzzle[int(usrMove[0])][int(usrMove[1])] = int(usrMove[2])
        if(sudoku.check_columns(puzzle)!=[] or sudoku.check_rows(puzzle)!=[] or sudoku.check_subgrids(puzzle)!=[]): #Checking each condition of whether the new move is invalid or not
            print("That is invalid!")
            invalidMoveCounter = invalidMoveCounter + 1
            totalMoveCounter = totalMoveCounter + 1
            puzzle[int(usrMove[0])][int(usrMove[1])] = previousMove #Setting the specific puzzle value back to its original as the replacement was invalid
        else:
            totalMoveCounter = totalMoveCounter + 1

    print("Game has ended!")
    for zeroChecker in range(0,len(puzzle)):
        if(0 in puzzle[zeroChecker]):
            isSolved=0
    if(isSolved==1):
        print("Puzzle is complete!")
    else:
        print("Puzzle is not complete!")
    print("You entered "+str(totalMoveCounter)+" Numbers in total")
    print("You entered "+str(invalidMoveCounter)+" Invalid Numbers in total")
        
        
if __name__ == "__main__":
    main()