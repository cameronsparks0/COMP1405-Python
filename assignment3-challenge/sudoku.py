import math
'''
COMP 1405 - Fall 2020
Assignment #3

Name: Cameron Sparks
ID: 101181932
Comments: None
'''


#------------------------------------------------------------------#
# provided function - do NOT remove or change
def load_puzzle(filename):
    ''' Reads a sudoku puzzle from the text file 'filename' in the current directory. 
        Returns a list of lists of integers that represents the game.
            load_puzzle(filename:str) -> str[str[int]]
        Empty cells in the game are denoted by 0s in the file (and the output list)
    '''
    puzzle = [] 
    with open(filename, "r") as f:
        for line in f:
            puzzle.append( [int(val) for val in line.split(",")] )
    return puzzle
#------------------------------------------------------------------#
#------------------------------------------------------------------#
# your functions go here!

def largest_puzzle_val(puzzle:list)->int:
    '''Description of Function
    Takes a list of integers that represent a sedoku puzzle and returns the amount of characters in the largest number.
    Parameters:
    puzzle (list): A list of integers that make up a (n^2 * n^2) grid of sedoku.

    returns:
    int: The amount of characters in the largest string.
     '''
    maximum=0
    for x in range(0,len(puzzle)):
        for y in puzzle[x]:
            if(y>maximum):
                maximum = y
    return len(str(maximum))


def puzzle_to_string(puzzle:list) -> str:
    '''Description of Function
    Takes a list of integers that represent a sedoku puzzle and returns the string visualization of the puzzle.
    Parameters:
    puzzle (list): A list of integers that make up a (n^2 * n^2) grid of sedoku.

    returns:
    str: A string representation of the input puzzle.
     '''
    sqrLength = math.sqrt(len(puzzle)) # Used to figure out where Lines are being placed
    xAxis = int(len(puzzle)) #Getting the length of the xAxis without the lines(|) or spaces
    yAxis = int(len(puzzle) + sqrLength-1) #Getting the length of the yAxis with lines
    yRow = 0 #Keeping track of which row the program is currently drawing
    rowPosition=0 #Keeping track of which column to draw (index related)
    counter = 1 #Keeping track of which column the program is currently attempting to draw and used to in trying to find if a line should be drawn instead (non index related)
    outputString="" #Final String to be returned
    minSpace = largest_puzzle_val(puzzle) #Due to some numbers being multiple characters we need to find the minimum amount of space each number needs to take up(If this is not used the whole puzzle is off balance with some row subgrids having more columns then others).
    xAxisCharacterTotal = 0 #Due to some numbers being multiple characters, having spaces afterwards and lines this keeps tracks of how many characters per row.
    lineLocations=[] #To keep track of specific index values where the lines are located

    for yAxisCount in range(0,yAxis):
        if ((yAxisCount+1) % (sqrLength+1)) !=0: #If the program is not where a horizontal line should be drawn, then begin printing the columns of the puzzle for that row. 
            while rowPosition < xAxis:
                if(counter % (sqrLength+1) !=0): #If the program is not where a vertical line should be drawn, then begin printing the single column value at that row.
                    if(puzzle[yRow][rowPosition]==0): #If a zero is entered in the puzzle, add spacing for it instead of printing zero.
                        for spacePadding in range(0,minSpace):
                            outputString = outputString + " "
                        outputString = outputString + " "
                    else: #If not zero then print the number and add the rest of the padding if needed (IE if the longest number is 3 characters and the current character is a 9, then print 9   )
                        outputString = outputString + str(puzzle[yRow][rowPosition])
                        for spacePadding in range(0,minSpace-len(str(puzzle[yRow][rowPosition]))):
                            outputString = outputString + " "
                        outputString = outputString + " "
                    counter = counter + 1
                    rowPosition = rowPosition +1
                else: #Printing the vertical line segments(Only one space after the line is used because it doesn't matter as the line will always be the same character length)
                    outputString = outputString + "| "
                    counter = 1
            if(yRow == 0): #After the first row is created, this finds and stores the position of the lines.
                xAxisCharacterTotal= len(outputString)-1
                for lineCheck in range(0,xAxisCharacterTotal):
                    if(list(outputString)[lineCheck]=="|"):
                        lineLocations.append(lineCheck+1)
            rowPosition=0
            counter = 1
            yRow = yRow + 1
        else: #Draw the horizontal lines and the +'s at the same positions of the vertical lines
            for lineCheck in range(0,xAxisCharacterTotal):
                if((lineCheck+1) in lineLocations):
                    outputString = outputString +"+"
                else:
                    outputString = outputString +"-"
        outputString = outputString + "\n"
    return outputString

def check_rows(puzzle:list ) -> list:
    '''Description of Function
    Takes a list of integers that represent a sedoku puzzle and returns a list of invalid rows(returns an empty list if valid).
    Parameters:
    puzzle (list): A list of integers that make up a (n^2 * n^2) grid of sedoku.

    returns:
    list: A list of invalid rows(returns an empty list if valid).
     '''
    maxDigit = len(puzzle) #Finding the maximum possible digit to later find digits that should not be in the puzzle
    outputList = [] #Final list with all the invalid rows being returned
    
    for yAxisCount in range(0,len(puzzle)):
        for xAxisCount in range(0,len(puzzle)):
            if(puzzle[yAxisCount][xAxisCount]>maxDigit or puzzle[yAxisCount][xAxisCount]<0): #Outputing invalid for rows with digits outside the range of the puzzle
                if(int(yAxisCount) not in outputList): #Making sure no duplicates of rows exist in the final list
                    outputList.append(yAxisCount)
            for xAxisCompare in range(0,len(puzzle)): #A comparison loop to find if two numbers are the same in a row
                if(xAxisCount != xAxisCompare): #Making sure both counters are not on the same number as that would trigger an invalid loop even when it shouldn't be.
                    if(puzzle[yAxisCount][xAxisCount]==puzzle[yAxisCount][xAxisCompare]):
                        if(puzzle[yAxisCount][xAxisCount]!=0): #If more then 1 empty space exists on the row, disclude it from being a possible invalid list entry.
                            if(int(yAxisCount) not in outputList):
                                outputList.append(yAxisCount)
    return outputList

def check_columns(puzzle:list ) -> list:
    '''Description of Function
    Takes a list of integers that represent a sedoku puzzle and returns a list of invalid columns(returns an empty list if valid).
    Parameters:
    puzzle (list): A list of integers that make up a (n^2 * n^2) grid of sedoku.

    returns:
    list: A list of invalid columns(returns an empty list if valid).
     '''
    maxDigit = len(puzzle) #This function runs nearly the same way the row one does, just with certain loops being changed around in nesting order
    outputList = []

    for xAxisCount in range(0,len(puzzle)):
        for yAxisCount in range(0,len(puzzle)):
            if(puzzle[yAxisCount][xAxisCount]>maxDigit or puzzle[yAxisCount][xAxisCount]<0):
                if(int(xAxisCount) not in outputList):
                    outputList.append(xAxisCount)
            for yAxisCompare in range(0,len(puzzle)):
                if(yAxisCount != yAxisCompare):
                    if(puzzle[yAxisCount][xAxisCount]==puzzle[yAxisCompare][xAxisCount]):
                        if(puzzle[yAxisCount][xAxisCount]!=0):
                            if(int(xAxisCount) not in outputList):
                                outputList.append(xAxisCount)
    return outputList

def check_subgrids(puzzle:list) -> list:
    '''Description of Function
    Takes a list of integers that represent a sedoku puzzle and returns a list of invalid subgrids(returns an empty list if valid).
    Parameters:
    puzzle (list): A list of integers that make up a (n^2 * n^2) grid of sedoku.

    returns:
    list: A list of invalid subgrids(returns an empty list if valid).
     '''
    sqrLength = int(math.sqrt(len(puzzle))) #Used in conjunction with the axis multiplers to space the x and y counters to specific parts of the puzzle.
    maxDigit=len(puzzle)
    subgridFinalList=[] #The list containing all subgrids
    invalidSubgrid=[] #The list containing all of the invalid subgrids - This is the final list that is returned
    xAxisMultiplier=0 #the x and y multipliers are used to shift the counter over by specific amounts in order to cover the entire puzzle(Covering and storing all subgrids).
    yAxisMultiplier=0
    tempSubgrid=[] #Used to store each subgrid individually before dumping onto the subgridFinalList

### Creating the list of all subgrids ##################################################
    for subgridCount in range(0,len(puzzle)): #Iterating over all possible subgrids
        if((subgridCount % sqrLength)==0 and subgridCount!=0): #Increasing the yAxisMultipler as the subgrid counter falls onto the next row of subgrids
            yAxisMultiplier = yAxisMultiplier+1
        if(xAxisMultiplier==sqrLength): #Setting the xAxisMultipler back to 0 as the subgrid counter falls onto the next row of subgrids
            xAxisMultiplier=0
        for subgridYAxisCount in range(0,sqrLength): #Iterating through subgrid x and y axises 
            for subgridXAxisCount in range(0,sqrLength):
                    tempSubgrid.append(puzzle[subgridYAxisCount+(sqrLength*yAxisMultiplier)][subgridXAxisCount+(sqrLength*xAxisMultiplier)]) #Creating each subgrid using its y and x axis counters along with their respective multipliers
        if(tempSubgrid!=[]):
            subgridFinalList.append(tempSubgrid) #Putting each subgrid into a list of combined subgrids
            tempSubgrid=[] #Making sure the next subgrid is being put into an empty list
        xAxisMultiplier= xAxisMultiplier+1
########################################################################################
### Creating the list of all invalid subgrids ##########################################
    for individualSubgrid in range(0,len(puzzle)): #Functions nearly the same as the column and row check but once again with different iterators
        for subgridElements in range(0,len(puzzle)):
            if(subgridFinalList[individualSubgrid][subgridElements]>maxDigit or subgridFinalList[individualSubgrid][subgridElements]<0):
                if(individualSubgrid not in invalidSubgrid):
                    invalidSubgrid.append(individualSubgrid)
            for subgridElementsCompare in range(0,len(puzzle)):
                if(subgridElements != subgridElementsCompare):
                    if(subgridFinalList[individualSubgrid][subgridElements]==subgridFinalList[individualSubgrid][subgridElementsCompare]):
                        if(subgridFinalList[individualSubgrid][subgridElements]!=0):
                            if(individualSubgrid not in invalidSubgrid):
                                invalidSubgrid.append(individualSubgrid)
    return invalidSubgrid

#------------------------------------------------------------------#
# Your "program" is driven by the main method
# Modify as needed to test your functions

def main():
    puzzle = load_puzzle('puzzle1.csv')
    #print(puzzle_to_string(puzzle))
    #print(check_rows(puzzle))
    #print(check_columns(puzzle))
    #print(check_subgrids(puzzle))

#------------------------------------------------------------------#
# Guard for main function - do NOT remove or change
if __name__ == "__main__":
    main()