#init the list of students  the list of courses and the list of marks to store objects of class Student, Course and Mark
list_student = []
list_course = []
list_mark = []
#init dictionary to store students marks in 1 course
#key: student_id and course_mark (a dictionary)
student_course_mark = {'student_id': None, 'course_mark' :{'course_id':None, 'mark':None}}


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
        ob = Student(self._name,self._id,self._DoB)
        list_student.append(ob)
    
#function to show list_student
def show_list_student():
        print('List of students: ')
        for i in list_student:# i is a class 
            print('student_id: ',i._id,'\nstudent_name: ',i._name,'\nstudent_DoB: ',i._DoB)
            print('\n')

class Course:
    def __init__(self,id,name):
        self._id = id
        self._name = name
    def add_course(self):#method to add a course object to list_course
        ob_course = Course(self._id,self._name)
        list_course.append(ob_course)
    
class Mark():
    def __init__(self,sid,cid,mark):
        self._sid = sid
        self._cid = cid
        self._mark = mark
    def add_mark(self):#method to add a mark object to list_mark
            for j in list_student:
                student_course_mark['student_id'] = j._id
                for i in list_course:
                    student_course_mark['course_mark']['course_id'] = i._id
                while True:
                    student_course_mark['course_mark']['mark'] = float(input('Enter the mark of student: '))
                    if student_course_mark['course_mark']['mark'] <0 or student_course_mark['course_mark']['mark'] > 20:
                        print('Invalid mark!')
                        print('Enter again!')
                        continue
                    else:
                        ob_mark = Mark(student_course_mark['student_id'],
                        student_course_mark['course_mark']['course_id'],
                        student_course_mark['course_mark']['mark'])
                        list_mark.append(ob_mark)#list of object marks
                        break
                print('\n')
    

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
            print('course_id: ',i._id,'\ncourse_name: ',i._name)
            print('\n')

#function to show marks of a course
def show_marks_1course(course_id):
            for i in list_mark:#i is objects of class Mark
                if i._cid == course_id:
                    print('student_id: ',i._sid,
                    '\ncourse_id: ',i._cid,
                    '\nmark: ',i._mark)
                    print('\n')

#function to show a student'marks in all course
def show_marks_1student(student_id):
            for i in list_mark:
                if i._sid == student_id:
                    print('student_id: ',i._sid,
                    '\ncourse_id: ',i._cid,
                    '\nmark: ',i._mark)
                    print('\n')
                       
#driver code
"\t\t\twelcome to the program".upper()
"\t\t\tbegin the program".upper()
print('\n')
while True:
    opt = int(input('\n----------------------------------------Menu--------------------------------------------\n\nEnter an option:\n  1.Input students info/add students\n  2.Input courses/add course\n  3.Add marks for all courses in the list\n  4.Show the course list\n  5.Show the student list\n  6.Show the marks\n  7.Show marks 1 course\n  8.Show marks of 1 student\n  9.End the program\n\nYour choice: '))
    if opt == 1:
        no_student = input_no_students() 
        for i in range(no_student):
            '\n\t\t\t-------------------------------------------'
            name = input('Enter the name of the student: ')
            id = input('Enter the ID of the student: ')
            DoB = input('Enter the DoB of the student: ')
            ob = Student(name,id,DoB)
            ob.add_student()
    elif opt == 2:  
        no_course = input_no_courses()
        for i in range(no_course):
            '\n\t\t\t-------------------------------------------'
            id = input('Enter the ID of the course: ')
            name = input('Enter the name of the course: ')
            ob_course = Course(id,name)
            ob_course.add_course()
    elif opt == 3:
        for i in list_course:
            print('\n\t\t\t-------------------------------------------')
            print('\n\t\t\t\tCourse ID: ',i._id)
            ob_mark = Mark(0,i._id,0)
            ob_mark.add_mark()
    elif opt == 4:
        print('\n\t\t\t-------------------------------------------')
        show_list_course()
    elif opt == 5:
        print('\n\t\t\t-------------------------------------------')
        show_list_student()
    elif opt ==6:
        print('\n\t\t\t-------------------------------------------')
        show_list_mark()
    elif opt == 7:
        print('\n\t\t\t-------------------------------------------')
        print('Enter the course id you want to see the marks:')
        while True:
            course_id = input('Enter the course id: ')
            if course_id == '' or course_id not in [i._cid for i in list_mark]:
                print('Invalid course name!')
                print('Enter again!')
                continue
            else:
                show_marks_1course(course_id)
                break
    elif opt == 8:
        print('\n\t\t\t-------------------------------------------')
        while True:
            print('Enter the student ID you want to see the marks:')
            student_id = input('Enter the student ID: ')
            if student_id == '':
                print('Invalid student ID!')
                print('Enter again!')
                continue
            else:
                show_marks_1student(student_id)
                break  
    elif opt == 9:
        print('\n\t\t\t-------------------------------------------')
        print('\n\t\t\t\tThank you for using the program!')
        break
    else:
        print('\n\t\t\t-------------------------------------------')
        print('Invalid option!')
        print('\n\t\t\t-------------------------------------------')
        continue


