#init the list of students  the list of courses and the list of marks to store objects of class Student, Course and Mark
list_student = []
list_course = []
list_mark = []
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
        ob_mark = Mark(self._sid, self._cid, self._mark)
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
'Instructions:'
'There are 2 types of courses: Normal course and Special course'
'Normal course: all student are required to take the course'
'Special course: only some students are required to take the course'
print('\n')
while True:
    opt = int(input('\n----------------------------------------Menu--------------------------------------------\n\nEnter an option:\n  1.Input students info/add students\n  2.Input courses/add course\n  3.Add marks for normal courses in the list\n  4.Add marks for special course\n  5.Show marks of 1 student\n  6.Show the marks of a course\n  7.Show marks list\n  8.Show students list\n  9.Show course list\n 10.End the program\n\nYour choice: '))
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
            print('\n\t\t\t-------------------------------------------')
            while True:
                course_id = input('Course you want to add mark: ')
                if course_id not in [i._id for i in list_course]:
                    print('Course not found!')
                    print('Enter again!')
                    continue
                else:#input marks for a course
                    for j in range(0,len(list_student)):
                        print('Student ',j+1,': ',list_student[j]._name)
                        while True:
                            mark = float(input('Enter the mark: '))
                            if mark <0 or mark >20:
                                print('Invalid mark!')
                                print('Enter again!')
                                continue
                            else:
                                ob_mark = Mark(list_student[j]._id,course_id,mark)
                                ob_mark.add_mark()
                                break
                break    
    elif opt == 4:
        print('\n\t\t\t-------------------------------------------')
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
                                        for i in range(0,no_student_intake):
                                            ob_mark = Mark(student_id,course_id,mark)
                                            ob_mark.add_mark()
                                        break
                            break
                        break
                break
    elif opt == 5:
        print('\n\t\t\t-------------------------------------------')
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
    elif opt ==6:
        print('\n\t\t\t-------------------------------------------')
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
    elif opt == 7:
        print('\n\t\t\t-------------------------------------------')
        show_list_mark()
    elif opt == 8:
        print('\n\t\t\t-------------------------------------------')
        show_list_student()
    elif opt == 9:
        print('\n\t\t\t-------------------------------------------')
        show_list_course()
    elif opt == 10:
        print('\n\t\t\t-------------------------------------------')
        print('End the program!')
        break


