def fileOpen(fileName:str)->list:
    '''Description of Function
    Takes in a string to be used as the file name for opening and reading a text file and returns a list of words that were in the file.
    Parameters:
    filename (str): The filename that is used by the function to access the associated textfile

    returns:
    allWordsInFile (list): The words that were in the file
    '''
    file=open(fileName,"r")
    allWordsInFile = []
    for wordLine in file:
        allWordsInFile.append(wordLine.strip()) #Stripping each word of newline characters and spaces so that finding spelling mistakes is possible in further code.
    file.close()
    return allWordsInFile

def fileOpenPunctuation(fileName:str)->list:
    '''Description of Function
    Takes in a string to be used as the file name for opening and reading a text file and returns a list of periods, newline characters and their associated index values.
    Parameters:
    filename (str): The filename that is used by the function to access the associated textfile

    returns:
    punctuationList (list): A list of periods and newline characters, along with their index values.
    '''
    file=open(fileName,"r")
    allwordsInFileBase = []
    for wordLine in file:
        allwordsInFileBase.append(wordLine) #First storing all of the words in a list to then search for periods and newline characters
    file.close()
    punctuationList = []
    allwordsInFileBase = loadPunctuation(allwordsInFileBase) # Using a helper function to return a list containing every word at different index values along with their .'s and \n's.
    for punctuationFinder in range(0, len(allwordsInFileBase)): #Checking for the different possible assortments of periods and \n's and then adding the ones found into a list with their index values.
        if("." in allwordsInFileBase[punctuationFinder] and "\n" in allwordsInFileBase[punctuationFinder]):
            tempList = [punctuationFinder,".\n"]
            punctuationList.extend(tempList)
        elif("." in allwordsInFileBase[punctuationFinder]):
            tempList = [punctuationFinder,"."]
            punctuationList.extend(tempList)
        elif("\n" in allwordsInFileBase[punctuationFinder]):
            tempList = [punctuationFinder,"\n"]
            punctuationList.extend(tempList)
    return punctuationList

def fileSave(filename:str, wordsToWrite:list):
    '''Description of Function
    Takes in a string to be used as the file name for opening and writing to a text file and a list of words to be written to the file.
    Note: This writing function is for saving the corrected text to a new txt file
    Parameters:
    filename (str): The filename that is used by the function to access the associated textfile
    wordsToWrite (list): A list of words that are used to write to the textfile
    '''
    file=open(filename,"w")
    for word in wordsToWrite:
        if("\n" in word): #Considering if a word is at the end of a line, so that the line below it starts at at the beginning.
            file.write(word)
        else:
            file.write(word+" ")
    file.close()

def fileWriteMyWords(filename:str, wordsToWrite:list):
    '''Description of Function
    Takes in a string to be used as the file name for opening and writing to a text file and a list of words to be written to the file.
    Note: This writing function is for saving words to the users personal txt file
    Parameters:
    filename (str): The filename that is used by the function to access the associated textfile
    wordsToWrite (list): A list of words that are used to write to the textfile
    '''
    file=open(filename,"w")
    for word in wordsToWrite:
        file.write(word+"\n")
    file.close()

def fileWriteMistakes(filename:str, wordsToWrite:list):
    '''Description of Function
    Takes in a string to be used as the file name for opening and writing to a text file and a list of words to be written to the file.
    Note: This writing function is for saving mistakes and their associated format to a txt file.
    Parameters:
    filename (str): The filename that is used by the function to access the associated textfile
    wordsToWrite (list): A list of words that are used to write to the textfile
    '''
    file=open(filename,"w")
    for mistakeLine in range(0,len(wordsToWrite)): #Accessing the specific mistake and its associated information to be written to each line of the file.
        for mistakeInfo in range(0,len(wordsToWrite[mistakeLine])):
            if(mistakeInfo != len(wordsToWrite[mistakeLine])-1):
                file.write(wordsToWrite[mistakeLine][mistakeInfo]+", ") #writing ,'s to seperate each piece of mistake information if the piece of information is not at the end of its line(list)
            else:
                file.write(wordsToWrite[mistakeLine][mistakeInfo])
        file.write("\n")
    file.close()

def loadPunctuation(wordList:list)->list:
    '''Description of Helper Function
    Takes in a list of words as input and outputs a new list without the space inbetween words, with each word having its own index position.
    Parameters:
    wordList(list): List of words, potentially containing spaces inbetween other words.

    returns:
    listOfTextWords: A list of words without spaces and each word having its own index position.
    '''
    listOfTextWords = []
    for wordLine in wordList:
        listOfTextWords.extend(wordLine.split(" "))
    return listOfTextWords

def loadWords(wordList:list)->list:
    '''Description of Helper Function
    Takes in a list of words as input and outputs a new list without the space inbetween words and newline characters/periods, with each word having its own index position.
    Parameters:
    wordList(list): List of words, potentially containing spaces inbetween other words and newline characters/periods.

    returns:
    listOfTextWords: A list of words without spaces and newline charcters/periods and each word having its own index position.
    '''
    listOfTextWords = []
    for wordLine in wordList:
        listOfTextWords.extend(wordLine.split())
    for word in range(0,len(listOfTextWords)):
        listOfTextWords[word] = listOfTextWords[word].strip(".")
    return listOfTextWords

def loadWordCorrecter(wordList:list)->list:
    '''Description of Helper Function
    Takes in a list of mistake strings(with their intended format) and outputs a list without spaces and commas
    Parameters:
    wordList(list): List of words, potentially containing spaces inbetween other words and commas.

    returns:
    finalList: A list of words without spaces and comas and each word having its own index position.
    '''
    finalList = []
    for wordCorrection in wordList:
        wordCorrection = wordCorrection.replace(" ","")
        finalList.append(wordCorrection.split(","))
    return finalList

def suggestionGiver(mistakeWord:list)->str:
    '''Description of Function
    Takes in a list of information corresponding to a specific mistake word and outputs suggestion words in a string
    Parameters:
    mistakeWord(list): A list containing the mistake word and all the suggestion words as well as their frequencies.

    returns:
    returnSuggestions: A string of possible suggestions
    '''
    suggestionListNumb = [] #To keep track of all the different frequencies each suggestion word has
    suggestionListWord = [] #To keep track of all the suggestion words
    for numberFinder in range(0,len(mistakeWord)):
        try:
            suggestionListNumb.append(mistakeWord[2+2*numberFinder]) #This will fetch every frequency in the list and append it to the new list
        except:
            pass
    suggestionListNumb = set(suggestionListNumb) #Turning it into a set to get rid of duplicate frequencies(The code furthur down doesn't need duplicates as it appends one frequency in one loop cycle).
    suggestionListNumb = list(suggestionListNumb)
    suggestionListNumb = sorted(suggestionListNumb, reverse=True) #Sorting the frequencies so the suggestion words can be sorted from most frequent to least frequent

    for numberFinder in suggestionListNumb:
        for wordFinder in range(0,len(mistakeWord)):
            if(numberFinder==mistakeWord[wordFinder]):
                suggestionListWord.append(mistakeWord[wordFinder-1]) #Appending the suggestion words from most to least frequent

    returnSuggestions = "[ " #Creating the final string with the suggestion words to be returned
    for x in suggestionListWord:
        returnSuggestions = returnSuggestions + x +", "
    returnSuggestions = returnSuggestions +"]"
    return returnSuggestions

def updateMistakes(mistakeList:list, correction:str, incorrectWord:str)->list:
    '''Description of Function
    Takes in the list of mistake words with their respective attached data, a correction word and the incorrectword being corrected.
    It outputs back an updated mistake list with the new suggestion word attached, or a frequency tally additioned.
    Parameters:
    mistakeList(list): A list containing all the mistake words and all the suggestion words as well as their frequency.
    correction(str): A suggestion word to be added to the mistakeList in some way.
    incorrectWord(str): The incorrect word that is being corrected.

    returns:
    mistakeList: An updated list of all mistake words with their respective attached data.
    '''
    replaceList = [] #For placing the specific sublist into (The sublist being the list containing the target incorrect word)
    replaceVal = 0 # Keeping track of the index value associated with the sublist
    newCorrectionFlag=0 #To signal if the correction is already associated with an incorrect word or not.
    for mistakeLine in range (0,len(mistakeList)):
        if(incorrectWord==mistakeList[mistakeLine][0]):
            replaceList = mistakeList[mistakeLine] #Grabbing the sublist containing the target incorrect word
            replaceVal = mistakeLine # Grabbing the index value of that sublist
    if(replaceList!=[]):#If the incorrect words sublist already exists in mistakelist, then either add 1 to a frequency if the suggestion words exists, or add the new suggestion word.
        for correctFinder in range(0, len(replaceList)):
            if(correction == replaceList[correctFinder]):
                newCorrectionFlag=1 #The correction word already exists, add one to the frequency
                replaceList[correctFinder+1] = int(replaceList[correctFinder+1]) +1
                replaceList[correctFinder+1] = str(replaceList[correctFinder+1])
        if(newCorrectionFlag==0): #The correction word does not exist, add it to the sublist
            newCorrection = [correction,"1"]
            replaceList.extend(newCorrection)
        mistakeList[replaceVal] = replaceList
    else:
        newIncorrectWord = [incorrectWord,correction,"1"] #If the incorrect word does not exist in any sublist, create a new sublist with the given correction.
        mistakeList.append(newIncorrectWord)
    
    return mistakeList

def spellCheck(wordList:list, givenWords:list, myWords:list, mistakeWords:list):
    '''Description of Function
    Takes in a list of possible incorrect words, a list of given correct words, a list of the users words and a list of incorrect words with their suggestion words and frequencies.
    Uses the four lists to allow the user to correct the spelling of the possible incorrect words and save their own words.
    Parameters:
    wordList(list): A list containing possible incorrect words
    givenWords(list): A list containing given correct words
    myWords(list): A list containing the users words
    mistakeWords(list): A list containing all the mistake words and all the suggestion words as well as their frequency.
    '''
    for word in range(0,len(givenWords)):
        givenWords[word] = givenWords[word].lower() #Making sure all words have the same case.
    for word in range(0,len(myWords)):
        myWords[word] = myWords[word].lower()
    for word in range(0,len(wordList)):
        mistakeSuggestions = "[No suggestions]" # The suggestions for a mistake will keep this string if there are no suggestions for that word
        wordList[word] = wordList[word].lower()
        if(wordList[word] not in givenWords): #Checking if every word in wordList is correct by comparing it to other lists.
            if(wordList[word] not in myWords):
                for possibleMistake in mistakeWords: 
                    if(wordList[word] == possibleMistake[0]): #Checking if the now incorrect word has any suggestions for correction
                        mistakeSuggestions= suggestionGiver(possibleMistake)
                potentialMistake = f'Potential mistake: {wordList[word]}      {mistakeSuggestions}'
                print(potentialMistake) #Letting the user know of any potential corrections if any
                correction = input("Action: ")
                if(correction !=""): #If the user is attempting to correct a word, update the mistakeWord list
                    incorrectWord = wordList[word]
                    wordList[word] = correction
                    mistakeWords = updateMistakes(mistakeWords, correction, incorrectWord)
                else: #If the user is happy with a word, add it to their myWords list and remove it from being an incorrect word.
                    myWords.append(wordList[word])
                    for wordRemover in range(0, len(mistakeWords)):
                        if(mistakeWords[wordRemover][0] == wordList[word]):
                            mistakeWords.remove(mistakeWords[wordRemover])
                            break

def main():
    ###Looking for and loading the 3 main files###
    givenWords = fileOpen("words.txt") 

    try:
        myWords = fileOpen("mywords.txt") #Using try and except blocks due to these files potentially not being there to begin with.
    except:
        myWords= []
    
    try:
        mistakeWords = fileOpen("mistakes.txt")
        mistakeList = loadWordCorrecter(mistakeWords)
    except:
        mistakeList= []
    ##############################################

    ###User inteface Section###
    commandState=True
    while(commandState==True):
        usrCommand = input("Enter Command: " )
        if "load " in usrCommand:
            try:
                textWords = fileOpen(usrCommand.split()[1]) #Loading the user entered file into a list of strings
                listOfTextWords = loadWords(textWords)
                listOfPunctuation = fileOpenPunctuation(usrCommand.split()[1]) #Also creating a list of .'s and \n's to put back into the listOfTextWords list to retain the structure of the orginial textfile.
            except:
                print("Please enter a valid text file!")
        elif "spell" in usrCommand:
            try:
                spellCheck(listOfTextWords, givenWords, myWords, mistakeList) # Calling the main spellcheck function to prompt the user into correcting the spelling of words.
            except:
                print("First load a file!")
        elif "save " in usrCommand:
            savingTextWords = list(listOfTextWords) # So that a duplicate is made instead of just using the same list under a different name.
            for x in range(0,len(listOfPunctuation)):
                if(str(listOfPunctuation[x]).isnumeric() == True): #Adding the .'s and \n's back into the list being saved
                    savingTextWords[listOfPunctuation[x]]= savingTextWords[listOfPunctuation[x]] + listOfPunctuation[x+1]
            fileSave(usrCommand.split()[1], savingTextWords) #Calling a function to save the list containing the corrected words into a user named file.
        elif "quit" in usrCommand:
            fileWriteMyWords("mywords.txt",myWords) #Writing the mywords and mistakes list into their seperate files.
            fileWriteMistakes("mistakes.txt",mistakeList)
            commandState=False
    ##############################################

if __name__ == "__main__":
    main()