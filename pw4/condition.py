import domains.class_course as c
import domains.class_student as s
import domains.class_mark as m
def check_course(course_id):
    if course_id not in [i._id for i in c.list_course]:
        print('Course ID not found!')
        return True

def check_student(student_id):
    if student_id not in [i._id for i in s.list_student]:
        print('Student ID not found!')
        return True

def limit_mark(mark):
    if mark <0 or mark > 20:
        print('Mark is invalid!')
        return True

def check_mark_1student(student_id):
    if student_id not in [i._cid for i in m.list_mark]:
        print('Student ID not found!')
        return True

def limit_student(no_student):
    if no_student <0 or no_student > len(s.list_student):
        print('Invalid number of students!')
        return True
