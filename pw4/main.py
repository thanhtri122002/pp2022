import domains.class_mark as m
import domains.class_student as s
import domains.class_course as c
import input as inp
import math 

def show_list_student():
    print('List of students:')
    for i in s.list_student:
        print('Student ID:',i._id,'Name:',i._name,'DoB:',i._DoB)
        
def show_list_course():
    print('List of coursesL')
    for i in c.list_course:
        print('Course ID:',i._id,'Name:',i._name,'Credit:',i._credit)

def show_list_mark():
    print('List of marks:')
    for i in m.list_mark:
        print('Student ID:',i._sid,'Course ID:',i._cid,'Mark:',i._mark,'Credits:',i._credits)


def update_marks_floor():
    for i in m.list_mark:
        i._mark = math.floor(i._mark)
        print('Student ID:',i._sid,'Course ID:',i._cid,'Mark:',i._mark,'Credits:',i._credits)

while True:
    opt = int(input('1. Add student\n2. Add course\n3. Add mark\n4. Show list of students\n5. Show list of courses\n6. Show list of marks\n7.Show marks of a student\n8. Show marks of a course\n9. Floor all marks down\n10. Calculate GPA of a student\n11. Sorted students by GPA \n12. Exit\n'))
    if opt == 1:
        inp.input_info_student()
    elif opt == 2:
        inp.input_info_course()
    elif opt == 3:
        course_id = input('Enter course ID: ')
        inp.input_info_mark(course_id)
    elif opt == 4:
        show_list_student()
    elif opt == 5:
        show_list_course()
    elif opt == 6:
        show_list_mark()
    elif opt == 7:
        student_id = input('Enter student ID: ')
        inp.show_marks_1student(student_id)
    elif opt == 8:
        course_id = input('Enter course ID: ')
        inp.show_marks_1course(course_id)
    elif opt == 9:
        update_marks_floor()
    elif opt == 10:
        student_id = input('Enter student ID: ')
        print('GPA of student:',student_id,'is:',inp.cal_gpa(student_id))
    elif opt == 11:
        print('List of students sorted by GPA:')
        sorted_gpa = inp.sort_gpa()
        for i in sorted_gpa:
            print('Student Id', i[0],'GPA:',i[1])
    elif opt == 12:
        break



