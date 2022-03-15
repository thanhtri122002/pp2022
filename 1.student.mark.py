#init the list of students and the list of courses
list_student = []
list_course = []

#init the dictionary of students and the dictionary of courses
student = {"name":None,"id":None,"DoB":None}
course = {"id":None,"name":None}
#dict in list

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
        

#function to enter students info
#effect: add student info to list_student
def input_info(no_students):
    for i in range(0,no_students):
            print('===========INSERT STUDENT NUMBER',i+1,'===============')
            student_id = input('Enter the id of the student: ')
            student_name = input('Enter the name of the student: ')
            student_DoB = input('Enter the DoB of the student: ')
            student_info = {"id":student_id,"name":student_name,"DoB":student_DoB}
            list_student.append(student_info)
            print('===================END===================')
            print('\n')
    

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
   
#function to enter courses info
#effect: add courses info to list_course
def input_course_info(no_courses):
    for i in range(0,no_courses):
            print('===========INSERT COURSE NUMBER',i+1,'===============')
            course_id=input('Enter the id of the course: ')
            course_name=input('Enter the name of the course: ')
            course_info ={"course_id":course_id,"course_name":course_name}
            list_course.append(course_info)
            print('===================END===================')
            print('\n')

#function to enter students mark of a given course
#effect: add students mark to list_student
def input_marks_course():
    while True:
        course_selected = input('Enter the course id you want to select: ')
        if course_selected not in[x['course_id'] for x in list_course]:
                print('Course not found!')
                print('Enter the course id again!')
                continue
        break
    "course validated".upper()
    for i in range(0,len(list_student)):
        while True:
            mark = float(input('Enter the mark of the student: '))
            if mark <0 or mark >20:
                print('Invalid mark!')
                print('Enter again!')
                continue
            else:
                course_mark_dict = {"course_mark":mark,"course_selected":course_selected}#make a dict course mark
                list_student[i].update(course_mark_dict)#update the mark of the course in student dict
                list_course[i].update(course_mark_dict)#update the mark of the course in course dict
                print('Student mark updated!')
                print('\n')
                break
#note:


#function to show list of courses
#effect: show list of courses
#pre-condition: list_course is not empty
def list_courses():
    for i in range(0,len(list_course)):
        print('COURSE NUMBER ',i+1)
        print('Name: ',list_course[i].get("course_name"))
        print('ID: ',list_course[i].get("course_id"))

#function to show list of students
#effect: show list of students
#pre-condition: list_student is not empty
def list_students():
    for i in range(0,len(list_student)):
        print('STUDENT NUMBER ',i+1)
        print('Name: ',list_student[i].get("name"))
        print('ID: ',list_student[i].get("id"))
        print('DoB: ',list_student[i].get("DoB"))
        print('Course id: ',list_student[i].get("course_selected"))
        print('MARK: ',list_student[i].get("course_mark"))
        print('\n')

#function to show 1 student's mark of a given course
#effect: show 1 student's mark of a given course
course_id_show = {"course_id_show":None ,"course_mark_show":None}
def show_marks_1course():
    while True:
        course_id_show['course_id_show'] = input('Enter the course id you want to select: ')
        if course_id_show['course_id_show'] not in[x['course_id'] for x in list_course]:
            print('Course not found!')
            print('Enter the course id again!')
            continue
        break
    "course validated".upper()
    for i in range(0,len(list_student)):
        if course_id_show['course_id_show'] == list_student[i].get("course_selected"):
            print('STUDENT NUMBER ',i+1)
            print('Name: ',list_student[i].get("name"))
            print('ID: ',list_student[i].get("id"))
            print('DoB: ',list_student[i].get("DoB"))
            print('Course id: ',list_student[i].get("course_selected"))
            print('MARK: ',list_student[i].get("course_mark"))
            print('\n')

#main driver
"\t\t\tbegin the program".upper()
print('\n')
no_student = input_no_students()
no_course = input_no_courses()
input_info(no_student)
input_course_info(no_course)
while True:
    choice = int(input('\n----------------------------------------Menu--------------------------------------------\n\nEnter an option:\n  1.Insert marks for a course\n  2. List students\n  3. List courses\n  4. Show marks in a course\n  5. Exit\n\nYou choose: '))
    if choice == 1:
        input_marks_course()
    elif choice == 2:  
        list_students()
    elif choice == 3: 
        list_courses()
    elif choice == 4:
        show_marks_1course()
    elif choice == 5:
        break
    else:
        print('Invalid option!')