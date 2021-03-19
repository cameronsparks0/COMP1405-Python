def show(c):
    '''Prints c to the screen.
       Pre-condition: len(c) is 1
    '''
    if len(c) != 1:
        print("BAD input to show()!")
    print(c, end='')

def ezDash(x:int):
    for y in range(1,x+1,1):
        show("-")
    show("\n")


def triangleMaker(x:int):
    for y in range(1,x+1,1):
        for w in range(1,(x-y)+1,1):
                show(" ")
        for z in range(1,y+1,1):
            show("Q")
        show("\n")

    ezDash(x)

    for y in range(1,x+1,1):
        for z in range(1,y+1,1):
            show("Q")
        show("\n")

    ezDash(x)

    for y in range(x+1,1,-1):
        for z in range(1,y,1):
            show("Q")
        show("\n")

    ezDash(x)

    for y in range(x+1,1,-1):
        for w in range(1,(x+2)-y,1):
                show(" ")
        for z in range(1,y,1):
            show("Q")
        show("\n")
    


while(1==1):
    usrTri = int(input("Enter a number: "))
    if(usrTri<=1):
        print("Goodbye.")
        break
    else:
        triangleMaker(usrTri)