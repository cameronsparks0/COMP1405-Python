# Date: October 13th 2020
# Class: COMP1405A
# Semester: Fall
# Assignment: #2
# Name: Cameron Sparks
# encrypt function: Takes in a string, an amount to shift over and an alphabet. Uses these variables to encrypt the string and return this new string.
# passwordIsValid function: Takes in a string and performs multiple different checks to see if it fits the specified criteria for a password. It will return a true/false booleon based on the string
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def encrypt(message:str, shift:int, alphabet:str)-> str:
    '''Description of Function
    
    Parameters:
    message (str): A string that will be encrypted

    shift (int): An integer to specify how much the message's characters will shift over provided a given alphabet.

    alphabet (str): A string that will be used along with the shift integer to encrypt the message.

    returns:

    str: The encrypted message
    
     '''
    alphCharacter=0
    alphabetLength = len(alphabet)
    encodedMessage=""

    for messageCharacter in message:
        while messageCharacter != alphabet[alphCharacter]: #Running a loop while x is not equal to alphabet at index alphCharacter. This is to find the alphCharacter index value that corresponds to the given alphabet character that matches x(or the character in the given string)
            alphCharacter = alphCharacter+1

        if(messageCharacter==alphabet[alphCharacter]): #Once x is equal to alphabet at index alphCharacter, that means alphCharacter corresponds to the correct alphabet and message character. Therefore we can begin to manipulate numbers with it.
            if((alphCharacter+shift)>(alphabetLength-1)): # Checking if the shifted amount will be larger then the last index of alphabet, if it is the code bellow figures out an equivalent to this index. This is to make sure the code doesn't crash later on as it would be an index out of range.
                tempStore = (alphCharacter+shift)-alphabetLength
                while tempStore>alphabetLength-1: #A while loop to keep subtracting the alphabet length off of a shifted amount greater then the alphabet length. This is to find a lesser equivalent to its index value.
                    tempStore = tempStore-alphabetLength
                shiftOver = tempStore

            elif((alphCharacter+shift)<0): 
                if((alphCharacter+shift)<-alphabetLength): # Checking if the shifted amount will be lesser then the negative length of the alphabet, if it is the code bellow figures out an equivalent to this index. This is to make sure the code doesn't crash later on as it would be an index out of range.
                    tempStore = (alphCharacter+shift)+alphabetLength
                    while(tempStore<-alphabetLength): #A while loop to keep adding the alphabet length onto a shifted amount lesser then the negative alphabet length. This is to find a greater equivalent to its index value.
                        tempStore = tempStore+alphabetLength
                    shiftOver = tempStore
                else:
                    shiftOver = alphabetLength+(alphCharacter+shift)

            else:
                shiftOver = alphCharacter+shift

            encodedMessage = encodedMessage + alphabet[shiftOver]
            alphCharacter=0

    return encodedMessage

def passwordIsValid(passwd : str) -> bool:
    '''Description of Function
    
    Parameters:
    passwd (str): A string being tested to see if it fits the valid criteria

    CRITERIA FOR PASSWD:
    All strings must be at least 5 characters long
    All strings must have at least two digits in it (0,1,2,...,9)
    All strings must have at least one special character in it (!@#$%^_.)
    All strings must have at least one uppercase letter
    All strings must have at least one lowercase letter
    All strings must start with either a letter or an underscore

    returns:
    bool: A true or false value whether or not the string fit the criteria.
    
     '''

    flag=0
    if len(passwd)<5:
        return False

    for passCharacter in passwd:
        if passCharacter.isdigit():
            flag+=1
    if flag < 2:
        return False
    flag=0

    for passCharacter in passwd:
        if passCharacter.isdigit()==False and passCharacter.isalpha()==False:
            flag+=1
    if flag<1:
        return False
    flag=0

    for passCharacter in passwd:
        if passCharacter.isupper():
            flag+=1
    if flag<1:
        return False
    flag=0

    for passCharacter in passwd:
        if passCharacter.islower():
            flag+=1
    if flag<1:
        return False
    flag=0

    if((passwd[0].isalpha()==False) and (passwd[0]!="_")):
        print("Hello")
        return False
    
    return True




print(encrypt("hello",-39,"eloh"))
print(passwordIsValid("_TEsT22!"))

