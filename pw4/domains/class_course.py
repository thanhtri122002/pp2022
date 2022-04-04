list_course = []
class Course:
    def __init__(self,id,name,credit):
        self._id = id
        self._name = name
        self._credit = credit
    def add_course(self):#method to add a course object to list_course
        ob_course = Course(self._id,self._name,self._credit)
        list_course.append(ob_course)