class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Faculty(Person):
    def __init__(self, fname, lname, dept):
        super().__init__(fname, lname)
        self.department = dept

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    def set_class(self, c):
        self.classyear = c
    def set_major(self, m):
        self.major = m
    def set_advisor(self, a):
        self.advisor = a