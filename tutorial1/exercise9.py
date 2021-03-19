name = input("What is your name:") #User input/Variable
age = int(input("What is your age:")) #User input/Variable

print("Your name is " +name.capitalize()+ " and you are "+str(age)+" Years old") #Print statement/String Function,String concatenation
print("Your name is "+name.lower())
print("Your name is "+str(len(name))+" Characters Long")#print statement/string length

if age>=16: #If statement
    hasLicense = input("Do you have a drivers license?") #User input

else: #else statement
    print("You are too young to drive!")#print statement

decimalNumber = float(input("Now please enter a decimal number:"))
print("Your number is "+str(decimalNumber) +" As an integer its "+str(int(decimalNumber)))

if decimalNumber>100:
    print("Your number is Greater then 100")

elif decimalNumber==100:
    print("Your number is = to 100")

else:
    print("Your number is Less then 100")