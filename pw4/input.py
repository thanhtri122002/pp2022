import domains.class_student as s
import domains.class_course as c
import domains.class_mark as m
import condition as co
import numpy as np

def input_no_students():
    while True:
        no_students = int(input('Enter the number of students : '))
        if no_students <0:
            print('Invalid number of students!')
            print('Enter again!')
            continue
        else:
            return no_students

def input_no_courses():
    while True:
        no_course = int(input('Enter the number of courses: '))
        if no_course <0:
            print('Invalid number of courses!')
            print('Enter again!')
            continue
        else:
            return no_course

def input_info_student():
    no = input_no_students()
    for i in range(no):
        name = input('Enter student name: ')
        dob = input('Enter student DoB: ')
        student_id = input('Enter student ID: ')
        ob = s.Student(name, dob, student_id)
        ob.add_student()

def input_info_course():
    no = input_no_courses()
    for i in range(no):
        course_id = input('Enter course ID: ')
        name = input('Enter course name: ')
        credit = int(input('Enter course credit: '))
        ob = c.Course(course_id, name, credit)
        ob.add_course()

def input_info_mark(course_id):
    while True:
        if co.check_course(course_id) == True:
            print('Enter again!')
            continue
        else:
            no_student_intake = int(input('Enter the number of students of the course: '))
            while True:
                if co.limit_student(no_student_intake) == True:
                    print('Invalid number of students!')
                    print('Enter again!')
                    continue
                else:
                    for i in range(no_student_intake):
                        student_id = input('Enter student ID: ')
                        while True:
                            if co.check_student(student_id) == True:
                                print('Student ID not found!')
                                print('Enter again!')
                                continue
                            else:
                                mark = float(input('Enter mark: '))
                                while True:
                                    if co.limit_mark(mark) == True:
                                        print('Mark is invalid!')
                                        print('Enter again!')
                                        continue
                                    else:
                                        credits = [i._credit for i in c.list_course if i._id == course_id][0]
                                        ob = m.Mark(student_id,course_id, mark, credits)
                                        ob.add_mark()
                                        break
                                break
                    break
            break


def show_marks_1student(student_id):
    print('List of marks of student:',student_id)
    for i in m.list_mark:
        if i._sid == student_id:
            print('Student ID:',i._sid,'Course ID:',i._cid,'Mark:',i._mark,'Credits:',i._credits)

def show_marks_1course(course_id):
    print('List of marks of course:',course_id)
    for i in m.list_mark:
        if i._cid == course_id:
            print('Student ID:',i._sid,'Course ID:',i._cid,'Mark:',i._mark,'Credits:',i._credits)

def arrmarks_1student(student_id):
    marks_a = np.array([i._mark for i in m.list_mark if i._sid == student_id])
    return marks_a

def arrcredits_1student(student_id):
    credits_a = np.array([i._credits for i in m.list_mark if i._sid == student_id])
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
    for i in m.list_mark:
        gpa_student[i._sid] = cal_gpa(i._sid)
    sorted_gpa = sorted(gpa_student.items(), key=lambda x: x[1], reverse=True)
    return sorted_gpa
