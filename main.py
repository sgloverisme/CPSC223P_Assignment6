from people import Student
from people import Faculty

f = []
f.append(Faculty('Susan', 'Barua', 'Computer Science'))
f.append(Faculty('Hossein', 'Moini', 'Mechanical Engineering'))
f.append(Faculty('Huda', 'Munjy', 'Civil Engineering'))
f.append(Faculty('Mostafa', 'Shiva', 'Electrical Engineering'))

s = []
std1 = Student('Erica', 'Perine')
std1.set_class('Freshman')
std1.set_major('Civil Engineering')
std1.set_advisor(f[2])
s.append(std1)
std2 = Student('Jonathan', 'Rosso')
std2.set_class('Senior')
std2.set_major('Computer Science')
std2.set_advisor(f[0])
s.append(std2)
std3 = Student('Samuel', 'Carter')
std3.set_class('Sophomore')
std3.set_major('Environmental Engineering')
std3.set_advisor(f[2])
s.append(std3)
std4 = Student('Stephanie', 'Dalaba')
std4.set_class('Senior')
std4.set_major('Electrical Engineering')
std4.set_advisor(f[3])
s.append(std4)
std5 = Student('Chuck', 'Pirards')
std5.set_class('Junior')
std5.set_major('Mechanical Engineering')
std5.set_advisor(f[1])
s.append(std5)
std6 = Student('Becky', 'Hanna')
std6.set_class('Senior')
std6.set_major('Computer Science')
std6.set_advisor('George Kiran')
s.append(std6)


while(True):
    print("      *** TUFFY TITAN STUDENT/FACULTY MAIN MENU")
    print("1. Add Faculty")
    print("2. Print Faculty")
    print("3. Add Student")
    print("4. Print Faculty")
    print("9. Exit the program")
    print()
    choice = int(input("Enter menu Choice: "))
    if choice == 1:
        fn = input("Enter first name: ")
        ln = input("Enter last name: ")
        dp = input("Enter department: ")
        f.append(Faculty(fn, ln, dp))
    elif choice == 2:
        print("======================= FACLUTY =======================")
        print("Record  Name                  Department")
        print("======  ====================  =========================")

        for  i, x in enumerate(f):
            print(f'{str(i):8}{x.firstname + " " + x.lastname:22}{x.department:25}')

        print ()
    elif choice == 3:
        fn = input("Enter first name: ")
        ln = input("Enter last name: ")
        c = input("Enter class year: ")
        m = input("Enter major: ")
        fa = input("Enter faculty advisor: ")
        std = Student(fn, ln)
        std.set_class(c)
        std.set_major (m)
        std.set_advisor(fa)
        s.append(std)
    elif choice == 4:
        print("===================================== STUDENTS ======================================")
        print("Name                  Class      Major                      Advisor")
        print("====================  =========  =========================  =========================")

        for y in s:
            print(f'{y.firstName+" "+ y.lastname:22}{y.classyear:11}{y.major:27}{y.advisor.firstname+" "+y.advisor.lastname:20}')
        print()

    elif choice == 9:
        break;