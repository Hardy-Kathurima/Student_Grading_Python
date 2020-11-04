# This application accepts user input, calculates average marks and determines the grade.The results are saved in a text file.
# create a class to store each student info
class Student:

    def __init__(self,f_name,l_name,email,admission,level):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.admission = admission
        self.level = level
# A function to calculate average score
    def grade(self,English,Kiswahili,Maths,Physics,Chemistry):
        total = English + Kiswahili + Maths + Physics + Chemistry
        average = total //5
        return average
# Accepting user data
while True:
    header = '****This application  calculates student average marks and save the results in text a file****'
    print(header)
    user = input("Do you want to calculate student average marks? (y/n): ")
    if user == 'y':
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        email = input("Enter email: ")
        admission = input("Enter admission: ")
        level = input("Enter level: ")

        divider = '*'
        print(divider*50)
# validating user input
        while True:
            try:
                english = int(input("\033[1;32;40m Marks Scored in English: "))
            except ValueError:
                print('\033[31m' + 'please enter valid english marks in digits')
            try:
                maths = int(input("\033[1;32;40m Marks Scored in Maths: "))
            except ValueError:
                print('\033[31m' + 'please enter valid maths marks in digits')
            try:
                kiswahili = int(input("\033[1;32;40m Marks Scored in Kiswahili: "))
            except ValueError:
                print('\033[31m' + 'please enter valid kiswahili marks in digits')
            try:
                physics = int(input("\033[1;32;40m Marks Scored in Physics: "))
            except ValueError:
                print('\033[31m' + 'please enter valid physics marks in digits')
            try:
                chemistry = int(input("\033[1;32;40m Marks Scored in Chemistry: "))
            except ValueError:
                print('\033[31m' + 'please enter valid chemistry marks in digits')

            else:
                break
        divider2 = '*'
        print(divider2*50)
# output data
        student1 = Student(firstName,lastName,email,admission ,level)
        print(f'NAME: {student1.f_name} - {student1.l_name}' )
        print(f'EMAIL: {student1.email}')
        print(f'ADMISSION: {student1.admission}')
        print(f'LEVEL: {student1.level}')
        meanGrade = student1.grade(english,maths,kiswahili,physics,chemistry)
        print(f'Mean Grade: {meanGrade}')
# open write and save input data in a text file
        with open('results.txt','a') as write_file:
            if meanGrade >=70:
                result ='A'
            elif meanGrade >= 60 and meanGrade < 70:
                result = 'B'
            elif meanGrade >= 50 and meanGrade <60:
                result = 'C'
            elif meanGrade >= 40 and meanGrade <50:
                result = 'D'
            elif meanGrade <= 40:
                result = 'E'

            write_file.write(f'Name:{student1.f_name} {student1.l_name}   Points:{meanGrade}   Grade:{result}\n')
        if meanGrade >=70:
            print(f"{student1.f_name} scored an A")
        elif meanGrade >= 60 and meanGrade < 70:
            print(f"{student1.f_name} scored a B")
        elif meanGrade >= 50 and meanGrade <60:
            print(f"{student1.f_name} scored a C")
        elif meanGrade >= 40 and meanGrade <50:
            print(f"{student1.f_name} scored a D")
        elif meanGrade <= 40:
            print(f"{student1.f_name} scored an E")
        else:
            print("Invalid")

    else:
        break
