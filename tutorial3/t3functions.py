def factorialWhile(n:int) -> int:
    factorialTotal = 1
    if(n!=0):
        while(n>1):
            factorialTotal = factorialTotal * n
            n = n -1
        return factorialTotal
    else:
        return 1

def factorialFor(n:int) -> int:
    factorialTotal = 1
    if(n!=0):
        for x in range(n,1,-1):
            factorialTotal = factorialTotal * x
        return factorialTotal
    else:
        return 1

def numberOfVowels(word:str):
    numVowels = 0
    for x in word:
        if x.lower() in "aeiou":
            numVowels = numVowels + 1
    print("Your number of vowels in this string is: "+ str(numVowels))






nFactorial = int(input("Please enter a positive integer: "))
print(str(factorialWhile(nFactorial)))
print(str(factorialFor(nFactorial)))

word = input("Please Enter a string: ")
numberOfVowels(word)

