def celsiusToFarenheit():
    print("\n")
    temperatureC = float(input("Value in Celsius to convert: "))
    temperatureF = (temperatureC * 9/5) +32
    print(str(temperatureC)+"°C = "+str(temperatureF)+"°F")
    print("Goodbye "+name)
    print("---------------------------------------------------------")

def gradeConvert():
    print("\n")
    grade = int(input("Grade percentage to convert: "))
    if(grade >= 80):
        print(str(grade)+" = A")
    elif(grade >= 70 and grade < 80):
        print(str(grade)+" = B")
    elif(grade >= 60 and grade < 70):
        print(str(grade)+" = C")
    elif(grade >= 50 and grade < 60):
        print(str(grade)+" = D")
    elif(grade < 50):
        print(str(grade)+" = F")
    print("Goodbye "+name)
    print("---------------------------------------------------------")

def feetToInch():
    print("\n")
    feet = float(input("Feet to convert : "))
    print (str(feet)+" Feet = "+str(feet*12)+" Inches")
    print("Goodbye "+name)
    print("---------------------------------------------------------")
def metToPar():
    print("\n")
    met = float(input("Meters(s) to convert : "))
    print (str(met)+" Meter(s) = "+str(met/30856775814913700)+" Parsec(s)")
    print("Goodbye "+name)
    print("---------------------------------------------------------")
def wattToJoule():
    print("\n")
    watt = float(input("Watt-Hour(s) to convert : "))
    print (str(watt)+" Watt-Hour(s) = "+str(watt*3600)+" Joules")
    print("Goodbye "+name)
    print("---------------------------------------------------------")


name = input("Please enter your name: ")
print("Hello "+name+", welcome to the unit converter\n")
print("Please choose the type of unit conversion you would like")
print("1 - Convert Celsius To Fahrenheit")
print("2 - Percent to letter grade")
print("3 - Feet to inches")
print("4 - Meters to Parsecs")
print("5 - Watt-hour to Joule")
print("\n")
choice = int(input("Choice: "))
if(choice == 1):
    celsiusToFarenheit()

elif(choice == 2):
    gradeConvert()

elif(choice == 3):
    feetToInch()

elif(choice == 4):
    metToPar()

elif(choice == 5):
    wattToJoule()

exit()