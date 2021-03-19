def show(c):
    '''Prints c to the screen.
       Pre-condition: len(c) is 1
    '''
    if len(c) != 1:
        print("BAD input to show()!")
    print(c, end='')

def triangleMaker(x:int):
    for y in range(1,x+1,1):
        for w in range(1,(x-y)+1,1):
                show(" ")
        for z in range(1,y+1,1):
            show(str(y))
        show("\n")
    


flag=0

while(flag==0):
    usrTri = int(input("Please enter an integer between 1 and 9: "))
    if(usrTri<1 or usrTri>9):
        print("The integer must be between 1 and 9, inclusively")
    else:
        triangleMaker(usrTri)
        answer = input("Would you like to draw another triangle (y/n)? ")
        if(answer=="y"):
            flag=0
        else:
            flag=1
            print("Goodbye.")