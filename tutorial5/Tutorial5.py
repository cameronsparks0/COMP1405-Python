def isRectangle(matrix:list)->bool:
    start = len(matrix[0])
    flag=True
    for x in matrix:
        if(len(x)!= start):
            flag=False
    return flag

def isNumericalHelper(stringList:list)->bool:
    flag=True
    for x in stringList:
        if(x.isdigit() == False):
            if(x.isalpha()==True):
                flag=False
            elif(x in ["!","@","#","$","%","^","&","*","(",")","-","=","[","{","]","}","|",":",";","'",'"',",","<",".",">","/","?","\""]):
                flag=False
    return flag

def isMatrix(matrix:list)->bool:
    flag=True
    if(isRectangle(matrix)==False):
        flag=False
    else:
        for x in matrix:
            if(isNumericalHelper(x)==False):
                flag=False
    return flag

def getLargestNumber(matrix:list)->int: #Helper Function
    maximum=0
    for x in range(0,len(matrix)):
        for y in matrix[x]:
            temp = int(len(y))
            if(temp>maximum):
                maximum=temp
    return maximum

def getLargestEndNumber(matrix:list)->int: #Helper Function
    maximum=0
    for x in range(0,len(matrix)):
        for y in range(0,len(matrix[0])):
            if(y==len(matrix[0])-1):
                temp=int(len(matrix[x][y]))
                if(temp>maximum):
                    maximum=temp
    return maximum

def printMatrix(matrix:list):
    if(isMatrix(matrix)==False):
        print("Not a matrix")
    else:
        width = getLargestNumber(matrix)+1
        endVariableWidth = getLargestEndNumber(matrix)+1
        for x in matrix:
            counter=1
            print("| ",end="")
            for y in x:
                if(counter==len(matrix[0])):
                    print(y,end="")
                    for z in range(0,endVariableWidth-len(y)):
                        print(" ",end="")
                else:
                    print(y,end="")
                    for z in range(0,width-len(y)):
                        print(" ",end="")
                counter = counter + 1
            print("|")

def loadMatrix(filename):
    matrix = [] 
    with open(filename, "r") as f:
        for line in f:
            matrix.append( [int(val) for val in line.split(",")] )
    for x in range(0,len(matrix)):
        for y in range(0,len(matrix[x])):
            matrix[x][y] = str(y)
    return matrix







def main():
    print(isRectangle([["0","1"],["2","3","4"]]))
    print(isNumericalHelper(["0","@","-13"]))
    print(isMatrix([["0","1"],["-3","3"]]))
    matrix = loadMatrix("test.csv") # Gonna need to add your own csv file if I can only upload the Tutorial5.py
    printMatrix(matrix)


if __name__ == "__main__":
    main()