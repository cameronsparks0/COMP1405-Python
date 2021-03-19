# process.py
# --------------
# COMP1405A - Fall2020


## Student: Cameron Sparks
## ID: 101181932
## Comments:
##
##
##
##



# Make sure the data.csv file is saved in the same directory as this file.
# If you are using VS Code, you must change the settings so that it can find 
# the file when it tries to open it.
# Go to Preferences -> Settings
#       Once in Settings, use the search bar to search for InFileDir
#       Check the box for  "Python -> Terminal : Execute In File Dir"



####
####  add your functions above the main method
####


def findByDomain(domain:str, data:list) -> list: 
    dataEnd = []
    x=0
    while(x<len(data)):
        dataN = data[x].split(",")
        name = dataN[0]
        count = 0
        for y in dataN:
            if(domain in y):
                count = count + 1
        if(count > 0):
            tempString = name + ":" + str(count)
            dataEnd.append(tempString)
        x = x + 1
    return dataEnd

def emailsByAge(lower:int, upper:int, data:list) -> list:
    Out = []
    x=0
    while(x<(upper-lower+2)):
        z=0
        if(x==0):
            Out.append(lower)
        else:
            countEmail=0
            count=0
            while(z<len(data)):
                dataN = data[z].split(",")
                age = dataN[1]
                if(age is ""):
                    pass
                elif(float(age)==(lower+x-1)):
                    count = count + 1
                    for y in dataN:
                        if(y.count("@")):
                            countEmail = countEmail + 1
                z = z + 1
            if(count>0):
                Out.append(countEmail/count)
            else:
                Out.append(0)
        x = x + 1
    return Out

        




# This function controls the program
def main():
    fname = 'data.csv'           # filename
    
    print("...opening file " + fname + " for reading")
    file = open(fname, 'r')      # open the file for reading

    print("...reading contents of file")
    data = file.readlines()      # read entire contents of file into list of strings
                                 # each line in the file is one string

    print("...closing file " + fname)
    file.close()                 # close the file now that we are done with it

    print(findByDomain("carleton",data))
    print(emailsByAge(7,15,data))

    #print("...data is...")
    #for line in data:
        #print(line, end='')

    ##
    ## data now has a list as needed for your functions.
    ##

    ## test your findByDomain() and emailsByAge() functions
    #users = findByDomain('carleton.ca', data)
    #print(users)
    #stats = emailsByAge(10,20,data)
    #print(stats)




###########################################################################
#
# Do NOT change the code below this
#
###########################################################################

# This if statement is needed so that when you "run" this program it will 
# automatically call the main function.
# If you load this function as a module it will not call main()
if __name__ == "__main__":
    main()