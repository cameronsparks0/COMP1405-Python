
def display(d:dict):
    for x in d:
        print(x+", "+str(d[x]))

def safeAdd(d, k, v, unsafe=False):
    choice = ""
    if(unsafe == False):
        d[k] = v
    else:
        if(k in d):
            print("The key "+k+" is already in the dictionary")
            choice = input("Current value  is "+str(d[k])+". Do you want to replace this value with "+str(v)+"? [yes/no]: ")
            if(choice.lower() == "yes"):
                d[k] = v

def merge1(d1,d2)-> dict:
    for x in d2:
        d1[x]= d2[x]
    return d1

def merge2(d1,d2)-> dict:
    for x in d2:
        if(x in d1):
            print(d1[x])
            d1[x] = [d1[x], d2[x]]
        else:
            d1[x]= d2[x]
    return d1

def top3(d:dict)->list:
    finalList=[]
    maximum=0
    key = ""
    counter=0
    while(counter<3):
        for x in d:
            if(d[x] > maximum):
                maximum = int(d[x])
                key = x
        finalList.append([maximum,key])
        d.pop(key)
        counter = counter + 1
        maximum=0
        
    return(finalList)

def main():
    d1= {"A":1, "B":2, "C":3}
    d2= {"A":4, "B":5, "C":6}
    d4= {'a': 100, 'b': 400, 'c':300, 'd': 500, 'e':250}
    #safeAdd(d1, "C", 4, True)
    #display(d1)
    #d3 = merge1(d1,d2)
    #display(d3)
    #d3 = merge2(d1,d2)
    #display(d3)
    big3 = top3(d4)
    print(big3)

if __name__ == "__main__":
    main()