def gradeCalculator(a:float, t:float, s:float, m:float, f:float) -> float:
    failureCase1Full = a*0.42 + t*0.08
    failureCase2Full = m*0.2 + f*0.25
    failureCase1 = (a*0.42 + t*0.08)/50
    failureCase2 = (m*0.2 + f*0.25)/45

    if(failureCase1 <0.5):
        if(failureCase2 <0.5):
            return min(failureCase1Full,failureCase2Full)
        else:
            return failureCase1Full    
    elif(failureCase2 <0.5):
        return failureCase2Full
    else:
        return a*0.42 + t*0.08 + m*0.2 + f*0.25 + s*0.05


print("Grade Calculator")
print("------------------------------------------------")
usrName = input("please enter your name : ")
print("------------------------------------------------")
assignmentGrade = float(input(usrName +", please enter your assignment grade : "))
tutorialGrade = float(input(usrName +", please enter your tutorial grade : "))
studyGrade = float(input(usrName +", please enter your study group grade : "))
midtermGrade = float(input(usrName +", please enter your midterms grade : "))
finalexamGrade = float(input(usrName +", please enter your final exam grade : "))
print("------------------------------------------------")

finalGrade = gradeCalculator(assignmentGrade,tutorialGrade,studyGrade,midtermGrade,finalexamGrade)
print(usrName+"'s Final Grade is "+str(finalGrade))