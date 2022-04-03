import numpy as np 
import math
#init the list of students  the list of courses and the list of marks to store objects of class Student, Course and Mark
list_student = []
list_course = []
list_mark = []
gpa_student = {}
#init dictionary to store students marks in 1 course

#function to enter number of students of a given course
#effect: insert number of students
def input_no_students():
    while True:
        no_students = int(input('Enter the number of students of the course: '))
        if no_students <0:
            print('Invalid number of students!')
            print('Enter again!')
            continue
        else:
            return no_students

#function to enter number of courses
#effect: insert number of courses
def input_no_courses():
    while True:
        no_course = int(input('Enter the number of courses: '))
        if no_course <0:
            print('Invalid number of courses!')
            print('Enter again!')
            continue
        else:
            return no_course

class Person:
    def __init__(self,name,DoB):
        self._name = name
        self._DoB = DoB

class Student(Person):
    def __init__(self,name,DoB,id):
        super().__init__(name,DoB)
        self._id = id
    def add_student(self):#method to add a student object to list_student
        ob = Student(self._name,self._DoB,self._id)
        list_student.append(ob)
    
#function to show list_student
def show_list_student():
        print('List of students: ')
        for i in list_student:# i is a class 
            print('student_id: ',i._id,'\nstudent_name: ',i._name,'\nstudent_DoB: ',i._DoB)
            print('\n')

class Course:
    def __init__(self,id,name,credit):
        self._id = id
        self._name = name
        self._credit = credit
    def add_course(self):#method to add a course object to list_course
        ob_course = Course(self._id,self._name,self._credit)
        list_course.append(ob_course)
    
class Mark():
    def __init__(self,sid,cid,mark,credits):
        self._sid = sid
        self._cid = cid
        self._mark = mark
        self._credits = credits
    def add_mark(self):#method to add a mark object to list_mark
        ob_mark = Mark(self._sid, self._cid, self._mark,self._credits)
        list_mark.append(ob_mark)

#function to show list_marks
def show_list_mark():
        print('List of marks: ')
        for i in list_mark:
            print('student_id: ',i._sid,
            '\ncourse_id: ',i._cid,
            '\nmark: ',i._mark)
            print('\n')

#function to show list_course    
def show_list_course():
        print('List of courses: ')
        for i in list_course:
            print('course_id: ',i._id,'\ncourse_name: ',i._name,'\ncourse_credit: ',i._credit)
            print('\n')
        
#function to show marks of a course
def show_marks_1course(course_id):
            for i in list_mark:#i is objects of class Mark
                if i._cid == course_id:
                    print('student_id: ',i._sid,
                    '\ncourse_id: ',i._cid,
                    '\nmark: ',i._mark,
                    '\ncredits: ',i._credits)
                    print('\n')

#function to show a student'marks in all course
def show_marks_1student(student_id):
            for i in list_mark:
                if i._sid == student_id:
                    print('student_id: ',i._sid,
                    '\ncourse_id: ',i._cid,
                    '\nmark: ',i._mark,
                    '\ncredits: ',i._credits)
                    print('\n')


def update_marks_floor():
    for i in list_mark:
            i._mark = math.floor(i._mark)
            print('student_id: ',i._sid,
            '\ncourse_id: ',i._cid,
            '\nmark: ',i._mark)
            print('\n')

def arrmarks_1student(student_id):
    marks_a = np.array([i._mark for i in list_mark if i._sid == student_id])
    return marks_a

def arrcredits_1student(student_id):
    credits_a = np.array([i._credits for i in list_mark if i._sid == student_id])
    return credits_a

def cal_gpa(student_id):
    marks_a = arrmarks_1student(student_id)
    credits_a = arrcredits_1student(student_id)
    numerator1 = np.multiply(marks_a,credits_a)
    denominator = np.sum(credits_a)
    gpa = np.sum(numerator1)/denominator
    return gpa

def sort_gpa():
    gpa_student = {}
    for i in list_student:
        gpa_student[i._id] = cal_gpa(i._id)
    gpa_student_sorted = sorted(gpa_student.items(), key=lambda x: x[1], reverse=True)# sorted by value
    return gpa_student_sorted
#driver code
"\t\t\twelcome to the program".upper()
"\t\t\tbegin the program".upper()
print('\n')
while True:
    opt = int(input('\n----------------------------------------Menu--------------------------------------------\n\nEnter an option:\n  1.Input students info/add students\n  2.Input courses/add course\n  3.Add marks \n  4.Show marks 1 student\n  5.Show marks 1 course\n  6.Show list marks\n  7.Show list  students\n  8.Show list courses\n  9.Floor all marks\n  10.Calculate Gpa of 1 student\n  11.Sort by gpa\n  12.Exit\n'))
    if opt == 1:
        print('\n\t\t\t----------------------------------------Input students info--------------------------------------------\n')
        no_students = input_no_students()
        for i in range(no_students):
            name = input('Enter the name of student: ')
            DoB = input('Enter the DoB of student: ')
            id = input('Enter the id of student: ')
            ob = Student(name,DoB,id)
            ob.add_student()
        print('\n')
    elif opt == 2:  
        print('\n\t\t\t----------------------------------------Input courses info--------------------------------------------\n')
        no_course = input_no_courses()
        for i in range(no_course):
            '\n\t\t\t-------------------------------------------'
            id = input('Enter the ID of the course: ')
            name = input('Enter the name of the course: ')
            credit = int(input('Enter the credit of the course: '))
            ob_course = Course(id,name,credit)
            ob_course.add_course()   
    elif opt == 3:
        print('\n\t\t\t----------------------------------------Add marks--------------------------------------------\n')
        while True:
            course_id = input('Enter the course ID you want to add marks:')
            if course_id not in [i._id for i in list_course]:
                print('Course not found!')
                print('Enter again!')
                continue
            else:
                no_student_intake = int(input('Enter the number of students intake: '))
                while True:
                    #if the number of students intake is greater than the number of students or less than 0 then it will ask to input again
                    if no_student_intake > len(list_student) or no_student_intake < 0:
                        print('Invalid number of students intake!')
                        print('Enter again!')
                        continue
                    else:
                        for i in range(no_student_intake):
                            while True:
                                student_id = input('Enter the student ID: ')
                                if student_id not in [i._id for i in list_student]:
                                    print('Invalid student ID!')
                                    print('Enter again!')
                                    continue
                                else:
                                    while True:
                                        mark = float(input('Enter the mark: '))
                                        if mark <0 or mark >20:
                                            print('Invalid mark!')
                                            print('Enter again!')
                                            continue
                                        else:
                                            #take the first credit of the course that is satisfied the condition
                                            credit = [i._credit for i in list_course if i._id == course_id][0]
                                            ob_mark = Mark(student_id,course_id,mark,credit)
                                            ob_mark.add_mark()
                                            break# the loop of input mark
                                break# the loop of input student_id
                        break# the loop of input number of students intake
                break# the loop of input course_id
    elif opt == 4:
        print('\n\t\t\t----------------------------------------Show marks 1 student--------------------------------------------\n')
        while True:
            print('Enter the student ID you want to see the marks:')
            student_id = input('Enter the student ID: ')
            if student_id not in [i._sid for i in list_mark]:
                print('Invalid student ID!')
                print('Enter again!')
                continue
            else:
                show_marks_1student(student_id)
                break  
    elif opt ==5:
        print('\n\t\t\t----------------------------------------Show marks 1 course--------------------------------------------\n')
        print('Enter the course id you want to see the marks:')
        while True:
            course_id = input('Course id: ')
            if course_id not in [i._id for i in list_course]:
                print('Course not found!')
                print('Enter again!')
                continue
            else:
                show_marks_1course(course_id)
                break
    elif opt == 6:
        print('\n\t\t\t----------------------------------------Show list marks--------------------------------------------\n')
        show_list_mark()
    elif opt == 7:
        print('\n\t\t\t----------------------------------------Show list students--------------------------------------------\n')
        show_list_student()
    elif opt == 8:
        print('\n\t\t\t----------------------------------------Show list courses--------------------------------------------\n')
        show_list_course()
    elif opt == 9:
        print('\n\t\t\t----------------------------------------Floor all marks--------------------------------------------\n')
        update_marks_floor()
    elif opt == 10:
        print('\n\t\t\t----------------------------------------Calculate Gpa of 1 student--------------------------------------------\n')
        while True:
            student_id = input('Enter the student ID you want to see the marks: ')
            if student_id not in [i._sid for i in list_mark]:
                print('Invalid student ID!')
                print('Enter again!')
                continue
            else:
                print('The GPA of the student is: ',cal_gpa(student_id))
                break
    elif opt == 11:
        print('\n\t\t\t----------------------------------------Sort by gpa--------------------------------------------\n')
        print('Sorting by GPA:')
        sorted_gpa = sort_gpa()
        for i in sorted_gpa:
            print('The student ID: ',i[0],' has GPA: ',i[1],'\n')
    elif opt == 12:
        print('Thank you for using the program!')
        print('End the program!')
        break



