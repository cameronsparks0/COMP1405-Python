import random

surnames = ['Davis', 'Johnson', 'Rodriguez']
given = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', "I", 'J']

class Student:
    def __init__(self, surname, given_name, id, courses):
        self.surname = surname
        self.given_name = given_name
        self.id = id
        self.length = len(surname)
        self.courses = courses
    def __repr__(self):
        return f'<{self.surname}, {self.given_name}: {self.id}>'
    def __str__(self):
        return f'<{self.surname}, {self.given_name}: {self.id}>'

def sur_key(s):
    return s.surname

def len_key(s):
    return s.length

def insertion_sort(s):
    for index in range(1, len(s)):
        #invariant: s[:index] is sorted

        # insert next s into sorted part
        pos = index
        while pos >= 1 and s[pos-1].id > s[pos].id:
            # swap s[pos-1] and s[pos]
            tmp = s[pos].id
            s[pos].id = s[pos-1].id
            s[pos-1].id = tmp
            pos -= 1
    return s

def selection_sort(s):
    for index in range(len(s)):
        # invariant: values[:index] is sorted
        # select minimum value remaining
        minPos = index
        for pos in range(index+1, len(s)):
            if s[pos].surname < s[minPos].surname:
                minPos = pos
            elif s[pos].surname == s[minPos].surname:
                if s[pos].given_name < s[minPos].given_name:
                    minPos = pos

        # put this element into the sorted part
        tmp = s[index].surname
        s[index].surname = s[minPos].surname
        s[minPos].surname = tmp 

def sortBySurname(s):
    s.sort(key=sur_key)

def sortByLength(s):
    s.sort(key=len_key)


# build a list of n students
n = 6
students = [Student(f'{surnames[i%len(surnames)]}', f'{given[i%len(given)]}', random.randint(0,1000), []) for i in range(n)]

print('before', students)
sortByLength(students)
print('after ', students)