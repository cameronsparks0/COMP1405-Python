class Student:
    name=None
    id=None
    courses=[]

    def __init__(self,name_,id_,courses_):
        self.name=name_
        self.id=id_
        self.courses=courses_
    def __str__(self):
        return f'{self.name}, {self.id}, {self.courses}'

def computeAverage(student:Student):
    counter=0
    total=0
    if(len(student.courses)==0):
        return -1
    for x in student.courses:
        total=total+x[1]
        counter = counter +1
    return(total/counter)
        
def findByID(students,id):
    for x in students:
        if(int(x.id)==id):
            return x
    return None

def findByCourse(students,course):
    fullList=[]
    for x in students:
        for y in x.courses:
            if(y[0]==course):
                fullList.append(x)
    return fullList

def studentsInGradeRange(students, low, high):
    fullList=[]
    for x in students:
        average=computeAverage(x)
        if(average>=low and average<=high):
            fullList.append(x.name)
    return fullList



s1 = Student("Cam","32",[("Comp1405",90),("Comp1805",75)])
s2 = Student("Bob","45",[("Comp4207",56),("Comp1805",71)])
s3 = Student("Jim","48",[("Comp3401",67),("Comp4207",35)])
s = [s1,s2,s3]
#print(s1)
#print(computeAverage(s1))
#print(findByID(s,42))
#comp1805List= findByCourse(s,"Comp1805")
#print(studentsInGradeRange(s,53,100))