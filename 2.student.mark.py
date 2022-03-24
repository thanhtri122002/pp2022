#init the list of students and the list of courses
list_student = []
list_course = []
student_course_mark = {'student_id': None, 'course_mark' :{'course_name':None, 'mark':None}}
list_mark = []


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
    def __init__(self,name,id,DoB):
        self.name = name
        self.id = id
        self.DoB = DoB
    def __str__(self):
        return 'Name: '+self.name+'\nID: '+self.id+'\nDoB: '+self.DoB

class Student(Person):
    def __init__(self,name,id,DoB):
        super().__init__(name,id,DoB)
    def add_student(self):
        ob = Student(self.name,self.id,self.DoB)
        list_student.append(ob)

def show_list_student():
        print('List of students: ')
        for i in list_student:# i is a class 
            print('student_id: ',i.id,'\nstudent_name: ',i.name,'\nstudent_DoB: ',i.DoB)
            print('\n')
        


class Course:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def add_course(self):
        ob_course = Course(self.id,self.name)
        list_course.append(ob_course)

class Mark():
    def __init__(self,id,name,mark):
        self.id = id
        self.name = name
        self.mark = mark
    def add_mark(self):
            for j in list_student:
                student_course_mark['student_id'] = j.id
                student_course_mark['course_mark']['course_name'] = i.name
                student_course_mark['course_mark']['mark'] = int(input('Enter the mark of the course: '))
                ob_mark = Mark(student_course_mark['student_id'],student_course_mark['course_mark']['course_name'],student_course_mark['course_mark']['mark'])
                list_mark.append(ob_mark)
                print('\n')
        
                

def show_list_mark():
        print('List of marks: ')
        for i in list_mark:
            print('student_id: ',i.id,'\ncourse_name: ',i.name,'\nmark: ',i.mark)
            print('\n')
        
def show_list_course():
        print('List of courses: ')
        for i in list_course:
            print('course_id: ',i.id,'\ncourse_name: ',i.name)
            print('\n')

#driver
"\t\t\tbegin the program".upper()
print('\n')
no_student = input_no_students()
no_course = input_no_courses()
while True:
    opt = int(input('\n----------------------------------------Menu--------------------------------------------\n\nEnter an option:\n  1.Input students info\n  2.Input courses\n  3.Add marks 1 course\n  4.Show the course list\n  5.Show the student list\n6.Show the marks for a course\n\nYour choice: '))
    if opt == 1:
        for i in range(no_student):
            '\n\t\t\t-------------------------------------------'
            name = input('Enter the name of the student: ')
            id = input('Enter the ID of the student: ')
            DoB = input('Enter the DoB of the student: ')
            ob = Student(name,id,DoB)
            ob.add_student()
    elif opt == 2:  
        for i in range(no_course):
            '\n\t\t\t-------------------------------------------'
            id = input('Enter the ID of the course: ')
            name = input('Enter the name of the course: ')
            ob_course = Course(id,name)
            ob_course.add_course()
    elif opt == 3:
        for i in list_course:
            print('\n\t\t\t-------------------------------------------')
            print('\n\t\t\t\tCourse ID: ',i.id)
            ob_mark = Mark(i.id,i.name,0)
            ob_mark.add_mark()
    elif opt == 4:
        print('\n\t\t\t-------------------------------------------')
        show_list_course()
    elif opt == 5:
        print('\n\t\t\t-------------------------------------------')
        show_list_student()
    elif opt ==6:
        print('\n\t\t\t-------------------------------------------')
        course_id = input('Enter the ID of the course: ')
        show_list_mark()
    else:
       print('bye bye')
       break



